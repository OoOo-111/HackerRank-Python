if __name__ == '__main__':
    
    students=[]
    
    for student in range(int(input())):
        name = input()
        score = float(input())
        student = [name,score]
        students.append(student)
        
    students.sort(key=lambda element: element[1]) 
    firstLowest= students[0][1]
    secondLowest=0
    
    for student in students:
      if(firstLowest<student[1]):
        secondLowest=student[1]
        break
    secondLowests=[]
    for student in students:
        if secondLowest == student[1]:
            secondLowests.append(student[0])
    secondLowests.sort()
    for student in secondLowests:
        print(student)