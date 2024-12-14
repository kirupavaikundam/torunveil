import email
from email.parser import BytesParser
from email.policy import default

def extract_metadata(raw_email):
    email_data = BytesParser(policy=default).parsebytes(raw_email.encode())
    metadata = {
        "From": email_data['From'],
        "To": email_data['To'],
        "Subject": email_data['Subject'],
        "Date": email_data['Date']
    }
    return metadata
