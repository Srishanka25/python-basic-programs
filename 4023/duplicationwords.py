def max_word_count(sen):
    words=w[w.strip() for w in sen.split()]
    d={}
    for w in words:
        if(w in d):
            d[w]+=1
        else:
            d[w]=1
    return max(d,key=d.get)
