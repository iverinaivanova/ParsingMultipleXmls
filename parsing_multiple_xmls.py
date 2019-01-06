'''
The following script parses all xml files in a directory and counts
the length of the abstracts and the bodytext of the articles. Then appends the filename and 
the lengths of the abstracts and the body of the articles to a csv file.

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
    for fullname in range(1):
        abst = lengths[0]
        body = sum(lengths[1:len(lengths)])
        print("Abstract length: ", abst)
        print("Body length: ", body)
        myFile = "../myFile_2.csv"
        csvRow = [filename, abst, body]
        with open(myFile, 'a') as f:
            writer = csv.writer(f, dialect = "excel")
            writer.writerow(csvRow)
            writer.writerow(['filename', 'abst', 'body'])
        print("Writing complete!")
        
        
       
