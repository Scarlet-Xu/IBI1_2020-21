# make a dictionary including all the codons
DNA_codons = {
    'TTT' : 'F', 'TCT' : 'S', 'TAT': 'Y', 'TGT': 'C',
    'TTC' : 'F', 'TCC' : 'S', 'TAC': 'Y', 'TGC': 'C',
    'TTA' : 'L', 'TCA' : 'S', 'TAA': 'O', 'TGA': 'X',
    'TTG' : 'L', 'TCG' : 'S', 'TAG': 'U', 'TGG': 'W',
    'CTT' : 'L', 'CCT' : 'P', 'CAT': 'H', 'CGT': 'R',
    'CTC' : 'L', 'CCC' : 'P', 'CAC': 'H', 'CGC': 'R',
    'CTA' : 'L', 'CCA' : 'P', 'CAA': 'Q', 'CGA': 'R',
    'CTG' : 'L', 'CCG' : 'P', 'CAG': 'Z', 'CGG': 'R',
    'ATT' : 'I', 'ACT' : 'T', 'AAT': 'N', 'AGT': 'S',
    'ATC' : 'I', 'ACC' : 'T', 'AAC': 'B', 'AGC': 'S',
    'ATA' : 'J', 'ACA' : 'T', 'AAA': 'K', 'AGA': 'R',
    'ATG' : 'M', 'ACG' : 'T', 'AAG': 'K', 'AGG': 'R',
    'GTT' : 'V', 'GCT' : 'A', 'GAT': 'D', 'GGT': 'G',
    'GTC' : 'V', 'GCC' : 'A', 'GAC': 'D', 'GGC': 'G',
    'GTA' : 'V', 'GCA' : 'A', 'GAA': 'E', 'GGA': 'A',
    'GTG' : 'V', 'GCG' : 'A', 'GAG': 'E', 'GGG': 'G'}
import os
# change the directory to where the file was downloaded
os.chdir('C:/Users/Scarlett/IBI1_2020-21/Practical8')
import re
# open and read the file
fasta = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
# make a new dictionary to store DNA names and sequences
dir = {}
for line in fasta:
# when the line begins with ">", we should store the whole line(DNA name) into the key of dictionary
    if line.startswith('>'):
        key = str(line)
        dir[key]= ''
# if not, we should store the DNA sequences into the value of dictionary and remove the newline characters
    else:
        dir[key] = dir[key] + line.replace('\n', '')
fasta.close()

# the user can input the filename when operating it
result = input('Please input the filename:')
final = open(result,'w')

# find all DNA sequence that have unknown functions
for key in dir:
    if re.search('unknown function', key):
# try to extract the name of DNA from the whole line
        a = key[1:10]
# because names have different length, we enlarge the range to "_m"
# and then we use substitute to remove the redundant portion "_m"
        a = re.sub(r'm', '', a)
        a = re.sub(r'_', '', a)
        protein=[]
# input all the DNA codons into the new list named protein
        for i in range(1,int(len(dir[key])/3)+1):
            protein.append(DNA_codons[dir[key][3*i-3: 3*i]])
        x = ''
# turn the list into a string
        for i in protein:
            x = x+i
# modify the new fasta format so that the content will show up as we want to see.
        final.write(a+'      ')
        final.write(str(len(dir[key])//3)+'\n')
        final.write(x+'\n')


