import numpy as np

def bag_of_words_vector(tokens, vocab):
    freq={word:0  for word in vocab}
    for i in tokens:
        if i in freq:
            freq[i]+=1
    return np.array(list(freq.values()),dtype=int)