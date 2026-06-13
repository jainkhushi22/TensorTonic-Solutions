import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    if max_len is None:
        max_len= max(len(seq) for seq in seqs) #finding maximum length
        
    pading=np.full((len(seqs),max_len),pad_value)#make a array filled with padded value
    
    for i , seq in enumerate(seqs):
        #adding sequence one by one in padding 
        if max_len<len(seq):
            seq=seq[:max_len] # if max len is less than seq we truncate the sequence
        pading[i,:len(seq)]=seq 
    return pading
    