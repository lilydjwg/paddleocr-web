#!/usr/bin/env python3

import argparse
import sys
import json

from paddleocr import PaddleOCR

LANGUAGES = {
  'abq': ('阿巴扎文', 'abq'),
  'ady': ('阿迪格语', 'ady'),
  'af': ('南非荷兰文', 'af'),
  'anp': ('昂加文', 'ang'),
  'ar': ('阿拉伯文', 'ar'),
  'ar-SA': ('沙特阿拉伯文', 'sa'),
  'av': ('阿瓦尔文', 'ava'),
  'az': ('阿塞拜疆文', 'az'),
  'be': ('白俄罗斯文', 'be'),
  'bg': ('保加利亚文', 'bg'),
  'bh': ('比哈尔文', 'bh'),
  'bn': ('孟加拉文', 'bho'),
  'bs': ('波斯尼亚文', 'bs'),
  'cs': ('捷克文', 'cs'),
  'cy': ('威尔士文', 'cy'),
  'da': ('丹麦文', 'da'),
  'dar': ('达尔格瓦文', 'dar'),
  'de': ('德文', 'german'),
  'en': ('英文', 'en'),
  'es': ('西班牙文', 'es'),
  'et': ('爱沙尼亚文', 'et'),
  'fa': ('波斯文', 'fa'),
  'fr': ('法文', 'fr'),
  'ga': ('爱尔兰文', 'ga'),
  'gom': ('果阿邦孔卡尼文', 'gom'),
  'hi': ('印地文', 'hi'),
  'hr': ('克罗地亚文', 'hr'),
  'hu': ('匈牙利文', 'hu'),
  'id': ('印尼文', 'id'),
  'inh': ('印古什文', 'inh'),
  'is': ('冰岛文', 'is'),
  'it': ('意大利文', 'it'),
  'ja': ('日文', 'japan'),
  'ko': ('韩文', 'korean'),
  'ku': ('库尔德文', 'ku'),
  'lbe': ('拉克文', 'lbe'),
  'lez': ('列兹金文', 'lez'),
  'lt': ('立陶宛文', 'lt'),
  'lv': ('拉脱维亚文', 'lv'),
  'mag': ('摩揭陀文', 'mah'),
  'mai': ('迈蒂利文', 'mai'),
  'mi': ('毛利文', 'mi'),
  'mn': ('蒙古文', 'mn'),
  'mr': ('马拉地文', 'mr'),
  'ms': ('马来文', 'ms'),
  'mt': ('马耳他文', 'mt'),
  'ne': ('尼泊尔文', 'ne'),
  'new': ('尼瓦尔文', 'new'),
  'nl': ('荷兰文', 'nl'),
  'no': ('挪威文', 'no'),
  'oc': ('奥克文', 'oc'),
  'pl': ('波兰文', 'pl'),
  'pt': ('葡萄牙文', 'pt'),
  'ro': ('罗马尼亚文', 'ro'),
  'ru': ('俄罗斯文', 'ru'),
  'sck': ('萨德里文', 'sck'),
  'sk': ('斯洛伐克文', 'sk'),
  'sl': ('斯洛文尼亚文', 'sl'),
  'sq': ('阿尔巴尼亚文', 'sq'),
  'sr-Cyrl': ('塞尔维亚文（西里尔字母）', 'rs_cyrillic'),
  'sr-Latn': ('塞尔维亚文（拉丁字母）', 'rs_latin'),
  'sv': ('瑞典文', 'sv'),
  'sw': ('斯瓦希里文', 'sw'),
  'ta': ('泰米尔文', 'ta'),
  'tab': ('塔巴萨兰文', 'tab'),
  'te': ('泰卢固文', 'te'),
  'tl': ('他加禄文', 'tl'),
  'tr': ('土耳其文', 'tr'),
  'ug': ('维吾尔文', 'ug'),
  'uk': ('乌克兰文', 'uk'),
  'ur': ('乌尔都文', 'ur'),
  'uz': ('乌兹别克文', 'uz'),
  'vi': ('越南文', 'vi'),
  'zh-Hans': ('中文（简体）', 'ch'),
  'zh-Hant': ('中文（繁体）', 'chinese_cht'),
}

def main(img, lang):
  # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
  # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
  ocr = PaddleOCR(use_angle_cls=True, lang=LANGUAGES[lang][1], show_log=False)
  result = ocr.ocr(img)
  json.dump(result, sys.stdout)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='PaddleOCR')
  parser.add_argument('--lang', default='zh-Hans',
                      help='language to recognize')
  parser.add_argument('image_file', nargs=1,
                      help='file to OCR')
  args = parser.parse_args()
  main(args.image_file[0], args.lang)
