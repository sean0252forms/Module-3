# Prompt the user to enter a word
# and assign it to the user_word variable.
def wordSet():
  user_word=input('input a word: ')
  word_without_vowels=''
  user_word=user_word.upper()
  for letter in user_word:
      # Complete the body of the for loop.
      if letter=='A':
        continue

      elif letter=='E':
        continue
      elif letter=='I':
        continue
      elif letter=='O':
        continue
      elif letter=='U':
        continue
      else:
        word_without_vowels+=letter
  print(word_without_vowels)