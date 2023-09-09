<script>
    import Switch from "svelte-switch";

    let checkedValue = true;

    function handleChange(e) {
        const { checked } = e.detail;
        checkedValue = checked;
    }
</script>

<div class="toggle-container">
    <span style="color:#9acd32">ALL SOLUTIONS</span>
    <Switch
        on:change={handleChange}
        checked={checkedValue}
        offColor={"#9acd32"}
        onColor={"#d52cab"}
        ><div slot="checkedIcon" />
        <div slot="unCheckedIcon" />
    </Switch>

    <span style="color:#d52cab">GLOBAL SOLUTION</span>
</div>

<style>
    .toggle-container {
        display: flex;
        align-items: center;
        justify-content: center;

        font-weight: bold;
        font-size: x-small;
        margin: 20px;
        width: fit-content;
    }
    .toggle-container span {
        display: inline-block;
        padding: 0px;
        word-wrap: break-word;
        width: 30%;
    }
</style>
