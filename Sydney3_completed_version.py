# sentence for testing purpose
# Our university has 25 students in Room 101, and they scored 89 out of 100 points!\nWe have 3 classes today, and 7 more assignments are due.

# Printing the welcome logo
print("=" * 50)
print("WELCOME TO LETTER COUNTER MACHINE".center(50))
print("=" * 50)
print("")

# Taking the input sentence from the user
sentence = input("Enter your sentence: ")

# or

# you can use the below sentence for testing purpose without taking input from the user
'''sentence = "Our university has 25 students in Room 101, and they scored 89 out of 100 points!\nWe have 3 classes today, and 7 more assignments are due."
'''
#checking if the input sentence is empty or not
while len(sentence) == 0:
  print("Please enter a valid sentence.")
  sentence = input("Enter your sentence: ")

# Implement the while loop to run the program
while True:

  # giving choices to the user to select the type of analysis they want to perform on the sentence
  print("")
  print("What do you want to do with the sentence?")
  print("1. Character census (Total number of characters, Number of letters, digits, whitespace, punctuation, etc.)")
  print("2. Case and vowel breakdown (uppercase, lowercase, vowels, consonants, individual vowel counts.)")
  print("3. Word statistics (Total words, longest word, average word length)")
  print("4. Line and sentence statistics (number of lines, sentences, and length of the longest line)")
  print("5. Exit the program")
  print("")

  print("")
  choice = input("Enter your choice (1-5): ")
  print("")

  if choice in ('1', '2', '3', '4', '5'):

    # Calling the respective functions based on the user's choice
    if choice =='5':
      print("")
      print("=" * 70)
      print("Exiting the program. Thank you for using the Letter Counter Machine!".center(70))
      print("=" * 70)
      print("")
      break

    if choice == '1':
      # Declaring a dictionary to store the count of each letter
      word_dic = {}

      # The total letters in the sentence
      total_characters = len(sentence)

      # Counting how many each word is counted in the sentence
      for char in sentence:
        if char not in word_dic:
          word_dic[char] = 0
        word_dic[char] += 1

      # Counting digits in the sentence
      digits = "1234567890"
      total_digits = 0
      for char in sentence:
        if char in digits:
          total_digits += 1

      """
      Counting whitespaces in the sentence
      It will also count the new line and tabs
      (If you not using input func for your sentence)
      """
      whitespace = " \n\t"
      total_whitespace = 0
      for char in sentence:
        if char in whitespace:
          total_whitespace += 1

      # Counting punctuation and other character in the sentence
      puntuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
      punctuation_count = 0
      for char in sentence:
        if char in puntuation:
          punctuation_count += 1

      # Printing the result logo
      print("")
      print("=" * 70)
      print("HERE IS THE RESULT".center(70))
      print("=" * 70)
      print("")

      # Printing the result
      print(f"{'Total characters in sentence':40}: {total_characters}")
      print(f"{'Total each letter used in sentence':40}: {word_dic}")
      print(f"{'Total digits in sentence':40}: {total_digits}")
      print(f"{'Total white spaces in sentence':40}: {total_whitespace}")
      print(f"{'Total other characters in sentence':40}: {punctuation_count}")

    if choice == '2':

      # Counting the upper and Lower case letters
      upper = 0
      lower = 0
      for i in sentence:
        if i.isupper():
          upper += 1
        if i.islower():
          lower += 1

      # Counting vowels and consonants
      vowels = 0
      consonants = 0
      for i in sentence:
        if i.isalpha():
            if i.lower() in "aeiou":
                  vowels += 1
            else:
                  consonants += 1

      # Counting individual vowels count in sentence
      count={"a":0, "e":0, "i":0, "o":0, "u":0}
      for ch in sentence.lower(): # converts all uppercase letters to lower case
            if ch in count:
                  count[ch] +=1

      # Printing the result logo
      print("")
      print("=" * 70)
      print("HERE IS THE RESULT".center(70))
      print("=" * 70)
      print("")

      # Printing the result
      print(f"{'All upper case letters in sentence':40}: {upper}")
      print(f"{'All lowercase letters in sentence':40}: {lower}")
      print(f"{'All vowels in sentence':40}: {vowels}")
      print(f"{'All consonants in sentence':40}: {consonants}")
      for vowel, count in count.items():
        bar = '█' * count
        print(f"{'Total ' + vowel + ' in sentence':40}: {bar} ({count})")

    if choice == '3':
      #Scannning character by character to find word and decraling varibles to store the result
      total_words = 0
      longest_word = ""
      current_word = ""
      total_word_letters = 0

      for char in sentence:
        if char.isalpha() or char == "'":
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


      # Printing the result logo
      print("")
      print("=" * 70)
      print("HERE IS THE RESULT".center(70))
      print("=" * 70)
      print("")

      # Printing the result
      print(f"{'Total words in sentence':40}: {total_words}")
      print(f"{'Longest word and its length':40}: {longest_word} (Length:{len(longest_word)})")
      print(f"{'Average word length':40}: {average_length}")

    if choice == '4':

      # Declaring variables to store the result
      lines_count = 1
      longest_line_len = 0
      current_line_len = 0
      sentences_count = 0

      # Checking the sentence character one by one
      for char in sentence:
        #1. Count lines (separated by the newline character '\n')
        if char == '\n':
          lines_count += 1
          # Checking if the line we just finished is the longest one
          if current_line_len > longest_line_len:
            longest_line_len = current_line_len
          #Counting character for next line
          current_line_len = 0
        else:
          # If it's not a new line add 1 to the length of current line
          current_line_len += 1
          
        #2. Count sentences (ending with '.', ',', '!', or '?'
        if char in '?!,.':
          sentences_count += 1
              
        #3. Checking if the length of final line is the longes
        if current_line_len > longest_line_len:
          longest_line_len = current_line_len

      # Printing the result logo
      print("")
      print("=" * 70)
      print("HERE IS THE RESULT".center(70))
      print("=" * 70)
      print("")

      # Printing the result
      print(f"{'Total line in text':40}: {lines_count}")
      print(f"{'Total sentences in text':40}: {sentences_count}")
      print(f"{'Longest line length':40}: {longest_line_len} character")

  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
