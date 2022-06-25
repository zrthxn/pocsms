<script lang="ts">
	import ContactCard from '$comp/contact-card.svelte';
	import Spinner from '$comp/spinner.svelte';
	import { getAllContacts } from '$lib/api';
	import { contacts } from '$lib/store';

	async function fetchContacts() {
		const data = await getAllContacts();
		contacts.set(data);
		return data;
	}
</script>

<h1>Contacts</h1>
<br /><br />

{#await fetchContacts()}
	<Spinner />
{:then value}
	<div id="contacts-container">
		{#each value as contact}
			<ContactCard {contact} />
		{/each}
	</div>
{/await}

<style lang="scss">
	#contacts-container {
		display: grid;
		gap: 1em;
		grid-template-columns: 1fr 1fr 1fr;

		@media (max-width: 400px) {
			grid-template-columns: 1fr;
		}
	}
</style>
