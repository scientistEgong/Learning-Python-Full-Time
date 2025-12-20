# Count all vowels in a string.

while True:
     a_count = 0
     vowel_count = 0
     vowels = "aeiouAEIOU"
     vowel_input = input("Enter a word or 'q' to quit: ")
     if vowel_input.lower() == "q":
          print("Exiting...")
          break

     for char in vowel_input:
          if char in vowels:
             vowel_count += 1
     print(vowel_count)

     # I need to work on this further.

       
        
           
          



    

