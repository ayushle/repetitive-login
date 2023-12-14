st=[] #string clue
wrd=str(input("words: "))
while wrd!='0': #intil 0 is entered values are taken
    st.append(wrd)
    wrd = str(input("words: "))



date=[] #date clues
dat=input("dd/mm/yyyy: ")
while dat!='0':
    date.append(dat)
    dat=input("dd/mm/yyyy: ")

ph_num=[] #phone number clues
ph_no=input("ph no :")
while ph_no!='0':
    ph_num.append(ph_no)
    ph_no=input("ph no :")

symbol=['@','&',''] #mostly used symbols

number=[0,1,2,3,4,5,6,7,8,9] #digits for combination 
