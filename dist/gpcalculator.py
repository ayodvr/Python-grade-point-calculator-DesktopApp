class Student:
    def __init__(self,name):

        self.name = name

    def personalDetails(self):
        return "Name: {}".format(self.name)


class Gpcalculator(Student):
    def __init__(self,scores_arr,cunit_arr):
        # super().__init__(name)
        self.scores_arr = scores_arr
        self.cunit_arr = cunit_arr

    def getGradePoint(self,score):
        if score < 40:
            return 1
        if score >= 40 and score <= 45:
            return 1.5
        if score >= 46 and score <= 49:
            return 2.0
        if score >= 50 and score <= 55:
            return 2.5
        if score >= 56 and score <= 59:
            return 3.0
        if score >= 60 and score <= 65:
            return 3.5
        if score >= 66 and score <= 69:
            return 4.0
        if score >= 70 and score <= 75:
            return 4.5
        if score >= 76:
            return 5.0

    def getCgp(self):
        tgp = 0.0
        cgp = 0.0
        for i in range(len(self.scores_arr)):
            tgp += self.getGradePoint(int(self.scores_arr[i])) * self.cunit_arr[i]
        cgp += tgp / sum(self.cunit_arr)
        return cgp

    def remark(self):
        grade = self.getCgp()
        if grade >= 4.5 and grade <= 5.0:
            return "Distinction"
        if grade >= 3.5 and grade <= 4.4:
            return "Upper Credit"
        if grade >= 2.5 and grade <= 3.4 :
            return "Lower Credit"
        if grade >= 1.5 and grade <= 2.4:
            return "Pass"
        if grade <= 1.5:
            return "Fail"

        
# for i in range(10 + 1):

#     if(i > 1):

#         for j in range(2,i):

#             if(i % j == 0):
#                 break
#         else:
#             print(i)

# num = 5
# fac = 1

# for i in range(1,num + 1):
#     fac = fac * i
# print("The factorial of ",num," is",fac)
