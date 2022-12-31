#!/usr/bin/python3

# Text2Markdown
# Version 1.1
import os

sdirectory = r"/home/administrator/converter/files/"
tdirectory = r"/home/administrator/converter/converted/"


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

for filename in os.listdir(sdirectory):
    if filename.endswith(".txt"):

         #Create File-Handle
         handle = os.path.join(sdirectory, filename)
         mdfile = filename.replace(".txt", ".md")
         orgtitle = filename.replace(".txt", "")
         mdfile = mdfile.replace(" ", "")

         #Convert File
         os.system('iconv -f ISO-8859-1 -t UTF-8//TRANSLIT \''+handle+'\' -o '+tdirectory + '\''  + mdfile+'\'')

         #Add File-Header
         line_prepender(tdirectory+mdfile,"---")
         line_prepender(tdirectory+mdfile,"title: "+orgtitle)
         line_prepender(tdirectory+mdfile,"---")

	 #Done
         print("Done converting: "+orgtitle)

    else:
        continue

