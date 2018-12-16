'''
The following script parses all xml files in a directory and counts
the length of the abstracts and the bodytext.

'''
import os
import xml.etree.ElementTree as ET
path = 'C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/A00'
print(path)
for filename in os.listdir(path):
    if not filename.endswith('.xml'):continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    '''for elem in root.iter():
        print(elem.tag, elem.attrib)'''
    lengths = []
    title = root[0][0][0].text
    print(title)
    for bodyText in root.iter('bodyText'):
        abstract = str(bodyText.text)
        words = abstract.split()
        lengths.append(len(words))
        print(lengths)
        print("Abstract length: ", lengths[0])
        print("Body length: ", sum(lengths[1:len(lengths)]))
       
