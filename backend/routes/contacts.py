import json
from os import path
from flask import Blueprint, jsonify

contacts = Blueprint('contacts', __name__)

def find_contact(id):
  with open(path.join('data', 'contacts.json')) as contact_file:
    contact_list = json.load(contact_file)
    contact_file.close()
    for contact in contact_list['contacts']:
      if contact['id'] == id:
        return contact

@contacts.route('/', methods=['GET'])
def get_all_contacts():
  with open(path.join('data', 'contacts.json')) as contact_file:
    contact_list = json.load(contact_file)
    contact_file.close()
    return jsonify(contact_list['contacts'])

@contacts.route('/<string:id>/', methods=['GET'])
def get_contact_by_id(id):
  return jsonify(find_contact(id))
