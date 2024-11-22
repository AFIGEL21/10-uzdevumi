from gensim.models import Word2Vec

# Mācīšanās korpuss
sentences = [["māja", "dzīvoklis", "jūra"]]
model = Word2Vec(sentences, min_count=1)

# Iegūst vektorus un veic līdzības analīzi
māja_vector = model.wv['māja']
dzīvoklis_vector = model.wv['dzīvoklis']
similarity = model.wv.similarity('māja', 'dzīvoklis')

print(f"Vārdu līdzība starp 'māja' un 'dzīvoklis': {similarity:.2f}")

