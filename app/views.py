from flask import Blueprint, render_template, request, jsonify
from app.models import EmailLog
from app import db
from app.email_service import send_email

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main_bp.route("/send_ajax", methods=["POST"])
def send_ajax():
    try:
        recipient = request.form.get("recipient")
        subject = request.form.get("subject")
        body = request.form.get("body")

        if not recipient or not subject or not body:
            return jsonify({
                "success": False,
                "message": "Alguns campos obrigatórios estão vazios."
            }), 400

        attachments = []
        if "attachment" in request.files:
            file = request.files["attachment"]
            if file and file.filename != "":
                file_data = file.read()
                attachments.append(
                    (file.filename, file.mimetype, file_data)
                )

        send_email(subject, body, [recipient], attachments)
        log = EmailLog(
            recipient=recipient,
            subject=subject,
            status="Enviado",
            error=""
        )
        db.session.add(log)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Email enviado com sucesso!"
        })

    except Exception as error:
        log = EmailLog(
            recipient=request.form.get("recipient", ""),
            subject=request.form.get("subject", ""),
            status="Erro",
            error=str(error)
        )
        db.session.add(log)
        db.session.commit()

        return jsonify({
            "success": False,
            "message": f"Erro ao enviar o e-mail: {str(error)}"
        }), 500


@main_bp.route("/history_data", methods=["GET"])
def history_data():
    try:
        logs = EmailLog.query.order_by(EmailLog.timestamp.desc()).all()

        data = []
        for log in logs:
            data.append({
                "id": log.id,
                "recipient": log.recipient,
                "subject": log.subject,
                "status": log.status,
                "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "error": log.error or ""
            })

        return jsonify({"success": True, "history": data})

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Erro ao carregar histórico: {str(e)}"
        }), 500
