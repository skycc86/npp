
seltxt = editor.getSelText()

if len(seltxt)>0:
  txtlist = sorted(seltxt.split('\n'))
  editor.deleteBack()
  editor.addText('\n'.join(txtlist))
else:
  txt = editor.getText()
  txtlist = sorted(txt.split('\n'))
  editor.clear()
  editor.setText('\n'.join(txtlist))


