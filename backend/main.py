from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv('../.env')

from config import API_HOST, API_PORT, account_phone
from routes.contacts import contacts
from routes.message import message

API = Flask(__name__)

API.register_blueprint(contacts, url_prefix="/contacts")
API.register_blueprint(message, url_prefix="/message")
CORS(API)

def main():
  API.run(host=API_HOST, port=int(API_PORT))

if __name__ == "__main__":
    main();
