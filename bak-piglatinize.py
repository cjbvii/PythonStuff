#!/usr/bin/env python

import string, sys

sentence = str(raw_input("Enter a sentence to piglatinize: "))
words = sentence.split
vowels = "aeiou"

def piglatinize(sentence):
  for word in words():
    firstletter = word[0]
    if firstletter.lower() in vowels:
       if word.istitle():
          print word.title() + "way",
       else:
          print word + "way",
    elif word[1].lower() not in vowels:
       if word.istitle():
          print word[2:len(word)].title() + word[0:2].lower() + "ay",
       else:
          print word[2:len(word)] + word[0:2] + "ay",
    elif word[0:2].lower() == "qu":
       if word.istitle():
          print word[2:len(word)].title() + word[0:2].lower() + "ay",
       else:
          print word[2:len(word)] + word[0:2] + "ay",
    else:
       if word.istitle():
          print word[1:len(word)].title() + firstletter.lower() + "ay",
       else:
          print word[1:len(word)] + firstletter + "ay",

piglatinize(sentence)

