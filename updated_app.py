
import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify
from groq import Groq

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize Groq client with the API key
client = Groq(api_key="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")

# Function to generate an email using the Groq API
def generate_email(name, place, product):
    prompt = (
        f"Generate a friendly and professional email to {name} in {place}, "
        f"introducing our product '{product}'. Mention how it can benefit them and include a call-to-action."
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content

# Home route with form to upload CSV and enter details
@app.route("/", methods=["GET", "POST"])
def index():
    emails = []
    if request.method == "POST":
        # File upload and form handling
        file = request.files.get("file")
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Load data
            data = pd.read_csv(file_path)
            
            # Collect template and sender details
            prompt_template = request.form.get("prompt_template")
            sender_email = request.form.get("sender_email")
            sender_password = request.form.get("sender_password")

            # Generate emails based on the CSV data
            for _, row in data.iterrows():
                name = row.get("Name", "Valued Customer")
                place = row.get("Location", "your area")
                product = row.get("Product", "our product")
                email_content = generate_email(name, place, product)
                emails.append({"name": name, "email": row.get("Email", ""), "content": email_content})

        return render_template("updated_index.html", emails=emails)
    
    return render_template("updated_index.html", emails=emails)

# Route to handle sending emails (currently simulated)
@app.route("/send_email", methods=["POST"])
def send_email():
    email = request.form.get("email")
    content = request.form.get("content")
    # Simulate sending email - actual email-sending logic can be added here
    return jsonify({"status": "success", "message": f"Email sent to {email}"})

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, port=5005)
