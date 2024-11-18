# analytics.py

from collections import defaultdict

# Initialize an in-memory data structure to store email status metrics
email_status = {
    "sent": 0,
    "pending": 0,
    "failed": 0,
    "opened": 0  # Requires ESP support to track opens
}

# Dictionary to keep individual email statuses by recipient
individual_status = defaultdict(lambda: {"status": "pending", "opened": False})

def update_status(recipient_email, status):
    """
    Update the status of a specific email and adjust the global status metrics.
    
    Args:
        recipient_email (str): The email address of the recipient.
        status (str): The new status ('sent', 'failed', or 'opened').
    """
    # Adjust individual status
    individual_status[recipient_email]["status"] = status

    # Adjust global metrics based on status
    if status == "sent":
        email_status["sent"] += 1
    elif status == "failed":
        email_status["failed"] += 1
    elif status == "opened":
        individual_status[recipient_email]["opened"] = True
        email_status["opened"] += 1

def get_email_status():
    """
    Retrieve the current email status metrics for display on the dashboard.
    
    Returns:
        dict: A dictionary containing overall email status counts.
    """
    return {
        "summary": email_status,
        "details": dict(individual_status)  # Convert defaultdict to regular dict for easy display
    }

# Mock function to simulate tracking opens via an ESP webhook
def track_open(recipient_email):
    """
    Simulate tracking an email open (for ESPs with open-tracking capability).
    
    Args:
        recipient_email (str): The email address of the recipient.
    """
    update_status(recipient_email, "opened")
