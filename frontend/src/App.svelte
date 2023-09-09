<script>
	import DecoSelector from "./DecoSelector.svelte";
	import Modal from "./Modal.svelte";
	import Slider from "./Slider.svelte";
</script>

<main>
	<Slider />
	<DecoSelector />
</main>

<style>
	main {
		width: 100%;
		height: 100%;
		text-align: center;
		padding: 1em;
		max-width: 100%;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
		flex-direction: column;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
