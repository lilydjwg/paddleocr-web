#!/usr/bin/python3

import json
import logging
import os
import asyncio
import tempfile
import subprocess
import time
from functools import partial

from aiohttp import web

logger = logging.getLogger(__name__)

async def ocr(sem, request):
  async with sem:
    return await _ocr(request)

async def _ocr(request):
  multipart = await request.multipart()

  with tempfile.TemporaryDirectory() as tmpdir:
    while True:
      part = await multipart.next()
      if not part:
        break

      if part.name == 'file':
        try:
          _, ext = part.filename.split('.')
        except ValueError:
          ext = 'png'
        tmpfile = os.path.join(tmpdir, f'image.{ext}')
        logger.info('image %s uploaded to %s', part.filename, tmpfile)
        with open(tmpfile, 'wb') as f:
          while True:
            data = await part.read_chunk()
            if not data:
              break
            f.write(part.decode(data))

      elif part.name == 'lang':
        lang = await part.text()

    st = time.time()
    res = await ocr_file(tmpfile, lang)
    logger.info('OCR time: %.3fs', time.time() - st)

  return web.json_response(
    {'result': res},
    headers = {
      # 'Access-Control-Allow-Origin': '*',
    },
  )

async def ocr_file(tmpfile, lang):
  cmd = f'''run_ocr --lang={lang} {tmpfile}'''
  p = await asyncio.create_subprocess_shell(cmd, stdout=subprocess.PIPE)
  out, _err = await p.communicate()
  return json.loads(out)

def setup_app(app, sem):
  app.router.add_post('/api', partial(ocr, sem))

def main():
  import argparse

  from nicelogger import enable_pretty_logging

  parser = argparse.ArgumentParser(
    description = 'HTTP services for PaddleOCR',
  )
  parser.add_argument('--port', default=5174, type=int,
                      help='port to listen on')
  parser.add_argument('--ip', default='127.0.0.1',
                      help='address to listen on')
  parser.add_argument('--loglevel', default='info',
                      choices=['debug', 'info', 'warn', 'error'],
                      help='log level')
  parser.add_argument('-j', type=int, default=os.cpu_count(),
                      help='max parallel jobs')
  args = parser.parse_args()

  enable_pretty_logging(args.loglevel.upper())

  app = web.Application()
  setup_app(app, asyncio.Semaphore(args.j))

  web.run_app(app, host=args.ip, port=args.port)

if __name__ == '__main__':
  main()
