def total(m1,m2,m3):
    return m1+m2+m3
def average(m1,m2,m3):
    return (m1+m2+m3)//3          
def Result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
name = input("Enter the name:")
m1 = int(input("Enter the subjec1 marks:"))
m2 = int(input("Enter the subjec2 marks:"))
m3 = int(input("Enter the subjec3 marks:"))
marks = average(m1,m2,m3)
Report = {
    "Student Name":name,
    "Total":total(m1,m2,m3),
    "Average":average(m1,m2,m3),
    "Result":Result(average(m1,m2,m3))
}
for key,value in Report.items():
    print(key,":",value)




#Output
# Enter the subjec1 marks:95
# Enter the subjec2 marks:93
# Enter the subjec3 marks:97
# Student Name : Uma
# Total : 285
# Average : 95
# Result : Pass