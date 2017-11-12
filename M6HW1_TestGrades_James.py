# CTI 110
# M6HW1 - Test Average and Grades
# Jeremiah James
# 4 NOV 2017



def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_grade(score):
    if(score < 60):
        return "F"
    elif(score < 70):
        return "D"
    elif(score < 80):
        return "C"
    elif(score < 90):
        return "B"
    elif(score < 101):
        return "A"

def ask_for_scores():
    score1 = float(input("please enter score 1: "))
    score2 = float(input("please enter score 2: "))
    score3 = float(input("please enter score 3: "))
    score4 = float(input("please enter score 4: "))
    score5 = float(input("please enter score 5: "))

    return score1, score2, score3, score4, score5

def print_table_of_results(score1, score2, score3, score4, score5):
    print("\nScore\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1), \
          str(score2) + "\t\t" + determine_grade(score2), \
          str(score3) + "\t\t" + determine_grade(score3), \
          str(score4) + "\t\t" + determine_grade(score4), \
          str(score5) + "\t\t" + determine_grade(score5), sep = "\n" )
                           
    
def main():
    score1, score2, score3, score4, score5 = ask_for_scores()
    print_table_of_results(score1, score2, score3, score4, score5)
    print()
    print("The average of test scores:", calc_average(score1, score2, score3, score4, \
    score5))


main()
        
