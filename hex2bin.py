import binascii
import sys
sys.path.append(r'C:\fatd5\lib\sbft')
import util
import re

outfile=infile = notepad.getCurrentFilename()
# hexdata = open(infile).read().splitlines()

vecx=False
if infile.endswith('vecx'):
  outfile = infile[:-1]
  vecx=True


if not infile.endswith(('.vec','.vecx','.lz4','.lz4rf')):
  notepad.messageBox("only support vec/vecx/lz4/lz4rf !!!")
else:
  txt = editor.getText()
  hexdata = txt.split('\n')
  hexdata = [x.replace(' ', '').rstrip() for x in hexdata]


  dat = []
  for i in hexdata:
    dat.append(binascii.unhexlify(i))
    

    
  out = open(outfile, 'wb')
  for i in hexdata:
    data = binascii.unhexlify(i)
    out.write(data)
  out.close()

  if infile.endswith('vecx'):
    outfile = util.zip_7z(outfile, outfile+'x', 1)

  notepad.reloadCurrentDocument()
    
  # editor.clear()
  # editor.setText(''.join(dat))
  # editor.gotoPos(0)


