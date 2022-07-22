<script>
  import { onMount } from "svelte";

  let lang;

  onMount(() => {
    lang = localStorage.getItem('lang') || 'zh-Hans';
  });
  function remember_lang() {
    localStorage.setItem('lang', lang);
  }
</script>

<select name="lang" bind:value={lang} on:change={remember_lang}>
  <option value="abq">abq: 阿巴扎文</option>
  <option value="ady">ady: 阿迪格语</option>
  <option value="af">af: 南非荷兰文</option>
  <option value="anp">anp: 昂加文</option>
  <option value="ar">ar: 阿拉伯文</option>
  <option value="ar-SA">ar-SA: 沙特阿拉伯文</option>
  <option value="av">av: 阿瓦尔文</option>
  <option value="az">az: 阿塞拜疆文</option>
  <option value="be">be: 白俄罗斯文</option>
  <option value="bg">bg: 保加利亚文</option>
  <option value="bh">bh: 比哈尔文</option>
  <option value="bn">bn: 孟加拉文</option>
  <option value="bs">bs: 波斯尼亚文</option>
  <option value="cs">cs: 捷克文</option>
  <option value="cy">cy: 威尔士文</option>
  <option value="da">da: 丹麦文</option>
  <option value="dar">dar: 达尔格瓦文</option>
  <option value="de">de: 德文</option>
  <option value="en">en: 英文</option>
  <option value="es">es: 西班牙文</option>
  <option value="et">et: 爱沙尼亚文</option>
  <option value="fa">fa: 波斯文</option>
  <option value="fr">fr: 法文</option>
  <option value="ga">ga: 爱尔兰文</option>
  <option value="gom">gom: 果阿邦孔卡尼文</option>
  <option value="hi">hi: 印地文</option>
  <option value="hr">hr: 克罗地亚文</option>
  <option value="hu">hu: 匈牙利文</option>
  <option value="id">id: 印尼文</option>
  <option value="inh">inh: 印古什文</option>
  <option value="is">is: 冰岛文</option>
  <option value="it">it: 意大利文</option>
  <option value="ja">ja: 日文</option>
  <option value="ko">ko: 韩文</option>
  <option value="ku">ku: 库尔德文</option>
  <option value="lbe">lbe: 拉克文</option>
  <option value="lez">lez: 列兹金文</option>
  <option value="lt">lt: 立陶宛文</option>
  <option value="lv">lv: 拉脱维亚文</option>
  <option value="mag">mag: 摩揭陀文</option>
  <option value="mai">mai: 迈蒂利文</option>
  <option value="mi">mi: 毛利文</option>
  <option value="mn">mn: 蒙古文</option>
  <option value="mr">mr: 马拉地文</option>
  <option value="ms">ms: 马来文</option>
  <option value="mt">mt: 马耳他文</option>
  <option value="ne">ne: 尼泊尔文</option>
  <option value="new">new: 尼瓦尔文</option>
  <option value="nl">nl: 荷兰文</option>
  <option value="no">no: 挪威文</option>
  <option value="oc">oc: 奥克文</option>
  <option value="pl">pl: 波兰文</option>
  <option value="pt">pt: 葡萄牙文</option>
  <option value="ro">ro: 罗马尼亚文</option>
  <option value="ru">ru: 俄罗斯文</option>
  <option value="sck">sck: 萨德里文</option>
  <option value="sk">sk: 斯洛伐克文</option>
  <option value="sl">sl: 斯洛文尼亚文</option>
  <option value="sq">sq: 阿尔巴尼亚文</option>
  <option value="sr-Cyrl">sr-Cyrl: 塞尔维亚文（西里尔字母）</option>
  <option value="sr-Latn">sr-Latn: 塞尔维亚文（拉丁字母）</option>
  <option value="sv">sv: 瑞典文</option>
  <option value="sw">sw: 斯瓦希里文</option>
  <option value="ta">ta: 泰米尔文</option>
  <option value="tab">tab: 塔巴萨兰文</option>
  <option value="te">te: 泰卢固文</option>
  <option value="tl">tl: 他加禄文</option>
  <option value="tr">tr: 土耳其文</option>
  <option value="ug">ug: 维吾尔文</option>
  <option value="uk">uk: 乌克兰文</option>
  <option value="ur">ur: 乌尔都文</option>
  <option value="uz">uz: 乌兹别克文</option>
  <option value="vi">vi: 越南文</option>
  <option value="zh-Hans">zh-Hans: 中文（简体）</option>
  <option value="zh-Hant">zh-Hant: 中文（繁体）</option>
</select>
