<script>
    import AutoComplete from "simple-svelte-autocomplete";
    import { deco_skills } from "./all_deco_skills";
    const skills = deco_skills;
    const levels = [1, 2, 3];
    let selectedLevel;
    let selectedDeco;
    function getData() {
        if (selectedDeco && selectedLevel) {
            return { [`${selectedDeco}`]: selectedLevel };
        } else {
            return {};
        }
    }
    export { getData };
</script>

<div class="single-deco-selector">
    <AutoComplete
        hideArrow={true}
        items={skills}
        bind:selectedItem={selectedDeco}
        maxItemsToShowInList="10"
    />
    <AutoComplete
        className={"level-input"}
        hideArrow={true}
        items={levels}
        bind:selectedItem={selectedLevel}
        maxItemsToShowInList="10"
    />
</div>

<style>
    .single-deco-selector {
        display: flex;
        flex-direction: row;
        margin: 2px;
        align-items: stretch;
        justify-content: center;
        flex-shrink: 1;
    }
    .single-deco-selector :global(.autocomplete) {
        min-width: 20%;
    }

    .single-deco-selector :global(.level-input) {
        width: 50px;
        min-width: 50px;
    }

    .single-deco-selector :global(.input) {
        text-align: center;
    }
    .single-deco-selector :global(.input-container) {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .single-deco-selector :global(.autocomplete-list-item) {
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
    }
    .single-deco-selector :global(.autocomplete-list) {
        display: flex;
        flex-direction: column;
    }
</style>
