# Text Generation

![Whatitdoes](https://pp.vk.me/c638224/v638224173/216b1/BBVlgDc2FT4.jpg "Whatitdoes")

#### Architecture

```
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
```
![Architecture](https://pp.vk.me/c638224/v638224173/215b3/5CqdJl1AhWk.jpg "Architecture")

#### Data
- [Recipes](http://www.ffts.com/recipes.htm) 38 MB
- Marvel Movie Subs 0.408 MB
- Poems 0.926 MB
- [Iliad](http://classics.mit.edu/Homer/iliad.mb.txt), [Odyssey](http://classics.mit.edu/Homer/odyssey.mb.txt) 1.4 MB
- [Darwin](https://archive.org/stream/originofspecies00darwuoft/originofspecies00darwuoft_djvu.txt) 1.3 MB

#### References
- [Deep Learning for Speech and Language](https://telecombcn-dl.github.io/2017-dlsl/)
- [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

Slides for our project can be found [here](https://docs.google.com/presentation/d/1sTySL7mtvsF3S0tOxSmpnh0tlorLkxpwfCR29ysxENQ/edit?usp=sharing)

Webpage for the project is [here](https://diplernin.github.io/)
