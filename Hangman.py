import random
def check(x,secretword):
    st=""
    for i in x:
        st=st+i
    if st==secretword:
        return True
    else:
        return False

file=open("words.txt","r")
string=" "
for i in file:
    string=i+string
words=list(string.split())
secretword=random.choice(words)
#print(secretword)
alphabets="abcdefghijklmnopqrstuvwxyz"
print("Welcome to the game, Hangman!")
print("I am thinking of word that is",len(secretword),"letters long.")
guess=6
li=list(secretword)
underscores=len(secretword)*"_"
x=str(underscores)
st=""
flag=0
lettersGuessed=[]
usedletters=[]
while(guess!=0):
    print("--------------")
    print("You have",guess,"guesses left")
    print("Available letters:",alphabets)
    print("Used Letters:",usedletters)
    print("Please guess a letter:",end=" ")
    ip=input()
    corner=0
    if ip not in usedletters:
            usedletters.append(ip)
    for i in lettersGuessed:
        corner=0
        if i==ip:
            print("Oops! You have already guessed that letter:",end="")
            for i in x:
                print(i,end="")
            print("")
            corner=1
            break
    if corner==1:
        continue
    lettersGuessed.append(ip)
    x=list(x)
    flag=0
    for i in range(len(li)):
        if li[i]==ip:
            inde=li.index(li[i])
            li[inde]="$"
            x[inde]=ip
            flag=1
            
    if flag==1:
        print("Good guess:",end="")
        for i in x:
            print(i,end="")   
        print()
        if check(x,secretword)==True:
            print("------------")
            print("Congratulations, you won!")
            break
        
    else:
        print("Oops! That letter is not in my word:",end="")
        guess=guess-1
        for i in x:
            print(i,end="")
        print("")        
    alpha=list(alphabets)
    for i in alpha:
        if i==ip:
            alp_index=alpha.index(i)
            final=1
            break
    if final==1:
        alphabets=alphabets[:alp_index]+alphabets[alp_index+1:]
if check(x,secretword)==False:
    print("------------")
    print("Sorry, you ran out of guesses.The word was",secretword)