<script lang="ts">
	import Spinner from '$comp/spinner.svelte';
	import { listMessagesSent } from '$lib/api';

	async function getMessages() {
		let messages = await listMessagesSent();
		return messages.sort((a, b) => {
			return new Date(b.time).getTime() - new Date(a.time).getTime();
		});
	}
</script>

<h1>Messages</h1>
<br /><br />

{#await getMessages()}
	<Spinner />
{:then value}
	<section class="card">
		<div class="message-log">
			<span><b>Contact Name</b></span>
			<span><b>Message Timestamp</b></span>
			<span><b>OTP</b></span>
		</div>

		{#each value as message}
			<div class="message-log">
				<span><a href={`/contact/${message.contact_id}`}>{message.contact_name}</a></span>
				<span>
					{new Date(message.time).toDateString()}
					{new Date(message.time).toLocaleTimeString()}
				</span>
				<span><code>{message.otp}</code></span>
			</div>
		{/each}
	</section>
{/await}

<style lang="scss">
	.message-log {
		margin: 0 1em;
		padding: 1em 0;

		border-bottom: 1px solid lightgray;
		display: grid;
		grid-template-columns: 2fr 3fr 1fr;

		&:first-of-type {
			border-bottom: 2px solid gray;
		}

		&:last-of-type {
			border-bottom: none;
		}

		span {
			&:last-of-type {
				text-align: right;
			}
		}

		@media (max-width: 400px) {
			& {
				grid-template-columns: 1fr;
			}
		}
	}
</style>
