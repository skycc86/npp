import itertools

seltxt = editor.getSelText()

if len(seltxt)>0:
  txtlist = seltxt.split('\n')
  out = [''.join(col) for col in itertools.zip_longest(*txtlist,fillvalue=' ')]
  
  editor.deleteBack()
  editor.addText('\n'.join(out))
else:
  txt = editor.getText()
  txtlist = txt.split('\n')
  out = [''.join(col) for col in itertools.zip_longest(*txtlist,fillvalue=' ')]
  
  editor.clear()
  editor.setText('\n'.join(out))



