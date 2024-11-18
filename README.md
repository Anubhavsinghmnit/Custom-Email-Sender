# Custom-Email-Sender
an app to generate the custom email using LLM and then send that email to a list of people using CSV file which is customized on their data 
Table of Contents
Project Overview
Features
Project Structure
Technologies Used
Setup and Installation
How to Run
Usage
Email Generation and Sending
Analytics Dashboard
Contributing
License
Project Overview
This project is a Custom Email Generator and Analytics Dashboard built using Flask. It allows users to:

Upload a CSV file with recipient details.
Use a customizable email template with placeholders.
Generate and send personalized emails via an SMTP service.
Track email statuses, including successful deliveries, failures, and opens.
The application also features an Analytics Dashboard for monitoring email delivery performance and individual email statuses.

Features
Dynamic Email Personalization: Supports placeholder values like {Name}, {Location}, etc., to tailor each email.
CSV Upload Support: Easily upload recipient data in CSV format.
SMTP Integration: Send emails directly using your email credentials.
Real-Time Analytics: Monitor the status of sent emails (e.g., sent, failed, opened).
User-Friendly Interface: Clean and responsive design for ease of use.
Project Structure
php
Copy code
project/
├── app.py               # Flask application
├── templates/           # HTML templates for the application
│   ├── index.html       # Main page for email generation
│   ├── analytics.html   # Dashboard for email analytics
├── static/              # Static files (CSS, JavaScript, images)
│   ├── style.css        # Stylesheet for the application
├── email_services.py    # Module for handling email sending
├── README.md            # Project documentation
Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS
SMTP: Email services using Python's smtplib
Setup and Installation
Prerequisites
Python 3.7 or later installed on your machine.
A valid email account (e.g., Gmail) with SMTP access enabled.
Installation Steps
Clone the repository:
bash
Copy code
git clone <repository_url>
cd project
Install the required Python packages:
bash
Copy code
pip install flask
How to Run
Start the Flask application:
bash
Copy code
python app.py
Open your browser and visit:
arduino
Copy code
http://127.0.0.1:5000
Usage
Email Generation and Sending
Go to the Custom Email Generator Dashboard:

Upload a CSV file with recipient details (columns like Name, Email, etc.).
Enter a personalized email template using placeholders (e.g., Hello {Name}).
Provide your email address and password for sending emails.
Click Generate and Send Emails to initiate the process.
Example CSV format:

sql
Copy code
Name,Email,Location
John Doe,john.doe@example.com,New York
Jane Smith,jane.smith@example.com,Los Angeles
Example email template:

sql
Copy code
Hello {Name},

We are excited to introduce our new product in {Location}.
Analytics Dashboard
Visit the Email Analytics Dashboard:
View overall email statuses: Sent, Pending, Failed, Opened.
Check individual email statuses.

