import axios from 'axios'
import { API_HOST } from '$lib/env'

const request = axios.create({
  baseURL: API_HOST,
  timeout: 10000
})

export interface Contact {
  id: string
  firstname: string
  lastname: string
  address: string
  phone: string
}

export interface MessageLog {
  contact_id: string
  contact_name: string
  otp: string
  time: string
}

export async function getAllContacts() {
  try {
    const contacts = await request.get('/contacts/')
    return contacts.data as Contact[]
  } catch (error) {
    console.error(error)
    return [] as Contact[]
  }
}

export async function getContactById(id: string) {
  const contact = await request.get(`/contacts/${id}/`)
  return contact.data as Contact
}

export async function sendMessageById(id: string, otp: string) {
  const sender = await request.post(`/message/send/`, { id, otp })
  return sender.data
}

export async function listMessagesSent() {
  const messages = await request.get(`/message/list/`)
  return messages.data as MessageLog[]
}
