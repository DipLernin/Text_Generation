<center><h1>Text Generation</h1></center>

The goal of this project is to **generate text**, accordingly to what our system has learned from its 
training, analyzing the text of certain datasets. Therefore the main idea is to **predict the next characters** given
 an input text.
An example is presented below:

<p align="center">
<img src="https://pp.vk.me/c638224/v638224173/216b1/BBVlgDc2FT4.jpg">
</p>

#### Architecture

The architecture built is described by this figure: 

<p align="center">
<img src="https://pp.vk.me/c638224/v638224173/215b3/5CqdJl1AhWk.jpg">
</p>

1. The input used is **sequences** formed by **40 one-hot encoding characters**. There are **59 possible characters**. 
2. An **RNN**(Recurrent Neural Network) layer to take into account the **temporal information** of the data.
3. A **softmax**, which for each possible character gives the corresponding probability of being the next. 
4. The output is chosen by predicting the character with the largest probability.

Different models were tried for this task, which their differences lie in which RNN is implemented: 
* **One layer LSTM** (Long Short-Term Memory) with 128 hidden units. 
* **One layer GRU** (Gated Recurrent Unit) with 128 hidden units.
* **One layer PLSTM** (Phased LSTM) 
* **Two layer LSTM** with 256 and 128 hidden units respectively.

Here we present the implementation of the one layer LSTM model implemented with **Keras**: 

```
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
```

#### Data

The datasets used for this purpose are: 

- [Recipes](http://www.ffts.com/recipes.htm) 41 MB
- Marvel Movie Subs 0.408 MB
- Poems 0.926 MB
- [Iliad](http://classics.mit.edu/Homer/iliad.mb.txt), [Odyssey](http://classics.mit.edu/Homer/odyssey.mb.txt) 1.46 MB
- [Darwin](https://archive.org/stream/originofspecies00darwuoft/originofspecies00darwuoft_djvu.txt) 1.27 MB

#### References
- [Deep Learning for Speech and Language](https://telecombcn-dl.github.io/2017-dlsl/)
- [Understanding LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

Slides for our project can be found [here](https://docs.google.com/presentation/d/1sTySL7mtvsF3S0tOxSmpnh0tlorLkxpwfCR29ysxENQ/edit?usp=sharing)

Webpage for the project is [here](https://diplernin.github.io/)
