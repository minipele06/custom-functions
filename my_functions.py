# custom-functions/my_functions.py

# TODO: define temperature conversion function here

def celsius_to_fahrenheit(i):
    return (i * 9/5) + 32

# TODO: define gradebook function here

def numeric_to_letter_grade(i):
    if i >= 93:
        return "A"
    elif i >= 90:
        return "A-"
    elif i >= 87.5:
        return "B+"
    elif i >=83:
        return "B"
    elif i >= 80:
        return "B-"
    elif i >= 77.5:
        return "C+"
    elif i >= 73:
        return "C"
    elif i >= 70:
        return "D"
    else:
        return "F"

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = float(input("Provide A Celsius Temperature To Be Converted "))
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = float(input("Please Provide Your Numeric Grade "))
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)