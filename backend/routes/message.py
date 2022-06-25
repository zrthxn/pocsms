import json
import pytz
from os import path
from datetime import datetime
from flask import Blueprint, jsonify, request
from twilio.rest import Client
from routes.contacts  import find_contact
from config import account_sid, account_auth_token, account_phone

message = Blueprint('message', __name__)
client = Client(account_sid, account_auth_token)

@message.route('/send/', methods=['POST'])
def send_msg_to():  
  _id = request.json['id']
  otp = request.json['otp']
  
  contact = find_contact(_id)
  
  try:
    message = client.messages \
                  .create(
                      body=f"Hi. Your OTP is {otp}.",
                      from_=account_phone,
                      to=contact['phone']
                  )

    with open(path.join('data', 'messages.json'), "r") as message_file:
      message_list = json.load(message_file)
      message_list["messages"].append({"contact_id": _id, 
                                       "contact_name": f'{contact["firstname"]} {contact["lastname"]}',
                                       "otp": otp,
                                       "time": str(datetime.now(tz=pytz.timezone('Asia/Kolkata')))})
      
    with open(path.join('data', 'messages.json'), "w") as message_file:
      message_file.write(json.dumps(message_list, indent=2))
      
    return jsonify({"status": message.status,
                    "err": message.error_code,
                    "message": message.error_message,
                    "to": message.to})
  except Exception as E:
    print(E)
    return jsonify({ "err": 500, "message": "Something went wrong!"})


@message.route('/list/', methods=['GET'])
def list_sent():
  with open(path.join('data', 'messages.json')) as message_file:
    message_list = json.load(message_file)
    message_file.close()
    return jsonify(message_list["messages"])
