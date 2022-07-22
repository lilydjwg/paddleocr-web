<script lang="ts">
  import Lang from "./lib/Lang.svelte";
  import Textbox from "./lib/Textbox.svelte";

  let abort = new AbortController();
  let form;
  let file;
  let image;

  let btn_msg = '上传识别';
  let loading;
  let error = '';
  let results = [];

  $: {
    loading = btn_msg !== '上传识别';
    if (loading) {
      document.title = '上传识别中... - PaddleOCR';
    } else {
      document.title = 'PaddleOCR';
    }
  }

  function update_preview() {
    error = '';
    if(file.files.length > 0) {
      const file_obj = file.files[0];
      const reader = new FileReader();
      reader.addEventListener("load", function(){
        image.src = reader.result;
        results = [];
      })
      reader.readAsDataURL(file_obj);
    }
  }

  async function upload_image() {
    abort.abort();
    abort = new AbortController();
    btn_msg = '上传中...';
    try {
      if(file.files.length === 0) {
        error = '未选择要识别的图片';
        return;
      } else {
        error = '';
      }
      const res = await fetch(form.action, {
        signal: abort.signal,
        method: form.method,
        body: new FormData(form),
      });
      const r = await res.json();
      if (abort.signal.aborted) {
        return;
      }
      results = r.result;
    } catch (e) {
      error = e;
    } finally {
      btn_msg = '上传识别';
    }
  }
</script>

<main>
  <div>
    <form action="/api" method="POST" bind:this={form} on:submit|preventDefault={upload_image}>
      <Lang />
      <input type="file" name="file" accept="image/*" bind:this={file} on:change={update_preview}/>
      <button type="submit" disabled={loading}>{btn_msg}</button>
    </form>
    <span class="error">{error}</span>
  </div>
  <div id="result">
    <img bind:this={image} alt=""/>
    <div>
      {#each results as r}
        <Textbox {r} />
      {/each}
    </div>
  </div>
  <!-- select to this end, not wrap to start -->
  <div>&nbsp;</div>
</main>

<style>
  .error {
    color: red;
  }

  #result {
    position: relative;
  }

  #result > img {
    user-select: none;
    pointer-events: none;
  }

  #result > * {
    position: absolute;
    top: 0;
    left: 0;
  }
</style>
