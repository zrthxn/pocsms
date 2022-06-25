<script>
	export let notext = false;
	export let center = false;

	if (center) notext = true;
</script>

<div class="spin-container {center ? 'center' : ''}">
	<div class="spinner" />
	{#if !notext}
		<span>Loading</span>
	{/if}
</div>

<style lang="scss">
	.spin-container {
		width: 100%;
		height: 20px;
		padding: 1em 0;

		position: relative;

		display: flex;
		flex-direction: column;
		align-content: center;

		span {
			margin: auto;
			margin-left: 30px;
			font-weight: 600;
			color: gray;
		}

		.spinner:before {
			content: '';
			position: absolute;
			width: 14px;
			height: 14px;

			border-radius: 50%;
			border: 3px solid #222;
			border-top-color: #ccc;
			animation: spinner 0.6s linear infinite;
		}

		@keyframes spinner {
			to {
				transform: rotate(360deg);
			}
		}

		&[class~='center'] {
			.spinner:before {
				left: 50%;
				margin-left: -7px;
			}
		}
	}
</style>
