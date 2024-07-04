class school:
    def __init__(student,weight, height, age,gender):
        student.weight = weight
        student.height = height
        student.age =  age
        student.gender = gender

    def bmi(student):
        bmi = (student.weight/(student.height/100)**2)
        return bmi
    def hights(student):
        return student.hights

    def ages(student):
        return student.age

    def bmr(student):
        if student.gender.lower() == 'male':
            bmr = 10 * student.weight + 6.25 * student.height - 5 * student.age + 5
        else:
            bmr = 10 * student.weight + 6.25 * student.height - 5 * student.age - 161
        return bmr

    def bmi_category(student):
        bmi = student.bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        elif 30 <= bmi < 34.9:
            return "Obesity class 1"
        elif 35 <= bmi < 39.9:
            return "Obesity class 2"
        else:
            return "Obesity class 3"

    def tdee(student, activity_level):
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very active': 1.9
        }
        bmr = student.bmr()
        tdee = bmr * activity_multipliers.get(activity_level.lower(), 1.2)
        return tdee

    def whtr(student, waist_circumference):
        whtr = waist_circumference / student.height
        return whtr












