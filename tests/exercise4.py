class StundentsCounting:
    def count_stundents_number(self, number):
        student = 0
        s = range(0, number)
        for n in s:
            answer = input(f"is {n} student in the class?")
            if answer == "yes":
                student = student + 1
            print(student)

        print(f"{student} students are in the class and " ,number - student," are not in the class")













students_counting = StundentsCounting()
students_counting.count_stundents_number(8)
