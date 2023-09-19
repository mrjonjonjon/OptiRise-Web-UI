<script>
  import Tab, { Icon, Label } from "@smui/tab";
  import { createEventDispatcher } from "svelte";

  import TabBar from "@smui/tab-bar";
  const dispatch = createEventDispatcher();

  let tabs = [
    {
      icon: "access_time",
      label: "Skill Constraints",
    },
    {
      icon: "near_me",
      label: "Weapon Constraints",
    },
    {
      icon: "favorite",
      label: "Results",
    },
  ];
  export let active = tabs[0];
  //$: dispatch("activeChange", active);
</script>

<div>
  <TabBar {tabs} let:tab bind:active>
    <Tab {tab}>
      <Icon class="material-icons">{tab.icon}</Icon>
      <Label>{tab.label}</Label>
    </Tab>
  </TabBar>
</div>
