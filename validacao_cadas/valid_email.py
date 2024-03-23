import re

def validar_email(email):
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(regex_email, email):
        return True
    else:
        return False
