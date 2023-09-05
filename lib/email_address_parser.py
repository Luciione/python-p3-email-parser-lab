import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        email_list = re.split(r'[,\s]+', self.email_addresses)
        
        valid_emails = []
        
        # Define a regular expression pattern for a valid email address
        email_pattern = r'^[\w\.-]+@[\w\.-]+$'
        
        for email in email_list:
            email = email.strip()
            
            # Check if the string matches the email pattern
            if re.match(email_pattern, email):
                valid_emails.append(email)
        
        sorted_emails = sorted(valid_emails)
        
        return sorted_emails
