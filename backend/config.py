import os

# Twilio Account SID and Auth Token from twilio.com/console
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
account_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
account_phone = os.getenv('TWILIO_PHONE_NUMBER')

API_HOST = os.getenv('BACKEND_HOSTN')
API_PORT = os.getenv('BACKEND_PORT')

if __name__ == "__main__":
  raise ImportError("Do not run this file.")
