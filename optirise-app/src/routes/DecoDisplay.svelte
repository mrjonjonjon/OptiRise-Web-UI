<script>
  import Tab, { Icon, Label } from "@smui/tab";
  import { createEventDispatcher } from "svelte";
  import List, { Item, Separator, Text } from "@smui/list";

  let clicked = "nothing yet";
  import TabBar from "@smui/tab-bar";
</script>

<List class="inspector-container">
  <Item on:SMUI:action={() => (clicked = "Delete")}><Text>Delete</Text></Item>
</List>

<!--
  <div class="inner-inspector" />
  
  -->

<style>
  .inspector-container {
    height: 50%;
    background-color: rgb(111, 116, 121);
    border-radius: 4px;
    margin: 1px;
    margin-right: 3px;
  }
</style>
