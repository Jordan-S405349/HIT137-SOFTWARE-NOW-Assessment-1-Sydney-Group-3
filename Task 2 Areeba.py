# Printing the welcome logo
print("=" * 80)
print("WELCOME TO CASE AND LETTER ANALYZER".center(50))
print("=" * 80)

sentence = input("Enter your sentence: ")

# Counting the upper and Lower case letters
u=0
l=0
for i in sentence:
  if i.isupper():
     u+=1
  if i.islower():
     l+=1
# Counting vowels and consonants
v=0
c=0
for i in sentence:
    if i.isalpha():
         if i.lower() in "aeiou":
               v+=1
         else:
               c+=1
# Counting individual vowels count in sentence


count={"a":0, "e":0, "i":0, "o":0, "u":0}
for ch in sentence.lower(): # converts all uppercase letters to lower case
       if ch in count:
             count[ch] +=1


 # Printing the Output
print("")
print("=" * 80)
print("HERE IS THE Output".center(50))
print("=" * 80)
print("")


print("All upper case letters in sentence :",u)
print("All lowercase letters in sentence  :",l)
print("All vowels in sentence             :",v)
print("All consonants in sentence         :",c)
print(f"{'Total individual vowels count in sentence':40}: {count}")


print("=" * 80)
print("THANK YOU!!!".center(50))
print("=" * 80)
print("")