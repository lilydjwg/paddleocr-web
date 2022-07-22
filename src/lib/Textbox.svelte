<script>
  export let r;

  let l, t, w, h;
  let coords;
  let text;
  let o;

  $: {
    coords = r[0];
    text = r[1][0];
    o = r[1][1];
    l = coords[0][0] - 2;
    t = coords[0][1] - 2;
    w = coords[2][0] - coords[0][0] + 4;
    h = coords[2][1] - coords[0][1] + 4;
    console.log(coords, l, t, w, h);
  }

  function select_this() {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNode(this);
    selection.removeAllRanges();
    selection.addRange(range);
  }
</script>

<div style="left: {l}px; top: {t}px; width: {w}px; height: {h}px; opacity: {o}; font-size: {h-2}px; white-space: nowrap;" on:dblclick={select_this}>
  {#each text as ch}<span>{ch}</span>{/each}
</div>

<style>
  div {
    position: absolute;
    border: 2px solid green;
    line-height: 1em;
    color: transparent;

    /* justify-all not supported yet
    text-align: justify-all;
    text-justify: inter-character;
    */

    display: flex;
    justify-content: space-between;
  }

  div > span {
    letter-spacing: -2px;
  }
</style>
