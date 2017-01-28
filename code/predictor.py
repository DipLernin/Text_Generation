import glob
from keras.models import load_model
import numpy as np
import sys

MODELS_FOLDER = 'trained_models'
DATASETS_FOLDER = 'datasets'

print('Loading models...')
model_files = glob.glob(MODELS_FOLDER + '/*.h5')
model_names = ['.'.join(f.split('/')[-1].split('.')[:-1]) for f in model_files]
models = dict([(n,load_model(f)) for n,f in zip(model_names,model_files)])

print('Available models:')
print(model_names)

paths = [DATASETS_FOLDER+'/'+f.split('/')[-1].split('.')[0]+'.txt' for f in model_files]
texts = [open(path).read().lower() for path in paths]
charss = [sorted(list(set(text))) for text in texts]
char_indices = dict([(n,dict((c, i) for i, c in enumerate(chars))) for n,chars in zip(model_names, charss)])
indices_char = dict([(n,dict((i, c) for i, c in enumerate(chars))) for n,chars in zip(model_names,charss)])
chars = dict(zip(model_names, charss))

maxlen = 40

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def predict(model_name, warming_text, count_char='', number=10, temperature=1.0):
    max_char_generated = 1000
    if model_name not in models:
        raise KeyError('Model not found')
    if len(warming_text) < maxlen:
        padding = ' '*(maxlen - len(warming_text))
        warming_text = padding + warming_text
    else:
        warming_text = warming_text[len(warming_text) - maxlen:]
    sentence = warming_text
    generated = ''
    while number > 0 and max_char_generated > 0:
        max_char_generated -= 1
        x = np.zeros((1, maxlen, len(chars[model_name])))
        for t, char in enumerate(sentence):
            x[0, t, char_indices[model_name][char]] = 1.
        preds = models[model_name].predict(x, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = indices_char[model_name][next_index]
        if count_char == '':
            number -= 1
        elif next_char == count_char:
            number -= 1
        generated += next_char
        sentence = sentence[1:] + next_char
        #sys.stdout.write(next_char)
        #sys.stdout.flush()
    #print(generated)
    return generated

# Example to generate 50 words
# r1 = predict('marvel_movies_subs.txt_v1', 'roses are red violets are blue', count_char=' ', number=50, temperature=0.2)
# r2 = predict('marvel_movies_subs.txt_v1', 'roses are red violets are blue', count_char=' ', number=50, temperature=1)
# r3 = predict('dummy.txt_v2', 'roses are red violets are blue', count_char=' ', number=50, temperature=0.2)
# r4 = predict('poems.txt_v1', 'roses are red violets are blue', count_char='\n', number=50, temperature=0.5)
# r5 = predict('darwin_origin_of_species.txt_v1', 'roses are red violets are blue', count_char='\n', number=50, temperature=0.5)
# r6 = predict('Homer_odyssey_Iliad.txt_v1', 'roses are red violets are blue', count_char='\n', number=50, temperature=0.5)
#
# r3 = predict('dummy.txt_v2', 'roses are red violets are blue', count_char=' ', number=50, temperature=0.5)
