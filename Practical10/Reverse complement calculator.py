# input a new DNA sequence
DNA= list(input('please input DNA sequence:'))
DNA_complement= ""
# make a new dictionary to record all the base pairings
complement= { "A": "T", "T": "A", "C": "G", "G": "C", "a": "t", "t":"a", "c":"g","g":"c"}
# make s to be the keys in the "complement" dictionary
for s in complement:
    for i in range(len(DNA)):
        # the bases in the sequence are paired with the values of dictionary in turn
        DNA_complement=DNA_complement + complement["".join(DNA[i])]
        # because the value is assigned repeatedly for the whole sequence, so we just select the first part of the repeated complement DNA
        DNA_complement= DNA_complement[0:len(DNA)]
# turn all the small letters into capital letters
DNA_complement = DNA_complement.upper()
# get the final complement DNA sequence
print(DNA_complement)

# make a new list
list_num = []
# turn the string of complement into a list
DNA_complement= list(DNA_complement)
# define a function to reverse the complement DNA sequence
def convert_order():
    for i in range(len(DNA_complement)):
        # convert the DNA strand in turn to become a reverse complement DNA sequence
        list_num.append(DNA_complement[len(DNA_complement)-i-1])
    # turn the list into a string
    print(''.join(list_num))
# initialse the function
convert_order()
