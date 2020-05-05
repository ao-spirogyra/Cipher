import string
from TextPackage import texthundler as thundle

# decode vigenere cipher

def calculateIndexOfCoincidence(text): 
    N = len(text)
    alphabets = list(string.ascii_lowercase)
    F = thundle.count_alphabets(text,alphabets)
    index_of_coincidence = sum([F[i]*(F[i]-1) for i in alphabets])/N*(N-1)
    return index_of_coincidence

def guessLengthOfKey(text):
    # use calculateIndexOfCoincidence()
    print('sthg')
def decryptCaeser(group):
    # use remainder of ascii%26 to express key and letter　
    print('sthg')

def splitTextToGroup(text,length_of_key):
    #split text into each group stepped by length of the key 
    text_list = list(text)
    group = [[""]*((len(text)//length_of_key) + 1) for i in [0]*length_of_key]
    for i in range(length_of_key):
        x = 0
        for l in range(i,len(text_list) + 1,length_of_key):
            try:
                group[i][x] = text_list[l]
                x += 1
            except LookupError as e:
                if (group[i][x] == ""):
                    break
    return group

def unite(group,length_of_key):
    plain_text_list = []
    plain_text = ""
    for i in range(len(group[0])):
        for l in range(length_of_key):
            plain_text_list.append(group[l][i])
    plain_text = "".join(plain_text_list)
    return plain_text


def decode(ciphered_text,length_of_key):
    # should modify to decrypt more than once corresponding with guessed key
    # execute decryptCaeser in for loop in case make decryptCaeser module
    group = splitTextToGroup(ciphered_text,length_of_key)

    eachAnalyzedGroup = decryptCaeser(group)
    
    plain_text_list = unite(eachAnalyzedGroup,length_of_key)
    plain_text = ''
    return plain_text.join(plain_text_list)
    

if __name__ == "__main__":
    ciphered_text = getTextFrom()
    length_of_key = guessLengthOfKey(ciphered_text)
    plain_text = decode(ciphered_text,length_of_key)
    print(plain_text)