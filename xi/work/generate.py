# -*- coding: utf-8 -*-
import pathlib, json

CSS = '''
/* placeholder */
'''

def build():
    html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Test</title></head><body><h1>Test</h1></body></html>'
    pathlib.Path(r'C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html').write_text(html, encoding='utf-8')
    print('OK')

if __name__ == '__main__':
    build()
