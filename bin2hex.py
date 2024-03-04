import binascii
import sys
sys.path.append(r'C:\fatd5\lib\sbft')
import util
import re


# bytelen = editor.getLength()
# dat = []
# for i in range(bytelen // 64):
#   vecline=''  
#   for x in range(64):
#     tmp = editor.getCharAt(x+(i*64))
#     if tmp>=0:
#       vecline += " {:02x}".format(tmp)
#     else:
#       vecline += " {:02x}".format(tmp+256)
#   dat.append(vecline)



infile = notepad.getCurrentFilename()
if infile.endswith('vecx'):
  infile = util.unzip_7z(infile)

if not infile.endswith(('.vec', '.lz4','.lz4rf')):
  notepad.messageBox("only support vec/vecx/lz4/lz4rf !!!")
else:
  bindata = open(infile, 'rb').read()
  bytelen = len(bindata)



  dat=[]
  for i in range(bytelen// 64):
    line = bindata[i * 64:i * 64 + 64]
    data = binascii.hexlify(line).decode()
    dat.append(' '.join(re.findall('\w\w', data)))

    
  editor.clear()
  editor.setText('\n'.join(dat))
  editor.gotoPos(0)
