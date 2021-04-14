# input all the information needed
name = input("Your name:")
grade_for_code_portfolio = input("Your grade for code portfolio:")
grade_for_poster_presentation = input("Your grade for poster presentation:")
grade_in_the_final_exam = input("Your grade in the final exam:")
# make a new function to compute the grade
def calculator():
    total_grade = 0
    total_grade= int(grade_for_code_portfolio)*0.4+int(grade_for_poster_presentation)*0.3+int(grade_in_the_final_exam)*0.3
    print("Your name:",name,"Total Grade:",total_grade)
    return
calculator()


