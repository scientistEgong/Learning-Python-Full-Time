def vowel_count():
    """Count all vowels in a string."""
    vow_letters = "aeiou"

    # Get inputs
    while True:
     text = input("Enter a word or q to quit: ")
     if text.lower() == "q":
          print("Exiting...")
          break

     # print vowel
     vowels = sum(1 for char in text.lower() if char in vow_letters)
     print(f"word: {text}\nVowel count: {vowels}")


vowel_count()

       
        
           
          



    

