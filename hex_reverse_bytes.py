import binascii
import sys
import re

seltxt = editor.getSelText()

if len(seltxt)==0:
  seltxt = editor.getCurLine()
  seltxt = seltxt.replace(' ', '')
  res = ''.join(re.findall('\w\w', seltxt)[::-1])
  
  editor.lineDelete()
  editor.addText(res)
else:
  res = ''.join(re.findall('\w\w', seltxt)[::-1])
  # editor.deleteBack()
  editor.replaceSel(res)


