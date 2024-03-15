admin_emails = ["info@ahbfinance.com", "root"]

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.admin = False
        
        if email in admin_emails:
            self.admin = True
        
         

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def update_email(self, new_email):
        self.email = new_email