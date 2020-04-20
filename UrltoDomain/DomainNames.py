import numpy as np
import matplotlib.pyplot as plt
filename="100UrlExamples.csv"
filename="1000UrlExamples.csv"
Urls=np.loadtxt(filename,delimiter=",",dtype="str")

Domainlist=[]
for Url in Urls:
    starti=0
    Indexlist=[]
    Index=0
    while Index!=-1:
        Index=Url.find("/",starti)
        starti=Index+1
        if Index!=-1:
            Indexlist.append(Index)
    Domainlist.append(Url[Indexlist[1]+1:Indexlist[2]])

for i in range(len(Urls)):
    if "www." in Domainlist[i]:
        Domainlist[i]=Domainlist[i][4::]


UniqueDomains=[]
for i in Domainlist:
    if i not in UniqueDomains:
        UniqueDomains.append(i)

freq=[]
for i in range(len(UniqueDomains)):
    freq.append(Domainlist.count(UniqueDomains[i]))

def sortSecond(val):
    return val[1]

Domainfreq=list(zip(UniqueDomains,freq))
Domainfreq.sort(key=sortSecond,reverse=True)
Domainfreq.reverse()
UniqueDomains,freq=zip(*Domainfreq)
freq=np.array(freq)
UniqueDomains=list(UniqueDomains)
#Horiz Bar chart
""" x=np.arange(len(UniqueDomains[-21::]))
plt.yticks(x,UniqueDomains[-21::],fontsize=8)
plt.barh(x,freq[-21::])
plt.xlabel("Frequency of Domain")
plt.ylabel("Domain Name")
plt.title("Top 20 most frequent Domains in \"{}\"\n Contains {} Urls".format(filename,len(Urls)))
plt.show()
 """

#Pie chart
OtherPercentTheshold=1 #frequencies below this percentage will be grouped in other

Totalfreq=sum(freq)
Percent=freq/Totalfreq
OtherIndex=np.where(Percent<=OtherPercentTheshold/100)
OtherPercent=Percent[OtherIndex[0][0]:OtherIndex[0][-1]+1]
OtherSum=sum(OtherPercent)
UniqueDomainsxOther=UniqueDomains[OtherIndex[0][-1]+1::]
PercentxOther=Percent[OtherIndex[0][-1]+1::]
PercentxOther=np.append(PercentxOther,OtherSum)
UniqueDomainsxOther.append("Other(<{}% frequency)".format(OtherPercentTheshold))
plt.pie(PercentxOther,labels=UniqueDomainsxOther,autopct="%1.1f%%",startangle=0)
plt.title("Frequency of Domains in \"{}\"".format(filename))
plt.axis("equal")
plt.show()

#print(len(list(set(UniqueDomains) - set(UniqueDomainsxOther)))