# import all the modules needed
# parse the xml file to the dom file
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')

# build up a new dictionary
dict = {}
for term in terms:
    id = term.getElementsByTagName('id')
    dict[id[0].firstChild.data] = []
for term in terms:
    id = term.getElementsByTagName('id')
    is_as = term.getElementsByTagName('is_a')
    for is_a in is_as:
        dict[is_a.firstChild.data].append(id[0].firstChild.data)

# Find out all the keywords named "DNA"
def count(species):
    for term in terms:
        if species in term.getElementsByTagName('defstr')[0].firstChild.data:
            ids = term.getElementsByTagName('id')[0].firstChild.data
            if dict[ids]:
                counter = dict[ids]
                n = count1(counter)
                s = str(n)
    return s

# Calculate the number of childnodes in DNA
def count1(counter):
    for i in range(len(counter)):
        if counter[i] not in store_childNodes1:
            store_childNodes1.append(counter[i])
            count1(dict[counter[i]])
    return len(store_childNodes1)

store_childNodes1 = []

DNA = count('DNA')
print('ChildNodes number of DNA: ' + DNA)

# Find out all the keywords named "RNA"
def count(species):
    for term in terms:
        if species in term.getElementsByTagName('defstr')[0].firstChild.data:
            ids = term.getElementsByTagName('id')[0].firstChild.data
            if dict[ids]:
                counter = dict[ids]
                n = count2(counter)
                s = str(n)
    return s

# Figure out the specific number of childnodes in RNA
def count2(counter):
    for i in range(len(counter)):
        if counter[i] not in store_childNodes2:
            store_childNodes2.append(counter[i])
            count2(dict[counter[i]])
    return len(store_childNodes2)

store_childNodes2=[]
RNA = count('RNA')
print('ChildNodes number of RNA: ' + RNA)

# In protein part, there were two kinds of situations
# This function is used to find out all the id named " Protein"
def count(species):
    for term in terms:
        if species in term.getElementsByTagName('defstr')[0].firstChild.data:
            ids = term.getElementsByTagName('id')[0].firstChild.data
            if dict[ids]:
                counter = dict[ids]
                n = count3(counter)
                s = str(n)
    return s

# calculate the corresponding number of childnodes
def count3(counter):
    for i in range(len(counter)):
        if counter[i] not in store_childNodes3:
            store_childNodes3.append(counter[i])
            count3(dict[counter[i]])
    return len(store_childNodes3)

store_childNodes3 = []
Protein = count('Protein')

# find the keywords of "protein"
def count(species):
    for term in terms:
        if species in term.getElementsByTagName('defstr')[0].firstChild.data:
            ids = term.getElementsByTagName('id')[0].firstChild.data
            if dict[ids]:
                counter = dict[ids]
                n = count5(counter)
                s = str(n)
    return s

# This function is used to find out all the id "protein"
def count5(counter):
    for i in range(len(counter)):
        if counter[i] not in store_childNodes3:
            store_childNodes3.append(counter[i])
            count5(dict[counter[i]])
    return len(store_childNodes3)

store_childNodes5 = []
protein = count('protein')

# Because id proving protein can be either "protein" or "Protein", so all we did before is to find out these two ids and add the corresponding number of chilnodes together
total_protein = int(protein)+int(Protein)
print('ChildNodes number of protein: ' + str(total_protein))

# find the keywords of glycoprotein
def count(species):
    for term in terms:
        if species in term.getElementsByTagName('defstr')[0].firstChild.data:
            ids = term.getElementsByTagName('id')[0].firstChild.data
            if dict[ids]:
                counter = dict[ids]
                n = count4(counter)
    print('ChildNodes number of ' + species + ': ' + str(n))
    return n

# a function that is used to calculate all the childnodes of glycoprotein
def count4(counter):
    for i in range(len(counter)):
        if counter[i] not in store_childNodes4:
            store_childNodes4.append(counter[i])
            count4(dict[counter[i]])
    return len(store_childNodes4)

store_childNodes4 = []
Glycoprotein = count('glycoprotein')

# How to simplify these codes above seemed a little bit difficult to me, so I had to repeat all the codes 4 times to calculate 4 types of biomolecules


import matplotlib.pyplot as plt
# Build a dictionary to store the keywords and the relavent values
dic2 = {'DNA': DNA, 'RNA': RNA, 'Protein': total_protein, 'Glycoprotein': Glycoprotein}
labels = dic2.keys()
sizes = dic2.values()
# show the distance each part away from the center of the circle, and every portion has equal distance away from the center
explode = (0, 0, 0, 0)
# Give this pie chart some characteristics
plt.pie(sizes,explode=None,
              labels=labels,
              autopct='%1.1f%%',
              shadow=False,
              startangle=90,
              colors = {"indigo","mediumslateblue", "darkviolet", "rebeccapurple"})
# give a title
plt.title('The number of childnodes in DNA,RNA,protein and glycoprotein')
# ensure that the chart is a circle
plt.axis('equal')
plt.show()

