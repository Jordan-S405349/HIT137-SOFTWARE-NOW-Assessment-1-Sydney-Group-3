#printing the welcome logo
print("=" * 50)
print("WELCOME TO WORD STATISTICS MACHINE".center(50))
print("="* 50)

#implement the while loop to run the program
while True:
  print("")
  sentence = input("Enter your sentence: ")

  #varibales for word statistics
  total_words = 0
  longest_word = ""
  current_word = ""
  total_word_letters = 0

  #Scannning character by character to find word
  for char in sentence:
    if char.isalpha() or char =="'":
      current_word += char
    else:
      if len(current_word) > 0:
        total_words += 1
        total_word_letters += len(current_word)

        #Check for the longest word
        if len(current_word) > len(longest_word):
          longest_word = current_word

        current_word = ""

  #Check if the sentence ended on a word
  if len(current_word) > 0:
    total_words += 1
    total_word_letters += len(current_word)
    if len(current_word) > len(longest_word):
      longest_word = current_word

  #calculate the average word length
  if total_words > 0:
    average_length = round(total_word_letters / total_words, 1)
  else:
    average_length = 0.0

  #Printing the result logo
  print("")
  print("="* 50)
  print("HERE IS THE REUSLT".center(50))
  print("=" * 50)
  print("")

  #printing the result
  print(f"{'Total words in sentence':40}: {total_words}")
  print(f"{'Longest word and its length':40}: {longest_word} (Length:{len(longest_word)})")
  print(f"{'Average word length':40}: {average_length}")

  print("")
  print("=" * 50)
  print("THANK YOU!!!".center(50))
  print("=" * 50)
  print("")

  #Break the while loop after printing the result
  break