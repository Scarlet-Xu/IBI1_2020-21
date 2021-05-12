# import all the modules needed
import re
from xml.dom.minidom import parse
import xml.dom.minidom
# parse the xlm to the dom
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
# define the term element as "DNA_associated"
information_associated = collection.getElementsByTagName("term")

# Initially we want to know if there is DNA-related gene ontology in this xml
# test the existence of DNA first
# define an integer to save the final childnode value
DNA_list = 0
for term in information_associated:
    # define "defstr" as an element of term, and the [0] means that choose the first part of the "defstr"
    defstr = term.getElementsByTagName("defstr")[0]
    # define the is_a as another element of term
    is_a = term.getElementsByTagName("is_a")
    # search whether "DNA" appears in the first portion of "defstr" element or not
    if re.search("DNA", (defstr.childNodes[0].data)):
        # if DNA exists, we choose this term and tend to figure out the childnodes it has in the is_a element
        # calculate the total length of childnodes in every is_a element, and assign the value to the established space
       DNA_list += is_a.length
print(DNA_list)

# Secondly we want to know if there is RNA-related gene ontology in this xml
RNA_list = 0
for term in information_associated:
    defstr = term.getElementsByTagName("defstr")[0]
    is_a = term.getElementsByTagName("is_a")
    # search whether "RNA" appears in the "defstr" element or not
    if re.search("RNA", (defstr.childNodes[0].data)):
       RNA_list += is_a.length
print(RNA_list)

protein_list = 0
for term in information_associated:
    defstr = term.getElementsByTagName("defstr")[0]
    is_a = term.getElementsByTagName("is_a")
    # search whether "protein" appears in the "defstr" element or not
    if re.search("protein", (defstr.childNodes[0].data)):
       protein_list += is_a.length
print(protein_list)

# I choose glycoprotein as the fourth kind of macromolecules
glycoprotein_list = 0
for term in information_associated:
    defstr = term.getElementsByTagName("defstr")[0]
    is_a = term.getElementsByTagName("is_a")
    # search whether "glycoprotein" appears in the "defstr" element or not
    if re.search("glycoprotein", (defstr.childNodes[0].data)):
       glycoprotein_list += is_a.length
print(glycoprotein_list)

# We use a matplotlib module to draw a pie chart
import matplotlib.pyplot as plt
# Build up a dictionary to input the names of macromolecules and the number of corresponding childnodes
dic = {'DNA': DNA_list, "RNA": RNA_list, "protein": protein_list, "glycoprotein": glycoprotein_list}
# make a corresponding label of each macromolecule
labels = {"DNA", "RNA", "Protein", "Glycoprotein"}
# input the total cases of each country
sizes = dic.values()
# show the distance each part away from the center of the circle, and every portion has equal distance away from the center
explode = (0, 0, 0, 0,0)
# assign some values to this pie chart
plt.pie(sizes,explode=None,
              labels=labels,
              autopct='%1.1f%%',
              shadow=False,
              startangle=90,
              colors = {"indigo","mediumslateblue", "darkviolet", "rebeccapurple"})
# give the pie chart a title
plt.title("The number of childNodes of DNA, RNA, protein and glycoprotein")
# ensure that the chart is a circle
plt.axis('equal')
plt.show()

