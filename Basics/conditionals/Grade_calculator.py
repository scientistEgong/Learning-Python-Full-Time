# Grade calculator program.
while True:
    score = input("Enter your score and check your grade or 'q' to quit: ")
    if score.lower() == "q":
        print("Breaking out of grade calculator program...")
        break

 
    try:
        score = int(score)

        if score < 0 or score > 100:
            print("Number must be between 0 and 100.")
            continue


        # conditions
        a_grade = (score >= 70) and (score <= 100)
        b_grade = (score >= 60 ) and (score <= 69)
        c_grade = (score >= 50) and (score <= 59)
        d_grade = (score >= 40) and (score <= 49)
        

        if a_grade:
            print(f"You had an A of {score}")
        elif b_grade:
            print(f"You had a B of {score}")
        elif c_grade:
            print(f"You had a  C of {score}")
        elif d_grade:
            print(f"You had a D of {score}")
        else:
            print(f"You had an F of {score}") 


    except ValueError:
        print("Invalid option, Try again.")

 