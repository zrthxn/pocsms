<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { contacts } from '$lib/store';
	import { getContactById, type Contact } from '$lib/api';
	import Spinner from '$comp/spinner.svelte';

	let contact: Contact;

	onMount(async () => {
		let search;
		if ($contacts) search = $contacts.find(({ id }) => id === $page.params.contactId);

		if (search) contact = search;
		else contact = await getContactById($page.params.contactId);
	});

	const composeMessage = () => {
		if (contact) goto(`/compose/${contact.id}`);
		else alert('Error: Unknown contact!');
	};
</script>

{#if contact}
	<h2>Contact</h2>

	<section class="card contact-details">
		<h1 class="contact-name">{contact.firstname} {contact.lastname}</h1>

		<span>Phone</span>
		<h3 class="contact-phone">
			<a href="tel:+{contact.phone}">{contact.phone}</a>
		</h3>

		<span>Address</span>
		<h3><a href="#address">{contact.address}</a></h3>

		<button class="large" on:click={composeMessage}>
			<b>Send Message</b>
		</button>
	</section>
{:else}
	<Spinner />
{/if}

<style lang="scss">
	.contact-details {
		margin: 1em 0;
		padding: 2em;

		span {
			color: gray;
		}

		button {
			margin-top: 2em;
			right: 0;
		}
	}
</style>
