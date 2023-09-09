<script>
    let showModal = true;
    let s = "abcde";
</script>

<button
    on:click={() => {
        showModal = !showModal;
    }}>Toggle Modal</button
>

{#if showModal}
    <main>
        <p>{s}</p>
        <button
            on:click={() => {
                showModal = !showModal;
            }}>Toggle Modal</button
        >
        <p>Hi</p>
    </main>
{/if}

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
        background-color: aqua;
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
