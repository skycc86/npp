import os
import subprocess

path = editor.getSelText()
if len(path)==0:
  path = editor.getCurLine()


z7 = r'C:\FATD5\lib\7za.exe'

path = path.strip('"').strip("'")

if os.path.isfile(path):  
  # notepad.open(path)
  if path.endswith(('.cmpx', '.vecx')):
    cmd = z7 + ' e -y "' + path + '" -o"{}"'.format(os.path.dirname(path))    
    subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    notepad.open(path[:-1])
  else:
    notepad.open(path)
elif os.path.isdir(path):
  os.startfile(os.path.realpath(path))
else:
  curfile = notepad.getCurrentFilename()
  if curfile.endswith(('.cmpx', '.vecx')):
    cmd = z7 + ' e -y "' + curfile + '" -o"{}"'.format(os.path.dirname(curfile))
    subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
    notepad.close()
    notepad.open(curfile[:-1])
  else:
    notepad.messageBox("invalid path {} !!!".format(path))
