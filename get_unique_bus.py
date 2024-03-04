import re

seltxt = editor.getSelText()

if len(seltxt)>0:
  txtlist = sorted(seltxt.split())
  editor.deleteBack()
  
  sigs = [re.sub('(\[\d+\])?( INVERT)?( \# \wreg)?$','',x) for x in txtlist]
  editor.addText('\n'.join(sorted(list(set(sigs)))))
else:
  txt = editor.getText()
  txtlist = sorted(txt.split())
  editor.selectAll()
  editor.clear()
  
  sigs = [re.sub('(\[\d+\])?( INVERT)?( \# \wreg)?$','',x) for x in txtlist]
  editor.addText('\n'.join(sorted(list(set(sigs)))))
  #editor.addText(txtlist)


