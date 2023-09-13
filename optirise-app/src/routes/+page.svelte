<script>
  import DecoSelector from "./DecoSelector.svelte";
  import Switch from "@smui/switch";
  import Tabs from "./Tabs.svelte";
  import LayoutGrid, { Cell } from "@smui/layout-grid";
  import { scale } from "svelte/transition";
  import ArmorPieceInspector from "./ArmorPieceInspector.svelte";
  import DetailedSetViewer from "./DetailedSetViewer.svelte";

  import Autocomplete from "@smui-extra/autocomplete";

  import Select, { Option } from "@smui/select";
  import Chip, { Set, TrailingAction, Text } from "@smui/chips";
  import Button, { Label } from "@smui/button";

  let fruits = ["Apple", "Orange", "Banana", "Mango"];
  let valueOutlined;
  let numSelectors = 2;
  let selectors = Array(numSelectors).fill(null);

  let currentTab;
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

  function handleActiveChange(event) {
    currentTab = event.detail;
    // console.log(currentTab);
  }
</script>

<div>OptiRise</div>
<Tabs on:activeChange={handleActiveChange} />

<div class="page-container">
  <div class="page-section">
    <div class="inspector-subsection">
      {#each { length: 5 } as a, b}
        <ArmorPieceInspector />
      {/each}
    </div>
  </div>

  <div class="page-section">
    <div>
      <Switch class="my-fully-colored-switch" />
    </div>
    <button on:click={addSelector}>+</button>
    <button on:click={removeSelector}>-</button>
    {#if currentTab && currentTab.icon == "access_time"}
      <div class="deco-subsection">
        <div>
          {#each { length: numSelectors } as _, i}
            <Cell class="cell">
              <DecoSelector bind:this={selectors[i]} />
            </Cell>
          {/each}
        </div>
      </div>
    {:else}<DetailedSetViewer />
    {/if}
  </div>
</div>

<style>
  .inspector-scroll-page {
  }
  .deco-selectors-container {
    display: flex;
    flex-direction: column;

    flex-wrap: wrap;
    max-height: 80vh;
    height: 80%;
    align-items: stretch;
    max-width: 100%;
    justify-content: flex-start;
    right: 0px;
    row-gap: 10px;
  }
  .page-container {
    display: flex;

    flex-direction: row;
    align-items: stretch;
    justify-items: center;
    height: 100vh;
    overflow: hidden;
    margin: 0;
  }

  .page-section {
    flex-grow: 1;
    flex-basis: 50%;

    overflow-y: auto;

    border-radius: 10px;
  }
  .page-section:nth-child(1) {
    background-color: transparent;
    display: flex;
    justify-content: center;
  }
  .page-section:nth-child(2) {
    background-color: #021526;
    justify-content: flex-start;
  }

  .deco-subsection {
    height: auto;
    margin: 5px;
    background-color: grey;
    scrollbar-width: 0px;
  }
  .inspector-subsection {
    display: flex;
    flex-direction: column;
    width: 80%;
    height: 100%;

    align-items: center;
    overflow-y: scroll;

    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 30px;

    scrollbar-width: 0px;
  }
  .layout-grid {
    height: 100%;
    width: 100%;
    box-sizing: content-box;
  }
</style>
