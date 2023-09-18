<script>
  import Tab, { Icon, Label } from "@smui/tab";
  import { createEventDispatcher } from "svelte";
  import DecoDisplay from "./DecoDisplay.svelte";
  import TabBar from "@smui/tab-bar";
  import List, { Item, Separator, Text } from "@smui/list";
  import Accordion, { Panel, Header, Content } from "@smui-extra/accordion";
  import Button from "@smui/button";

  let clicked = "nothing yet";

  export let part = {
    partName: "Buff Chest",
    decoNames: [
      "Weakness Exploit Lv2",
      "Agitator Lv3",
      "Dragon Resistance Lv4",
    ],
  };
</script>

<div class="inspector-container">
  <Button
    style="background-color:#9e2b2d00;height:6vh"
    color="secondary"
    on:click={() => clicked++}
    variant="raised"
  >
    <Label>{part.partName}</Label>
  </Button>
  <List class="deco-displays-list">
    {#each { length: 3 } as a, i}
      <Item on:SMUI:action={() => (clicked = "Cut")} class="list-item"
        ><Button color="secondary" on:click={() => clicked++} variant="raised">
          <Label>{part.decoNames[i]}</Label>
        </Button></Item
      >
    {/each}
  </List>
</div>

<!--
<div class="inner-inspector" />

-->

<style lang="scss">
  :global(.mdc-deprecated-list-item__ripple) {
    display: none;
  }
  .inspector-container :global(.mdc-button) {
    padding: 0px;
    height: 80%;
    width: 100%;
  }
  :global(.list-item) {
    height: 4vh;
  }

  :global(.deco-displays-list) {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    padding: 0px;

    flex-grow: 1;
    font-size: x-small;
  }
  .inspector-container {
    margin: 0px;
    align-items: stretch;
    width: 70%;
    height: fit-content;
    display: flex;
    flex-direction: column;
    border: solid black 2px;

    background-color: rgb(10, 55, 94);
    background: linear-gradient(
      to bottom right,
      rgb(10, 55, 94),
      rgb(65, 14, 124)
    ); /* Gradient from top-left (red) to bottom-right (yellow) */

    box-sizing: border-box;
    border-radius: 7px;

    row-gap: 3px;
  }
</style>
