# argument is text and list of alphabets
# this returns a dictionary(key is alphabet, value is number of each alphabet in the text)
# it can process various type of list(like A~Z&a~z,a~z&" "&!? or whatever)
def count_alphabets(text,alphabets):
    # make dict recording appearance times for each alphabets
    dict_counter = {}
    for i in range(len(alphabets)):
        alphabet = alphabets[i]
        dict_counter.setdefault(alphabet,text.count(alphabet))
    return dict_counter