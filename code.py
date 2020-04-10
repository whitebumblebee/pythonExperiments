import json
import PyPDF2 as ppdf
import re

with open('india_helpline.json') as f:
    data = json.load(f)
# print(data)
# for i in data:
#     print(i)
l = list()
l1 = []
numbers = []
with open('coronvavirushelplinenumber.pdf','rb') as f:
    reader = ppdf.PdfFileReader(f)
    page = reader.getPage(0).extractText()
    x = page.split('\n')
    # print(x)s
    for i in x:
        j = i.strip()
        l.append(j.split()) 
for i in l:
    if re.search(r'^[0-9]',i[0]):
        l1.append(i)
# print(l1,len(l1))
for i in l1:
    try:
        x = int(i[0])

        if x and x>28:
            numbers.append(i[0])
    except:
        numbers.append(i[0])
numbers[-4] = "01912520982"
numbers.insert(12,"104")
# print("number of numbers is {}".format(len(numbers)))
newNumbers=[]
for number in numbers:
    if '-' in number:
        numberList = number.split('-')
        s = ''.join(numberList)
        if s[0]=='0':
            s1 = "+91"+s[1:]
        newNumbers.append(s1)
    else:
        newNumbers.append(number)
print(newNumbers)
print(len(newNumbers))

for i,j in zip(data,range(len(newNumbers))):
    print(i['number'],newNumbers[j])
    if re.search(i['number'][1:],newNumbers[j]):
        print("{} verified".format(i["state"]))
