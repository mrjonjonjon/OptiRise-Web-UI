<script>
  import DecoSelector from "./DecoSelector.svelte";
  import Switch from "@smui/switch";
  import Tabs from "./Tabs.svelte";
  import LayoutGrid, { Cell } from "@smui/layout-grid";
  import { scale } from "svelte/transition";
  import ArmorPieceInspector from "./ArmorPieceInspector.svelte";
  import DetailedSetViewer from "./DetailedSetViewer.svelte";
  import CircularProgress from "@smui/circular-progress";

  import Autocomplete from "@smui-extra/autocomplete";

  import Select, { Option } from "@smui/select";
  import Chip, { Set, TrailingAction, Text } from "@smui/chips";
  import Button, { Label } from "@smui/button";
  //#region variables
  let solutionsLoading = false;
  let partIconUrls = [
    "/helm.png",
    "body.png",
    "/arm.png",
    "waist.png",
    "leg.png",
  ];

  let currentParts = [
    {
      partName: "Lambent Casque",
      decoNames: [
        "Weakness Exploit Lv2",
        "Critical Eye Lv2",
        "Dragon Resistance Lv2",
      ],
    },
    {
      partName: "Drakehide Mail",
      decoNames: ["Guard Lv1", "Agitator Lv2", "Stamina Surge Lv2"],
    },
    {
      partName: "Wyrmclaw Gauntlets",
      decoNames: ["Attack Boost Lv1", "Agitator Lv2", "Evade Window Lv1"],
    },
    {
      partName: "Serpentscale Coil",
      decoNames: ["Focus Lv2", "Agitator Lv1", "Defense Boost Lv1"],
    },
    {
      partName: "Skystride Greaves",
      decoNames: ["Weakness Exploit Lv1", "Jump Master Lv1", "Windproof Lv2"],
    },
  ];

  let currentTab = {
    icon: "access_time",
    label: "Skill Constraints",
  };

  let solutions = [];

  let constraints = [{ skill: "WeaknessExploit", relation: "<", level: 2 }];
  //#endregion
  $: console.log(currentTab);
  //#region function
  function handleActiveChange(event) {
    currentTab = event.detail;
    // console.log(currentTab);
  }

  function getSolutions(constraints) {
    /*
    currentTab = {
      icon: "near_me",
      label: "Weapon Constraints",
    };*/
    solutionsLoading = true;
    // Define the URL for your request
    const url = "http://127.0.0.1:5000/send_data";

    // Use the Fetch API to send a POST request with constraints as the body
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(constraints), // Convert the constraints object to a JSON string
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        return response.json(); // Parse the response to JSON
      })
      .then((data) => {
        solutions = data;
        solutionsLoading = false;
        console.log(solutions);
      })
      .catch((error) => {
        console.log(
          "There was a problem with the fetch operation:",
          error.message
        );
      });
  }
  //#endregion
</script>

<div class="app-root">
  <div>OptiRise</div>
  <Tabs on:activeChange={handleActiveChange} bind:active={currentTab} />

  <div class="page-container">
    <div class="page-section">
      <div class="inspector-subsection">
        <div class="inspector-subsection-label">Current Build</div>
        {#each { length: 5 } as _, i}
          <ArmorPieceInspector
            part={currentParts[i]}
            partIconUrl={partIconUrls[i]}
          />
        {/each}
      </div>
    </div>

    <div class="page-section">
      {#if currentTab && currentTab.icon == "access_time"}
        <div class="deco-subsection">
          <div>
            <Cell class="cell">
              <DecoSelector bind:constraints {getSolutions} />
            </Cell>
          </div>
        </div>
      {:else if !solutionsLoading}<div class="detailed-viewer-subsection">
          <DetailedSetViewer {solutions} />
        </div>{:else}
        <CircularProgress class="circular-progress" indeterminate />
      {/if}
    </div>
  </div>
</div>

<style>
  .detailed-viewer-subsection {
    height: 100%;
    background-color: black;
  }
  .app-root :global(.circular-progress) {
    width: 100%;
    height: 100%;
  }
  .app-root {
    max-height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .inspector-subsection-label {
    flex-shrink: 0;
    height: 20px;
    background-color: #fff500;
    position: sticky;
    top: 0;
    width: 100%;
    z-index: 100;
    text-align: center;
    color: black;
  }
  .deco-selectors-container {
    display: flex;
    flex-direction: column;

    flex-wrap: wrap;
    max-height: 80vh;
    height: 80%;
    align-items: stretch;
    max-width: 100%;
    justify-content: flex-start;
    right: 0px;
    row-gap: 10px;
  }
  .page-container {
    display: flex;

    flex-direction: row;
    align-items: stretch;
    justify-items: center;

    overflow: hidden;
    margin: 0;
    gap: 5px;
  }

  .page-section {
    flex-grow: 1;
    flex-basis: 50%;

    overflow-y: auto;
    scrollbar-width: none;

    border-radius: 10px;
  }

  .page-section::-webkit-scrollbar {
    display: none;
  }
  .page-section:nth-child(1) {
    background-color: transparent;
    display: flex;
    justify-content: center;
    background-image: url("bg.jpeg");
  }
  .page-section:nth-child(2) {
    background-color: #021526;
    justify-content: flex-start;
    background-image: url("bg2.jpeg");
  }

  .deco-subsection {
    height: auto;
    margin: 5px;
    background-color: grey;
    scrollbar-width: 0px;
  }
  .inspector-subsection {
    display: flex;
    flex-direction: column;
    width: 80%;
    height: 100%;

    align-items: center;

    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;

    scrollbar-width: 0px;
  }
  .layout-grid {
    height: 100%;
    width: 100%;
    box-sizing: content-box;
  }
</style>
