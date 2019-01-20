'''
The following script parses all xml files in a directory and counts
the length of the abstracts and the bodytext of the articles, 
as well as the number of self mentions (i.e. 1st sg and pl personal pronouns). 
Then it appends the filename, the lengths of the abstracts and the body of the articles, 
and the count of self mentions to a csv file.

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
    texts = []
    pronouns = []
    selfMent = ["we", "our", "us", "i", "me", "my"]
    title = root[0][0][0].text
    print(title)
    for bodyText in root.iter('bodyText'):
        abstract = str(bodyText.text)
        words = abstract.split()
        lengths.append(len(words))
        texts.append(words)
    for fullname in range(1):
        abst = lengths[0]
        body = sum(lengths[1:len(lengths)])
        print("Abstract length: ", abst)
        print("Body length: ", body)
        abstMent = texts[0]
        #bodyMent = texts[1:len(texts)]
        all_small = str(abstMent).lower()
        for word in selfMent[:]:
            if word in all_small:
                pronouns.append(word)
        selfMent_num = len(pronouns)  
        myFile = "../myFile_2.csv"
        csvRow = [filename, abst, body, selfMent_num]
        with open(myFile, 'a') as f:
            writer = csv.writer(f, dialect = "excel")
            writer.writerow(csvRow)
        print("Writing complete!")
        
        
       
