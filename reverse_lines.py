
seltxt = editor.getSelText()

if len(seltxt)>0:
  txtlist = seltxt.split('\n')
  editor.deleteBack()
  editor.addText('\n'.join(txtlist[::-1]))
else:
  txt = editor.getText()
  txtlist = txt.split('\n')
  editor.clear()
  editor.setText('\n'.join(txtlist[::-1]))


