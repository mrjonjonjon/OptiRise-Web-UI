<script>
  import Autocomplete from "@smui-extra/autocomplete";
  import Switch from "@smui/switch";
  import Select, { Option } from "@smui/select";
  import Chip, { Set, TrailingAction, Text } from "@smui/chips";
  import Button, { Label } from "@smui/button";

  let fruits = ["WeaknessExploit", "Orange", "Banana", "Mango"];
  let levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  let relations = [">=", ">", "=", "<", "<="];
  let valueOutlined;
  let selectedLevel;
  let selectedRelation = ">=";

  let input = [1, 2, 3, 4];

  function addInputChip() {
    if (input.length) {
      input.push(input[input.length - 1] + 1);
      input = input;
    } else {
      input.push(1);
      input = input;
    }
  }
</script>

<div class="single-deco-selector-container">
  <Autocomplete
    options={fruits}
    textfield$variant="outlined"
    bind:value={valueOutlined}
    label="Skill"
    class="deco-autocomplete"
  />
  <Select bind:value={selectedRelation} class="level-autocomplete">
    {#each relations as rel}
      <Option value={rel}>{rel}</Option>
    {/each}
  </Select>
  <Autocomplete
    options={levels}
    textfield$variant="outlined"
    bind:value={selectedLevel}
    label="Level"
    class="level-autocomplete"
  />
</div>

<style>
  .single-deco-selector-container :global(div > span > span) {
    text-align: center;
  }
  .single-deco-selector-container :global(div > span:nth-child(2)) {
    display: none;
  }
  .single-deco-selector-container :global(.level-autocomplete) {
    flex-grow: 1;
    box-sizing: border-box;
    flex-basis: 0px;
    min-width: 0px;
  }

  .single-deco-selector-container :global(.deco-autocomplete) {
    flex-grow: 4;
    flex-basis: 0px;
    box-sizing: border-box;
  }

  .single-deco-selector-container {
    display: flex;
    flex-direction: row;
    max-width: 100%;
    justify-content: space-evenly;
  }
  :global(.mdc-text-field) {
    width: 100%;
  }
</style>
