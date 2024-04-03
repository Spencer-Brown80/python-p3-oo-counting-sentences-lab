#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, stringVal):
    if isinstance(stringVal, str):
      self._value = stringVal
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    return self._value.endswith(".")
      
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    pattern = r'[.?!]+'
    matches = re.findall(pattern, self.value)
    return len(matches)
    
      
    
  
  
  
  
