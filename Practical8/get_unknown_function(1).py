# Method A
import os
os.chdir('C:/Users/Scarlett/IBI1_2020-21/Practical8')
import re
# open the file given and we can only read it
fasta = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
# make a new file that can only be written
gene_sequence = open('gene_sequence.fa', 'w')
for line in fasta:
    # if the line includes DNA information, we turn the DNA information and the corresponding sequence into a single line ,
    # but between two different DNA sequences, there should be a newline
    if re.search('>', line):
        a = re.sub(r'\n','',line)
        b = re.sub(r'>','\n>',a)
        gene_sequence.write(b)
    else:
        # we remove all the newlilne characters so that the sequence can be turned into a single line
        c = re.sub(r'\n','',line)
        gene_sequence.write(c)
gene_sequence.close()

# open the previous file and this can only be read.
gene_sequence = open('gene_sequence.fa', 'r')
# open a new fasta file to be modified
result = open('DNA.fa', 'w')
# find all the DNA sequences having unknown functions
if re.search('unknown function', line):
    d = re.findall(r'^>(\s+)_mRNA',line).group(0)
# change the list d to string d, since write command can only be used on string.
    result.write(''.join(d))
    result.close()



# Method B
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

result = open('DNA.fa','w')
# find all DNA sequence that have unknown functions
for key in dir:
    if re.search('unknown function', key):
# try to extract the name of DNA from the whole line
        a = key[1:10]
# because names have different length, we enlarge the range to "_m"
# and then we use substitute to remove the redundant portion "_m"
        a = re.sub(r'm', '', a)
        a = re.sub(r'_', '', a)
# input all the values
        result.write(a+'   ')
        result.write(str(len(dir[key]))+'\n')
        result.write(dir[key]+'\n')