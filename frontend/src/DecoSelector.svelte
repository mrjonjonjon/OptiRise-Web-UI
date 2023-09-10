<script>
    import AutoComplete from "simple-svelte-autocomplete";
    import Switch from "svelte-switch";
    import ToggleSwitch from "./ToggleSwitch.svelte";
    import SingleDecoSelector from "./SingleDecoSelector.svelte";

    let numSelectors = 2;

    let selectors = Array(numSelectors).fill(null);
    const addSelector = () => {
        if (numSelectors < 45) {
            numSelectors += 1;
            selectors.push(null); // Add a new slot for the new component instance
        }
    };
    const removeSelector = () => {
        if (numSelectors > 0) {
            numSelectors -= 1;
            selectors.pop(); // Remove the last component instance reference
        }
    };

    let aggregatedData = [];

    async function gatherAndSendData() {
        aggregatedData = selectors.map((child) =>
            child ? child.getData() : {}
        );

        console.log(aggregatedData);
        try {
            const response = await fetch("http://127.0.0.1:5000/send_data", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(aggregatedData),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const responseData = await response.json();
            console.log("Data sent and response received:", responseData);
        } catch (error) {
            console.error("Error sending data:", error);
        }
    }
</script>

<ToggleSwitch />
<div>
    {#each { length: numSelectors } as _, i}
        <SingleDecoSelector bind:this={selectors[i]} />
    {/each}
</div>

<button on:click={addSelector}>+</button>
<button on:click={removeSelector}>-</button>
<button on:click={gatherAndSendData}>SUBMIT</button>

<style>
    div {
        display: flex;
        flex-direction: column;

        flex-wrap: wrap;
        width: 80vw;
        height: 60vw;
    }
</style>
