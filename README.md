# Text Generation

#### Architecture

```
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
```
![Architecture](https://pp.vk.me/c638224/v638224173/215ac/Dav5JGiBfUo.jpg "Architecture")

#### Data
- [Recipes](http://www.ffts.com/recipes.htm) 11 MB (compressed)
- Marvel Movie Subs 0.408 MB
- Poems 0.926 MB
- Iliad Odyssey 1.4 MB
- Darwin 1.3 MB

#### References
- [Deep Learning for Speech and Language](https://telecombcn-dl.github.io/2017-dlsl/)
- [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

Slides for our project can be found [here](https://docs.google.com/presentation/d/1sTySL7mtvsF3S0tOxSmpnh0tlorLkxpwfCR29ysxENQ/edit?usp=sharing)
