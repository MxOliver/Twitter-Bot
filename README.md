# Vintage Etiquette Bot

A python based twitter bot

---

The twitter can be found [here](https://twitter.com/etiquette_bot)

Some of my favorites:

`Never refuse to keep running your cane menacingly twirled aloft, shillelah-fashion.`

`Never speak of the salt-cellars and I should hardly call a peeled pineapple in the rag.`

`Never lose your lips, drink too late.`

`Never convey the male reader, for a room.`

`Never be a servant or washed-gold watch-guards.`

## Follow Up

This is my first application built in python, and also my first attempt at teaching myself python. 
Thus, I have plenty of ideas for refactoring once I have a better grasp on the language

The markov chain algorithm I wrote uses 'Never' as a starting point instead of a randomized word. This works with this particular text because the etiquette manual is called "Never" and every scentence in the book starts with the word "Never" however, I'd like to refactor the algorithm so that it can work with any source text.

- [ ] Refactor the algorithm to pick a random start word to build the markov chain off of

- [ ] Handle issues with special characters that are present in the text 

- [ ] Refactor the set up so that the code has reusable components and easier to read

- [ ] Create a single-page application where users can upload a source text and it will print randomized phrases to the view
