#!/usr/bin/env python

import string, sys

sentence = str(raw_input("Enter a sentence to piglatinize: "))
words = sentence.split
vowels = "aeiouy"
punctuation = ".,?!:;"
pigsentence =[]


def piglatinize(sentence):
  for word in words():
    punct=""
    firstletter = word[0]
    if word[len(word)-1] in punctuation:
       punct = word[len(word)-1]
       word = word[0:len(word)-1]
    firstletter = word[0]
    if firstletter.lower() in vowels:
          pigword = word.lower() + "way" + punct
          if word.istitle():
             pigword = pigword.title()
          pigsentence.append(pigword)
    elif word[1].lower() not in vowels:
          pigword = word[2:len(word)] + word[0:2].lower() + "ay" + punct
          if word.istitle():
             pigword = pigword.title()
          pigsentence.append(pigword)
    elif word[0:2].lower() == "qu":
          pigword = word[2:len(word)] + word[0:2].lower() + "ay" + punct
          if word.istitle():
             pigword = pigword.title()
          pigsentence.append(pigword)
    else:
          pigword = word[1:len(word)] + firstletter.lower() + "ay" + punct
          if word.istitle():
             pigword = pigword.title()
          pigsentence.append(pigword)

piglatinize(sentence)

print ' '.join(pigsentence)

