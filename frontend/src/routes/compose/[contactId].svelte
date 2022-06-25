<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { contacts } from '$lib/store';
	import { sendMessageById } from '$lib/api';
	import Spinner from '$comp/spinner.svelte';

	$: contact = $contacts.find(({ id }) => id === $page.params.contactId);
	$: OTP = String();

	function otpgen(length: number = 6) {
		let otp = String();
		while (length > 0) {
			otp += Math.floor(Math.random() * 10).toString(10);
			length--;
		}
		OTP = otp;
	}

	onMount(() => {
		otpgen(6);
	});

	let sending = { status: '', err: 0, message: '', to: '' };
	async function sendMessage() {
		sending.status = 'sending';
		if (contact) sending = await sendMessageById(contact.id, OTP);
		else alert('Error: Unknown Contact!');
	}
</script>

{#if contact}
	<h2>Compose</h2>

	<section class="card contact-message">
		<h3>Send a Message to {contact.firstname}</h3>

		<div class="message-text">
			<input
				id="sms"
				type="text"
				placeholder="Your Message Here"
				disabled
				value={OTP ? `Hi. Your OTP is ${OTP}.` : ''}
			/>

			<button class="large" on:click={sendMessage}>
				{#if sending.status == 'sending'}
					<Spinner notext center />
				{:else if sending.status == 'sent' || sending.status == 'queued'}
					<b>Sent</b>
				{:else if sending.err}
					<b>{sending.message}</b>
				{:else}
					<b>Send</b>
				{/if}
			</button>
		</div>
	</section>
{:else}
	<Spinner />
{/if}

<style lang="scss">
	.contact-message {
		margin: 1em 0;
		padding: 2em;

		.message-text {
			display: grid;

			input {
				text-align: center;
			}
		}
	}
</style>
