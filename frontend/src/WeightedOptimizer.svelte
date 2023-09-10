<script>
    import AutoComplete from "simple-svelte-autocomplete";
    let selectedSkill;
    import { deco_skills } from "./all_deco_skills";
</script>

<div class="single-deco-selector">
    <AutoComplete
        hideArrow={true}
        items={deco_skills}
        bind:selectedItem={selectedSkill}
        maxItemsToShowInList="10"
    />
</div>

<style>
</style>
