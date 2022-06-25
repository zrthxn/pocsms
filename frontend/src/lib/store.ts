import { writable } from 'svelte/store';

import type { Contact } from './api';

export const contacts = writable<Contact[]>();
