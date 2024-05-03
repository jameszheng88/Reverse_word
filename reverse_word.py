def reverse_word (message):
  word_letter = ""
  i = len(message)-1
  while i >= 0:
    word_letter += message[i]
    i -= 1
  return word_letter

print("Enter a word or phase")
message = input()
print(reverse_word(message))