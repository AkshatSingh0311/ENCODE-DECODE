#%%
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
    print(s_morse_decode)
    l_morse_decode=s_morse_decode.split(" ")
    #print(l_morse_decode)
    for i in l_morse_decode:
        if i=='':
            l_morse_decode.remove('')
            #l_morse_decode.remove('') #I DON'T KNOW WHY BUT THIS IS REQUIRED DON'T REMOVE 

    print(l_morse_decode)
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
    for i in range(len(l_final)):
        for j in range(len(l_final[i])):
            print(decode(l_final[i][j]))
s=input("Enter string to be decoded ")
master_decoder_sentence_separator(s)
#%%
