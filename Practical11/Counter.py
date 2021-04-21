dict={'AA':4,
		'RA':-1,'RR':5,
		'NA':-2,'NR':0, 'NN':6,
		'DA':-2,'DR':-2,'DN':1, 'DD':6,
		'CA':0, 'CR':-3,'CN':-3,'CD':-3,'CC':9,
		'QA':-1,'QR':1, 'QN':0, 'QD':0, 'QC':-3,'QQ':5,
		'EA':-1,'ER':0, 'EN':0, 'ED':2, 'EC':-4,'EQ':2, 'EE':5,
		'GA':0 ,'GR':-2,'GN':0, 'GD':-1,'GC':-3,'GQ':-2,'GE':-2,'GG':6,
		'HA':-2,'HR':0, 'HN':1, 'HD':-1,'HC':-3,'HQ':0, 'HE':0, 'HG':-2,'HH':8,
		'IA':-1,'IR':-3,'IN':-3,'ID':-3,'IC':-1,'IQ':-3,'IE':-3,'IG':-4,'IH':-3,'II':4,
		'LA':-1,'LR':-2,'LN':-3,'LD':-4,'LC':-1,'LQ':-2,'LE':-3,'LG':-4,'LH':-3,'LI':2, 'LL':4,
		'KA':-1,'KR':2, 'KN':0, 'KD':-1,'KC':-3,'KQ':1, 'KE':1, 'KG':-2,'KH':-1,'KI':-3,'KL':-2,'KK':5,
		'MA':-1,'MR':-1,'MN':-2,'MD':-3,'MC':-1,'MQ':0, 'ME':-2,'MG':-3,'MH':-2,'MI':1, 'ML':2, 'MK':-1,'MM':5,
		'FA':-2,'FR':-3,'FN':-3,'FD':-3,'FC':-2,'FQ':-3,'FE':-3,'FG':-3,'FH':-1,'FI':0, 'FL':0, 'FK':-3,'FM':0, 'FF':6,
		'PA':-1,'PR':-2,'PN':-2,'PD':-1,'PC':-3,'PQ':-1,'PE':-1,'PG':-2,'PH':-2,'PI':-3,'PL':-3,'PK':-1,'PM':-2,'PF':-4,'PP':7,
		'SA':1, 'SR':-1,'SN':1, 'SD':0, 'SC':-1,'SQ':0, 'SE':0, 'SG':0, 'SH':-1,'SI':-2,'SL':-2,'SK':0, 'SM':-1,'SF':-2,'SP':-1,'SS':4,
		'TA':0, 'TR':-1,'TN':0, 'TD':-1,'TC':-1,'TQ':-1,'TE':-1,'TG':-2,'TH':-2,'TI':-1,'TL':-1,'TK':-1,'TM':-1,'TF':-2,'TP':-1,'TS':1, 'TT':5,
		'WA':-3,'WR':-3,'WN':-4,'WD':-4,'WC':-2,'WQ':-2,'WE':-3,'WG':-2,'WH':-2,'WI':-3,'WL':-2,'WK':-3,'WM':-1,'WF':1, 'WP':-4,'WS':-3,'WT':-2,'WW':11,
		'YA':-2,'YR':-2,'YN':-2,'YD':-3,'YC':-2,'YQ':-1,'YE':-2,'YG':-3,'YH':2, 'YI':-1,'YL':-1,'YK':-2,'YM':-1,'YF':3, 'YP':-3,'YS':-2,'YT':-2,'YW':2, 'YY':7,
		'VA':0, 'VR':-3,'VN':-3,'VD':-3,'VC':-1,'VQ':-2,'VE':-2,'VG':-3,'VH':-3,'VI':3, 'VL':1, 'VK':-2,'VM':1, 'VF':-1,'VP':-2,'VS':-2,'VT':0, 'VW':-3,'VY':-1,'VV':4}
seq1 = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2 = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
Randomseq = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"
vector  = ""
counter = 0
edit_distance = 0

# task 1: seq1 and seq2
for i in range(0,len(seq1)):
	if (seq2[i] != seq1[i]):
		edit_distance += 1
	vector = seq1[i] + seq2[i]
	if (vector not in dict):
		vector = seq2[i] + seq1[i]
	counter += dict[vector]
percentage1 = str((1-(edit_distance/len(seq1)))*100)+str("%")


print("Sequence for human SOD2 protein")
print("Alignment score: "+ str(counter))
print("Similarity of two sequences: "+ str(percentage1))


vector  = ""
counter = 0
edit_distance = 0
# task 2: seq1 and Randomseq
for i in range(0,len(seq2)):
	if (Randomseq[i] != seq1[i]):
		edit_distance += 1
	vector = Randomseq[i] + seq2[i]
	if (vector not in dict):
		vector = seq2[i] + Randomseq[i]
	counter= counter+ dict[vector]
percentage2 = str((1-(edit_distance/len(Randomseq)))*100)+str("%")


print("Sequence of mouse SOD2 protein")
print("Alignment score: "+ str(counter))
print("Similarity of two sequences: "+ str(percentage2))

counter = 0
vector  = ""
edit_distance = 0
# task 3: seq2 and Randomseq
for i in range(0,len(Randomseq)):
	if (seq2[i] != Randomseq[i]):
		edit_distance += 1
	vector = Randomseq[i] + seq2[i]
	if (vector not in dict):
		vector = seq2[i] + Randomseq[i]
	counter += dict[vector]
percentage3 =str((1-(edit_distance/len(seq2)))*100)+str("%")


print("A random sequence")
print("Alignment score: "+ str(counter))
print("Similarity of two sequences: "+ str(percentage3))