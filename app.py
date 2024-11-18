# app.py
import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from data_processing import load_data
from email_service import generate_and_send_emails
from analytics import get_email_status
from flask import jsonify
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Home route with form to upload CSV and enter the prompt
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # File upload and form handling
        file = request.files.get("file")
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Load data and get prompt template
            data = load_data(file_path)
            prompt_template = request.form.get("prompt_template")

            # Get sender email credentials
            sender_email = request.form.get("sender_email")
            sender_password = request.form.get("sender_password")

            # Generate and send emails with credentials
            generate_and_send_emails(data, prompt_template, sender_email, sender_password)

            return redirect(url_for('analytics'))
    
    return render_template("index.html")

# Analytics route to display email status
# @app.route("/analytics")
# def analytics():
#     status_data = get_email_status()
#     return render_template("analytics.html", status_data=status_data)


@app.route("/analytics")
def analytics():
    status_data = get_email_status()
    if request.headers.get("accept") == "application/json":
        # Return JSON for real-time updates
        return jsonify(status_data)
    else:
        # Render HTML template for first-time load
        return render_template("analytics.html", status_data=status_data)
    
if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,port=5005)
