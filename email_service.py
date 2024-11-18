
# email_service.py
import smtplib
from groq import Groq
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from analytics import update_status

# Initialize Groq client with API key
client = Groq(api_key="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")

def generate_email_content(prompt_template, row_data):
    """
    Uses the prompt template and row data to generate customized email content.
    Calls Groq API to personalize the email with LLM.
    """
    # Replace placeholders with actual row data in the prompt template
    prompt = prompt_template.format(**row_data)

    # Using Groq API to generate enhanced email content
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192"
    )
    
    # Extract and return the generated message
    return response.choices[0].message.content

def send_email(recipient_email, subject, content, sender_email, sender_password):
    """
    Sends an email with the provided subject and content.
    Uses SMTP to send the email via the sender's account.
    """
    try:
        # Setup the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        # Successfully sent, update status
        print(f"Email sent to {recipient_email}")
        update_status(recipient_email, "sent")

    except smtplib.SMTPAuthenticationError:
        print(f"Authentication error: Check email and password for {sender_email}")
        update_status(recipient_email, "failed")

    except smtplib.SMTPException as e:
        print(f"SMTP error when sending email to {recipient_email}: {e}")
        update_status(recipient_email, "failed")

    except Exception as e:
        print(f"Unexpected error when sending email to {recipient_email}: {e}")
        update_status(recipient_email, "failed")

def generate_and_send_emails(data, prompt_template, sender_email, sender_password):
    """
    Generates and sends emails for each recipient based on the data and prompt template.
    
    Args:
        data (DataFrame): Loaded data as a pandas DataFrame.
        prompt_template (str): The template for email content.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
    """
    subject = "Personalized Offer from Our Company"

    for _, row in data.iterrows():
        row_data = row.to_dict()
        # Generate email content with Groq API
        email_content = generate_email_content(prompt_template, row_data)
        recipient_email = row_data.get("Email")
        
        # Send email with provided sender credentials
        send_email(recipient_email, subject, email_content, sender_email, sender_password)
