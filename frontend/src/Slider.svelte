<script lang="ts">
    import Slider from "@smui/slider";

    let value = 0;
    export let min = 0;
    export let max = 10;
</script>

<Slider
    bind:value
    {min}
    {max}
    step={5}
    discrete
    tickMarks
    input$aria-label="Tick mark slider"
/>

<pre class="status">Value: {value}</pre>
