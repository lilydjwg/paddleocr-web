<script>
  import { onMount } from "svelte";
  import { getTransform, matrixToString } from "../matrix.js";

  export let r;

  let l, t, w, h;
  let coords;
  let text;
  let o;
  let box;
  let fontsize;

  $: fontsize = r[0][3][1] - r[0][0][1];

  onMount(() => {
    coords = r[0];
    text = r[1][0];
    o = 0;
    l = coords[0][0];
    t = coords[0][1];

    setTimeout(() => {
      const bound = box.getBoundingClientRect();
      w = bound.width;
      h = bound.height;
      const M = getTransform(
        [[0, 0], [0, h], [w, 0], [w, h]],
        [
          [coords[0][0] - l, coords[0][1] - t],
          [coords[3][0] - l, coords[3][1] - t],
          [coords[1][0] - l, coords[1][1] - t],
          [coords[2][0] - l, coords[2][1] - t],
        ],
      );
      M[0][1] = -M[0][1];
      const s = matrixToString(M);
      box.style.transform = `matrix3d(${s})`;
      o = r[1][1];
    }, 100);
  });
</script>

<div style="left: {l}px; top: {t}px; opacity: {o}; font-size: {fontsize}px; white-space: nowrap;" bind:this={box}>{text}</div>

<style>
  div {
    position: absolute;
    transform-origin: 0 0;
    line-height: 1em;
    border: 2px solid green;
    color: transparent;
  }
</style>
