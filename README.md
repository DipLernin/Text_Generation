# Text Generation

#### Architecture

```
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
```

#### Data
- [Recipes](http://www.ffts.com/recipes.htm)
- Marvel Movie Subs
- Poems
- Iliad Odyssey

#### References
- [Deep Learning for Speech and Language](https://telecombcn-dl.github.io/2017-dlsl/)
- [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

Slides for our project can be found [here](https://docs.google.com/presentation/d/1sTySL7mtvsF3S0tOxSmpnh0tlorLkxpwfCR29ysxENQ/edit?usp=sharing)
