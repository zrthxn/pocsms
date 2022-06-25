<script lang="ts">
	/** @description User pages, Layout imports */

	import Header from '$comp/header.svelte';
	import Footer from '$comp/footer.svelte';

	import '$lib/global.styles.scss';
</script>

<main>
	<Header />

	<section>
		<slot />
	</section>

	<Footer />
</main>

<style lang="scss">
	main {
		section {
			max-width: 1000px;
			margin: auto;
			padding: 2em 1em;
		}
	}
</style>
