import resources

wrd=resources.st
dat=resources.date
ph_num=resources.ph_num
num=resources.number
sym=resources.symbol

passwrd=[]
wrd=[]

k=len(wrd)
i=0

while (i<k):
    wrd.append(resources.st[i].upper())
    wrd.append(resources.st[i][0].upper()+resources.st[i][1:])  #to have 
    i+=1
k=len(wrd)
i=0
while i<k:
    j=0
    while j<k:
        if j==i:
            j+=1
        else:
            wrd.append(wrd[i]+wrd[j])
            j+=1
    i+=1




da_te=[]
i=0
while i<len(dat):
    da_te.append(dat[i][0:4])
    da_te.append(dat[i][4:])
    da_te.append(dat[i][0:4]+dat[i][6:])
    da_te.append(dat[i])
    i+=1
i=0
while i<len(wrd):
    j=0
    while j<len(da_te):
        k=0
        while k<len(sym):
            passwd=wrd[i]+sym[k]+da_te[j]
            passwrd.append(passwd)
            k+=1
        j+=1
    i+=1
i=0

i=0
while i<len(wrd):
    j=0
    while j<len(ph_num):
        k=0
        while k<len(sym):
            passwd=wrd[i]+sym[k]+ph_num[j]
            passwrd.append(passwd)
            k+=1
        j+=1
    i+=1

print(passwrd)