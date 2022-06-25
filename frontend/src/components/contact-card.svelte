<script lang="ts">
	import { goto } from '$app/navigation';
	import type { Contact } from '$lib/api';

	export let contact: Contact;

	const openContact = () => {
		goto(`/contact/${contact.id}`);
	};
</script>

<div class="card" on:click={openContact}>
	<h3>{contact.firstname}</h3>
	<h2>{contact.lastname}</h2>

	<span>{contact.phone}</span>
</div>
