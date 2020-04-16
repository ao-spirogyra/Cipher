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
    for i in num_alphabets
        index_of_coincidence += F[i]*(F[i]-1)
    return (index_of_coincidence/N(N-1))

def guessLengthOfKey(text)
# use calculateIndexOfCoincidence()

def decode(ciphered_text,length_of_key):


if __name__ == "__main__"
    ciphered_text = getTextFrom()
    length_of_key = guessLengthOfKey(text)
    plain_text = decode(ciphered_text,length_of_key)
    print(plain_text)