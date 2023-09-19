<script>
  import Autocomplete from "@smui-extra/autocomplete";
  import Switch from "@smui/switch";
  import Select, { Option } from "@smui/select";
  import Chip, { Set, TrailingAction, Text } from "@smui/chips";
  import Button, { Label } from "@smui/button";
  export let getSolutions;
  let all_skills = [];
  import { onMount } from "svelte";

  onMount(async () => {
    const response = await fetch("/all_skills.json");
    all_skills = await response.json();
  });

  // Read the JSON file synchronously
  //const jsonString = fs.readFileSync("../../static/all_skills.json", "utf8");
  //console.log(data);

  let relations = [">=", ">", "=", "<", "<="];
  let valueOutlined;
  let selectedLevel = 0;
  let selectedRelation = ">=";

  export let constraints = [
    { skill: "WeaknessExploit", relation: "<", level: 2 },
    /*
    { skill: "AttackBoost", relation: "<=", level: 7 },
    { skill: "CriticalEye", relation: "<=", level: 7 },
    { skill: "Earplugs", relation: "<", level: 5 },
    { skill: "Handicraft", relation: "<", level: 5 },
    { skill: "Agitator", relation: "<=", level: 5 },
    { skill: "HealthBoost", relation: "<=", level: 3 },
    { skill: "CriticalBoost", relation: "<", level: 3 },
    { skill: "Guard", relation: "<", level: 5 },
    { skill: "EvadeWindow", relation: "<=", level: 5 },
    { skill: "Focus", relation: "<", level: 3 },
    { skill: "StaminaSurge", relation: "<", level: 3 },
    { skill: "Windproof", relation: "<", level: 5 },
    { skill: "Partbreaker", relation: "<", level: 3 },
    { skill: "QuickSheath", relation: "<", level: 3 },
    { skill: "SpeedEating", relation: "<", level: 3 },
    { skill: "DivineBlessing", relation: "<", level: 3 },
    { skill: "GuardUp", relation: "<", level: 1 },
    { skill: "FreeMeal", relation: "<", level: 3 },
    { skill: "WideRange", relation: "<", level: 5 },
    { skill: "SpeedSharpening", relation: "<", level: 3 },
    */
  ];

  function addInputChip(skill, relation, level) {
    constraints.push({ skill, relation, level });
    constraints = constraints;
  }
</script>

<div class="top-deco-selector">
  <div class="selector-row">
    <Autocomplete
      options={all_skills}
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

    <Select bind:value={selectedLevel} class="level-autocomplete">
      {#each { length: 10 } as _, i}
        <Option value={i}>{i}</Option>
      {/each}
    </Select>
  </div>
  <div class="button-and-chips">
    <Button
      class="add-button"
      on:click={addInputChip(valueOutlined, selectedRelation, selectedLevel)}
      ><Label>Add Constraint</Label></Button
    >
    <Button
      class="find-solutions-button"
      on:click={() => {
        getSolutions(constraints);
      }}><Label>Find Solutions</Label></Button
    >

    <Set chips={constraints} let:chip input>
      <Chip {chip}>
        <Text>{chip.skill} {chip.relation} {chip.level}</Text>
        <TrailingAction icon$class="material-icons">cancel</TrailingAction>
      </Chip>
    </Set>
  </div>
</div>

<style>
  .top-deco-selector :global(.deco-autocomplete) > :global(div:first-of-type) {
    height: 100%;
  }

  .top-deco-selector :global(.mdc-text-field--outlined) {
    height: 100%;
  }
  .top-deco-selector :global(.mdc-select__anchor) {
    height: 100%;
  }

  .top-deco-selector :global(.mdc-select),
  :global(.smui-autocomplete) {
    box-sizing: border-box;
    width: 100%;
    padding: auto;
  }
  .button-and-chips {
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .top-deco-selector :global(.add-button) {
    padding: 0px;
    flex-grow: 1;
    width: 90%;
    margin: 10px;
    display: inline-block;

    background-color: rgb(34, 236, 51);
    color: rgb(63, 61, 61);
    box-sizing: border-box;
    border-radius: 20px;
  }

  .top-deco-selector :global(.find-solutions-button) {
    padding: 0px;
    flex-grow: 1;
    width: 90%;
    margin: 10px;
    display: inline-block;

    background-color: #dfff45;
    color: rgb(63, 61, 61);
    box-sizing: border-box;
    border-radius: 20px;
  }
  :global(.mdc-chip) {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
  :global(.mdc-chip button) {
    position: absolute;
    right: 9px;
  }
  .selector-row :global(div > span > span) {
    text-align: center;
  }
  .selector-row :global(div > span:nth-child(2)) {
    display: none;
  }
  .selector-row :global(.level-autocomplete) {
    flex-grow: 1;
    box-sizing: border-box;
    flex-basis: 0px;
    min-width: 0px;
  }

  .selector-row :global(.deco-autocomplete) {
    flex-grow: 4;
    flex-basis: 0px;
    box-sizing: border-box;
  }

  .selector-row {
    display: flex;
    flex-direction: row;
    max-width: 100%;
    justify-content: space-evenly;
  }
  :global(.mdc-text-field) {
    width: 100%;
  }
</style>
