#%%
def encode(s):
    e=['!','@','#','$','%','^','&','*',"'"]
    l=['a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p']
    c=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    d={'A':'•−','B':'−•••','C':'−•−•','D':'−••','E':"•",'F':"••−•",'G':"−−•",'H':"••••",'I':"••",'J':"•−−−",'K':"−•−",'L':"•−••",'M':"−−",'N':"−•",'O':"−−−",'P':"•−−•",'Q':'−−•−','R':'•−•','S':'•••','T':'−','U':'••−','V':'•••−','W':'•−−','X':'−••−','Y':'−•−−','Z':'−−••','1':'•−−−−','2':'••−−−','3':'•••−−−','4':'••••−','5':'•••••','6':'−••••','7':'−−•••','8':'−−−••','9':'−−−−•','0':'−−−−−','a':'•−','b':'−•••','c':'−•−•','d':'−••','e':"•",'f':"••−•",'g':"−−•",'h':"••••",'i':"••",'j':"•−−−",'k':"−•−",'l':"•−••",'m':"−−",'n':"−•",'o':"−−−",'p':"•−−•",'q':'−−•−','r':'•−•','s':'•••','t':'−','u':'••−','v':'•••−','w':'•−−','x':'−••−','y':'−•−−','z':'−−••'}
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
def decode(s):
    d= {'•−': 'A', '−•••': 'B', '−•−•': 'C', '−••': 'D', '•': 'E', '••−•': 'F', '−−•': 'G', '••••': 'H', '••': 'I', '•−−−': 'J', '−•−': 'K', '•−••': 'L', '−−': 'M', '−•': 'N', '−−−': 'O', '•−−•': 'P', '−−•−': 'Q', '•−•': 'R', '•••': 'S', '−': 'T', '••−': 'U', '•••−': 'V', '•−−': 'W', '−••−': 'X', '−•−−': 'Y', '−−••': 'Z', '•−−−−': '1', '••−−−': '2', '•••−−−': '3', '••••−': '4', '•••••': '5', '−••••':'6','−−•••': '7', '−−−••': '8', '−−−−•': '9', '−−−−−': '0'}
    lo_dot=['1','3','5','7','9']
    le_dash=['0','2','4','6','8']
    s_morse_decode=" "
    for i in s:
        if i in lo_dot:
            s_morse_decode+="•"
        elif i in le_dash:
            s_morse_decode+="−"
        elif i ==" ":
            s_morse_decode+=" "
    #print(s_morse_decode)
    l_morse_decode=s_morse_decode.split(" ")
    #print(l_morse_decode)
    for i in l_morse_decode:
        if i=='':
            l_morse_decode.remove('')
            #l_morse_decode.remove('') #I DON'T KNOW WHY BUT THIS IS REQUIRED DON'T REMOVE 

    #print(l_morse_decode)
    s_decoded_final=""
    for i in l_morse_decode:
        for j in d:
            if i==j:
                s_decoded_final+=d[i]
    return s_decoded_final  
def master_decoder_sentence_separator(s):
    l=s.split("-||-")
    l_final=[]
    for i in l:
        l_final.append(i.split("|"))
    #print(l,end=" ")
    #print("---------------------")
    #print(l_final,end=" ")
    d=""
    for i in range(len(l_final)):
        for j in range(len(l_final[i])):
            #print(decode(l_final[i][j]),end=" ")
            d+=decode(l_final[i][j])
            d+=' '
    return d
x=input("Enter string to be encoded and decoded")
s=master_encoder_sentence_separator(x)
du=master_decoder_sentence_separator(s)
print(du)
#%%
