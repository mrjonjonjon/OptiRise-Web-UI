<script>
  //extendable panel for a single full solution
  import Accordion, { Panel, Header, Content } from "@smui-extra/accordion";

  export let solution = {};
</script>

<Accordion>
  <Panel extend>
    <Header>
      <div class="part-infos-container">
        {#each ["head", "body", "arm", "waist", "leg"] as partType, i}
          <div class="part-info header">{solution[partType].partName}</div>
        {/each}
      </div></Header
    >
    <Content>
      <div class="part-infos-container">
        {#each ["head", "body", "arm", "waist", "leg"] as partType, i}
          <div class="part-info">
            {#if solution[partType].skills}
              {#each solution[partType].skills as [skillname, skillevel]}
                <div class="single-skill-info">
                  {skillname},{skillevel}
                </div>
              {/each}
            {/if}
            {#if solution[partType].decoNames.length > 0}
              {#each solution[partType].decoNames as deco}
                <div class="single-deco-info">
                  {deco}
                </div>
              {/each}
            {:else}
              <div />
            {/if}
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
  :global(.smui-accordion__header__title) {
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
