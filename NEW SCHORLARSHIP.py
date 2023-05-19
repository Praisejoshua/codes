students=int(input('Enter the number of students'))
for i in range(1, students+1):
    attendance=int (input("Enter your minimum attendance "))
    CGPA=float(input("Enter you CGPA"))
    if attendance>=90 and CGPA>=4.5:
        print("full scholarship and complete books will be given")
    elif attendance>=90 and CGPA>=4.0:    
        print("30% scholarship and complete books will be given")
    elif attendance>=70 and CGPA>=4.0:
        print("30% scholarship and 50% of books will be given")
    elif attendance>=70 and CGPA>=3.5:
        print("no scholarship and 50% of books will be given")
    else:
        print("no scholarship  and no books will be given")
