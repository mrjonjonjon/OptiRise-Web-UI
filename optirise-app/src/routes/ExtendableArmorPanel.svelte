<script>
  import Accordion, { Panel, Header, Content } from "@smui-extra/accordion";
  const rows = [
    /** data (example below) */
  ];
  const columns = [
    /** columns config (example below) */
  ];

  export let numSkills = [1, 2, 3, 4, 5];
  export let numDecos = [2, 5, 1, 2, 3];
  export let partNames = [
    "Pride Helm",
    "Buff Chest",
    "Onmyou Tekkou",
    "Pride Waist",
    "Ceanataur X",
  ];
</script>

<Accordion>
  <Panel extend>
    <Header>
      <div class="part-infos-container">
        {#each { length: 5 } as a, i}
          <div class="part-info header">{partNames[i]}</div>
        {/each}
      </div></Header
    >
    <Content>
      <div class="part-infos-container">
        {#each { length: 5 } as a, i}
          <div class="part-info">
            {#each { length: numSkills[i] } as a, b}<div
                class="single-skill-info"
              >
                Agitator Lv2
              </div>{/each}
            {#each { length: numDecos[i] } as a, b}<div
                class="single-deco-info"
              >
                Agitator Lv2
              </div>{/each}
          </div>
        {/each}
      </div>
    </Content>
  </Panel>
</Accordion>

<style>
  :global(.part-info.header) {
    font-size: x-small;
  }
  :global(.smui-paper__content) {
    padding: 0px !important;
    text-align: center;
  }
  :global(.single-deco-info) {
    background-color: rgb(35, 121, 197);
    margin: 2px;
    border-radius: 8px;
  }

  :global(.single-skill-info) {
    background-color: rgb(29, 52, 155);
    margin: 2px;
    border-radius: 8px;
  }
  :global(.part-infos-container) {
    display: flex;
    flex-direction: row;
    gap: 5px;
  }
  :global(.part-info) {
    font-size: x-small;
    height: 100%;
    background-color: rgba(100, 92, 216, 0);
    border-radius: 9px;
    flex-basis: 0px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
</style>
