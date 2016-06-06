from nltk.corpus import stopwords
from string import punctuation
sws = stopwords.words('english')
i=open('input','r')
o=open('out','w')
for line in i.readlines():
	t = [i for i in line.split() if i.strip().lower().translate(None,punctuation) not in sws]
	o.write(' '.join(t))
	o.write("\n")

