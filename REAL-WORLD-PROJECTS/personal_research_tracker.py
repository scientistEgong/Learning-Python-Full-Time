# from datetime import datetime
# import json
# import sys
# import time


# date = datetime.now()
# formatted_time = date.strftime("%Y-%m-%d %I:%M %p")
# print(formatted_time)

# def writing(text, timer=0.06):
#     """Writing effect for text display."""
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(timer)
#     print()  # Move to the next line after finishing


# def question_Database(project_title):
#     """A json database that contains the questions for the research topics."""
#     questions = [
#         f"What is the core concept of {project_title}?",
#         f"What probelm or need does {project_title} seek to address?",
#         f"How did {project_title} develop over time?",
#         f"What are the major controversies and biases concerining {project_title}?",
#         f"What are the common misconceptions about this topic?"]
        

#     # Storage for user response.
#     research_response = {
#         "title": project_title,
#         "date_added": None,
#         "status": "in-progress",
#         "questions": []
#     }

#     # Loop through each question.
#     for q in questions:
#         user_response = input(f"{q}\nYour Answer: ")


#     # Save question, answer, and feedback.
#     research_response["questions"].append({
#         "question": q,
#         "answer": user_response,
#         "validity": feedback})    
    

#     return research_response

      
    
# def add_new_topics():
#         while True:
#             writing("Project Documentation Dashboard\n")
#             project_title = input("Enter project title: ").title()
#             research_response = question_Database(project_title)
#             time = formatted_time



# def view_topics():
#     """View saved topics."""


# def update_progress():
#     """Update research progress based on recent findings"""

# def rate_for_user_experience():
#     """Rate user experience"""



# def mark_for_completion():
#     """Mark finished projects as complete."""

# def exiting_code():
#     exit()





# def main():
#     """"Main function that runs entire program"""
#     while True:
#         writing("\n--Research Tracker Dashboard--")
#         writing("1. Add new Topics✍\n" \
#         "2. View Topics\n" \
#         "3. Update Progress\n" \
#         "4. Rate user Experience🧡\n" \
#         "5. Mark as completed✅\n" \
#         "6. Exit")
#         while True:
#             writing("Enter the following options to proceed (1 - 6).")
#             user_input = input(">>> ")
#             if user_input == "1":
#                add_new_topics()
#                break
#             elif user_input == "2":
#                 view_topics()
#                 break
#             elif user_input == "3":
#                 update_progress()
#                 break
#             elif user_input == "4":
#                 rate_for_user_experience()
#                 break
#             elif user_input == "5":
#                 mark_for_completion()
#                 break
#             elif user_input == "6":
#                 exiting_code()
#                 break
#             else:
#                 writing("Invalid input!")


# # Run code               
# if __name__ == "__main__":
#     print(main())
