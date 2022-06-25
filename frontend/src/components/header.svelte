<header>
	<div class="container">
		<a href="/">Contacts</a>
		<a href="/messages">Messages</a>
	</div>
</header>

<style lang="scss">
	@import '../lib/variables.styles.scss';

	header {
		padding: 1em 0;
		display: flex;
		background-color: $colorAccent;

		.container {
			max-width: 1000px;
			margin: auto;
			padding: 1em;
		}

		a {
			margin-right: 2em;
			color: white;
		}
	}
</style>
