## Text Segmentation by Mean of Simulated Annealing

In recipe that is given in
[https://www.nltk.org/book/ch03.html](nltk-book), 
*Simulated Annealing* (SA) can be used as a non-deterministic search algorithm to
find the best possible text segmentation. The evaluation function that
is used in SA is purely based on the lexicon size and the length of
segments.

Two possible improvements to the technique are:
- interaction between segments are taken into the consideration by a
  mechanism such a Markov transition probability.
- a better definition of temperature for annealing
