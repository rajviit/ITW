class student:
    def __init__(self, id, name, age, english, science, maths):
        self.id = id
        self.name = name
        self.age = age
        self.english = english
        self.science = science
        self.maths = maths

    def CalcStudent(self):
        total = (self.english + self.science + self.maths)
        percentage = (total/300)*100
        print("Result is: ")
        print("The total is :", total)
        if (self.english > 50 and self.science > 50 and self.maths > 50):
            print("You are pass")
        else:
            print("your are fail")
        print("percentage")
        if (percentage >= 75):
            print("Has got A Grade")
        elif (percentage >= 60 and percentage < 75):
            print("Has got B Grade")
        elif (percentage >= 50 and percentage < 60):
            print("Has got C Grade")
        else:
            print("You are not eligible for any grade due to Fail Status")


if __name__ == '__main__':
    name = input("Enter your name : ")
    id = input("Enter your id : ")
    age = int(input("Enter your age: "))
    maths = int(input("Enter your maths marks: "))
    science = int(input("Enter your science marks: "))
    english = int(input("Enter your english marks: "))
    s1 = student(id, name, age, english, science, maths)
    s1.CalcStudent()