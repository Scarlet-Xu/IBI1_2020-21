gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
import numpy as np
# make a and b correspond to each other 
a = np.array(gene_lengths)
b = np.array(exon_counts)
average_exon_length = a/b
# sort the list
n = sorted(average_exon_length)
print(n)


# use numpy and matplotlib to draw a boxplox
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(n,
            # give the chart a name
            labels = {'Average exon length'},
            # set the widths of boxplot
            widths = 0.75,
            # the boxplot can have a color
            patch_artist = True,
            # give the boxplot yellow on the surface and purple on the line
            boxprops ={'color':'purple', 'facecolor':'yellow'})
plt.show()
