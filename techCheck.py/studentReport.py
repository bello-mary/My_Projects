def main():
    #Input
    studentName = input("Enter student's name : " )
    courseName = input("Enter your course name : " )
    numOfAbsence = int(input("Enter number of Absence : " ))
    numOfAttendance = int(input("Enter number of Attendance : " ))

    #Processing
    total = numOfAttendance + numOfAbsence
    attendancePct = numOfAttendance/total

    #Output
    print("The Student's name is  ",studentName)
    print("The Course's name is ",courseName)
    print("Absences : ", numOfAbsence ,"Classes")
    print("Attendances :", numOfAttendance, "Classes")
    print("Attendance percent :", "{0:.2f}".format(attendancePct))


main()