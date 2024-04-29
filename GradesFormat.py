# Daniela Baptiste

"""This program computes a final grade using 3 homeworks, 2 labs, and a test.
Algorithm
1.Ask the user for 3 homework grades HW1, HW2, HW3
2.Ask the user for 2 lab grades Lab1, Lab2
3.Ask the user for the test grade Exam
4.HWK_avg = (HW1 + HW2 + HW3) / 3
5. Lab_avg = (Lab1 + Lab 2) / 2
6.Formula for points is Homework * .50 * Lab * .20 * Exam * .30
7. Compute the points for each category
8. Output the points for each category
9. Compute the total points (HW * Lab * Exam)
10. Output the result
"""

HW1 = float(input("Enter the first homework grade"))
HW2 = float(input("Enter the second homework grade"))
HW3 = float(input("Enter the third homework grade"))

Lab1= float(input("Enter the first lab grade"))
Lab2= float(input("Enter the second lab grade"))

Exam = float(input("Enter the exam grade"))
# compute the averages for homework and labs
HWK_avg = (HW1 + HW2 + HW3)/ 3
Lab_avg = (Lab1 + Lab2) / 2
HWK_Points = HWK_avg * 0.50
Lab_Points = Lab_avg* 0.20
# compute the exam points
Exam_points = Exam * 0.30
TotalGrade = HWK_Points + Lab_Points + Exam_points
# output each category of points and the Total Grade
print("Homework points are %0.2f" %(HWK_Points)) # using % formatting 0.2f
print("Lab points are %0.2f" %(Lab_Points))
print("Exam points are %0.2f" %Exam_points)
# output the final graded with a label
print(f"The final average is {TotalGrade:.2f}")  # example of an f string
