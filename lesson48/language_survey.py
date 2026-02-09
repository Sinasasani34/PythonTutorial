from survey import AnonymousSurvey

question = "What language did you first learn to speak? "
language_survay = AnonymousSurvey(question)

language_survay.show_question()

print("Press 'q' at any time to ")

while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survay.store_response(response)

print("Thank you every one! ")
language_survay.show_result()