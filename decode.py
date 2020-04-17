import string

# decode vigenere cipher
def count_alphabets(text,alphabets):
    for i in alphabets
        F[i] = text.count(i)
    return F

def calculateIndexOfCoincidence(text): 
    N = len(text)
    alphabets = list(string.ascii_lowercase)
    F = count_alphabets(text,alphabets)
    index_of_coincidence = sum([F[i]*(F[i]-1) for i in alphabets])/N(N-1)
    return index_of_coincidence

def guessLengthOfKey(text):
    # use calculateIndexOfCoincidence()

def DecryptCaeser(group):
    # use remainder of ascii%26 to express key and letter　

def splitTextToGroup(text,length_of_key)
    #split text into each group stepped by length of the key 
    text_list = list(text)
    for i in length_of_key
        x = 0
        for l in range(i,len(text),length_of_key)
            group[i][x] = text_list[l]
            x += 1
    return group

def unite(group,length_of_key):
    for i in len(group[0])
        for l in length_of_key
            plain_text_list = plain_text_list.append(group[l][i])
    return plain_text


def decode(ciphered_text,length_of_key):
    # should modify to decrypt more than once corresponding with guessed key
    # execute decryptCaeser in for loop in case make decryptCaeser module
    group = splitTextToGroup(ciphered_text,length_of_key)

    eachAnalyzedGroup = decryptCaeser(group)
    
    plain_text_list = unite(eachAnalyzedGroup,length_of_key)
    plain_text = ''
    return plain_text.join(plain_text_list)
    

if __name__ == "__main__"
    ciphered_text = getTextFrom()
    length_of_key = guessLengthOfKey(text)
    plain_text = decode(ciphered_text,length_of_key)
    print(plain_text)