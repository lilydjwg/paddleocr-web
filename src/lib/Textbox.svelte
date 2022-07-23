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
  let vertical = false;

  $: {
    coords = r[0];
    vertical = (coords[3][1] - coords[0][1]) / (coords[1][0] - coords[0][0]) > 1.5;
    if(vertical) {
      fontsize = coords[1][0] - coords[0][0];
    }else{
      fontsize = coords[3][1] - coords[0][1];
    }
    console.log('fontsize', fontsize);
    text = r[1][0];
    o = 0;
    l = coords[0][0];
    t = coords[0][1];
  }

  onMount(() => {
    setTimeout(() => {
      const bound = box.getBoundingClientRect();
      w = bound.width;
      h = bound.height;
      const from = [[0, 0], [w, 0], [w, h], [0, h]];
      const to = [
        [coords[0][0] - l, coords[0][1] - t],
        [coords[1][0] - l, coords[1][1] - t],
        [coords[2][0] - l, coords[2][1] - t],
        [coords[3][0] - l, coords[3][1] - t],
      ];
      const M = getTransform(from, to);
      console.log(r, from, to, M);
      const s = matrixToString(M);
      box.style.transform = `matrix3d(${s})`;
      o = r[1][1];
    }, 100);
  });
</script>

<div style="left: {l}px; top: {t}px; opacity: {o}; font-size: {fontsize}px; " class="{vertical ? 'vertical' : 'horizontal'}" bind:this={box}>{text}</div>

<style>
  div {
    position: absolute;
    transform-origin: 0 0;
    line-height: 1em;
    white-space: nowrap;
    border: 2px solid green;
    color: transparent;
  }

  div.vertical {
    writing-mode: vertical-lr;
    font-family: "DejaVu Sans", "思源黑体 CN", 思源黑体, "Noto Sans CJK SC";
  }
</style>
