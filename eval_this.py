import itertools
import sys,os,time,re

seltxt = editor.getSelText()

if len(seltxt)==0:
  seltxt = editor.getCurLine()
  res = eval(seltxt)
  editor.lineDelete()
  editor.addText(res)
else:
  res = eval(seltxt)
  # editor.deleteBack()
  editor.replaceSel(res)


