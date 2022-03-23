import string
message = input('enter the message: ').upper().replace('J','I')
key = input('enter the key: ').upper().replace('J','I')

unique_key={}
alphabet_list=[]
alphabet_seq = string.ascii_uppercase.replace('J','I');

def create_matrix():
    matrixList=[]
    for val in range(0,len(key)):
        if key[val] not in unique_key:
            unique_key[key[val]]=1
            alphabet_list.append(key[val])
    for i in range(0,26):
        if alphabet_seq[i] not in unique_key:
            unique_key[alphabet_seq[i]]=1
            alphabet_list.append(alphabet_seq[i])
    for i in range(0,5):
        start=i*5
        end =i*5+5
        for j in range(start,end,start+6):
            matrixList.append([alphabet_list[j],alphabet_list[j+1],alphabet_list[j+2],alphabet_list[j+3],alphabet_list[j+4]])
    return matrixList

def createPair():
    messagePair=[]
    lenth = len(message)
    if(lenth%2):
        message.join('X')
    for i in range(1,len(message),2): 
        if(message[i]==message[i-1]):
            messagePair.append([message[i-1],'X'])
        else:
            messagePair.append([message[i-1],message[i]])
    return messagePair   
   
  
def find_row_col(matrixList,x):
    ans=list([])
    flag = 0
    for i in range(0,5):
        for j in range(0,5):
            if(matrixList[i][j]==x):
                ans.append([i,j])
                return ans
def cipherText(matrixlist,messagePair):
    cipherText=''
    for pair in messagePair:
        ans1 = find_row_col(matrixlist,pair[0])
        ans2 = find_row_col(matrixlist,pair[1])
        print(ans1,ans2)
        x1 = (ans1[0][0])
        y1 = (ans1[0][1])
        x2 = (ans2[0][0])
        y2 = (ans2[0][1])
        #print(ans1,ans2)
        if(x1==x2):
            y1=(y1+1)%5
            y2=(y2+1)%5
            cipherText+=matrixList[x1][y1]
            cipherText+=matrixlist[x2][y2]
        elif y1 == y2:
            x1 = (x1+1)%5
            x2 = (x2+1)%5
            cipherText+=matrixList[x1][y1]
            cipherText+=matrixlist[x2][y2]
        else:
            cipherText+=matrixList[x1][y2]
            cipherText+=matrixlist[x2][y1]
        cipherText+=' '
    return cipherText
def plainText(matrixlist,cipherText):
    plainTex=''
    for i in range(0,len(cipherText),3):
        ans1 = find_row_col(matrixlist,cipherText[i])
        ans2 = find_row_col(matrixlist,cipherText[i+1])
        x1 = (ans1[0][0])
        y1 = (ans1[0][1])
        x2 = (ans2[0][0])
        y2 = (ans2[0][1])
       # print(ans1,ans2)
        if(x1==x2):
            y1=abs((y1-1)%5)
            y2=abs((y2-1)%5)
            plainTex+=matrixList[x1][y1]
            plainTex+=matrixlist[x2][y2]
        elif y1 == y2:
            x1 = abs((x1-1)%5)
            x2 = abs((x2-1)%5)
            plainTex+=matrixList[x1][y1]
            plainTex+=matrixlist[x2][y2]
        else:
            plainTex+=matrixList[x1][y2]
            plainTex+=matrixlist[x2][y1]
        plainTex+=' '
    return plainTex
      
matrixList  = create_matrix()
print(matrixList)
messagePair = createPair()
print(messagePair)
cipherTex = (cipherText(matrixList,messagePair))
print(cipherTex)
print(plainText(matrixList,cipherTex))





