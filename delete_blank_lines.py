



seltxt = editor.getSelText()

if len(seltxt)>0:
  txtlist = seltxt.split('\n')
  
  pos = editor.getCurrentPos()
  anchor = editor.getAnchor()
  startline = editor.lineFromPosition(min(pos, anchor))
  endline = startline+len(txtlist)
  
  for x in range(startline, startline+len(txtlist)):
    line = editor.getLine(x)
    if line.strip() == "":
      editor.deleteLine(x)
      
  def testLine(contents,linenumber, totallines):
    if linenumber>=startline and linenumber<endline and contents.strip() == "":
      editor.deleteLine(linenumber)
      return 0
  
  # editor.deleteBack()
  # editor.addText('\n'.join(txtlist))
else:
  def testLine(contents,linenumber, totallines):
    if contents.strip() == "":
      editor.deleteLine(linenumber)
      return 0


editor.forEachLine(testLine)
  
  
