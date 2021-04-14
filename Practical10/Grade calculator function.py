
# make a new function to compute the grade
def calculator(name,grade_for_code_portfolio,grade_for_poster_presentation,grade_in_the_final_exam):
    total_grade = 0
    total_grade = float(grade_for_code_portfolio) * 0.4 + float(grade_for_poster_presentation) * 0.3 + float(grade_in_the_final_exam) * 0.3
    n="Your name:"+name+'      '+'Your final grade is:'+str(total_grade)
    return n
# here is an example
print("Here is an example:")
print(calculator("Xu Yuyanran",70,90,80))

# input all the information needed
name = input("Your name:")
grade_for_code_portfolio = input("Your grade for code portfolio:")
grade_for_poster_presentation = input("Your grade for poster presentation:")
grade_in_the_final_exam = input("Your grade in the final exam:")
print(calculator(name,grade_for_code_portfolio,grade_for_poster_presentation,grade_in_the_final_exam))







