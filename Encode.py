#%%
import random as r
def encode(s):
    e=['!','@','#','$','%','^','&','*',"'"]
    l=['a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p']
    c=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    d={'A':'•−','B':'−•••','C':'−•−•','D':'−••','E':"•",'F':"••−•",'G':"−−•",'H':"••••",'I':"••",'J':"•−−−",'K':"−•−",'L':"•−••",'M':"−−",'N':"−•",'O':"−−−",'P':"•−−•",'Q':'−−•−','R':'•−•','S':'•••','T':'−','U':'••−','V':'•••−','W':'•−−','X':'−••−','Y':'−•−−','Z':'−−••','1':'•−−−−','2':'••−−−','3':'•••−−−','4':'••••−','5':'•••••','6':'−••••','7':'−−•••','8':'−−−••','9':'−−−−•','0':'−−−−−','a':'•−','b':'−•••','c':'−•−•','d':'−••','e':"•",'f':"••−•",'g':"−−•",'h':"••••",'i':"••",'j':"•−−−",'k':"−•−",'l':"•−••",'m':"−−",'n':"−•",'o':"−−−",'p':"•−−•",'q':'−−•−','r':'•−•','s':'•••','t':'−','u':'••−','v':'•••−','w':'•− −','x':'−••−','y':'−•− −','z':'− −••'}
    lo_dot=[1,3,5,7,9]
    le_dash=[0,2,4,6,8]
    cs=""
    ms=""
    for i in s:
        for j in d:
            if i==j:
                ms+=d[i]+r.choice(e)+r.choice(l)+r.choice(c)+" "
    for i in ms:
        if i=="•":
            cs+=str(r.choice(lo_dot))
        if i=="−":
            cs+=str(r.choice(le_dash))
        if i==" ":
            cs+=" "
        if i in e or i in l or i in c:
            cs+=i
    return cs
def master_encoder_sentence_separator(x):
    s=""
    l=x.split(".")
    l_end=[]
    for i in range(len(l)):
        l_end.append(l[i].split())
    if l_end[len(l_end)-1]==[]:
        l_end.remove([])
    for i in range(len(l_end)):
        if i!=0:
            s+="-||-" #sentence separator
        for j in range(len(l_end[i])):
            s+=encode(l_end[i][j])+"|" #word separator 
    s+="-||-"
    return s
x=input("enter the string to be coverted ")
print(master_encoder_sentence_separator(x))
#%%
