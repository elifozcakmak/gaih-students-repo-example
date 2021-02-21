students=[]
grades=[]
info=dict()
sortedinfo=dict()

for i in range(5):
  students.append(input("Name-Surname: "))
  tmp=[]
  tmp.append(int(input("Midterm: ")))
  tmp.append(int(input("Final: ")))
  tmp.append(int(input("Homework: ")))
  average=(tmp[0]+tmp[1]+tmp[2])/3
  tmp.append(average)
  grades.append(tmp)
  info.update({students[i]:grades[i]})
  #print(info)

sortedinfo=dict(sorted(info.items(), key=lambda item: item[1][3], reverse=True))
student_highestgrade=list(sortedinfo.keys())[0]
print("Congratulations " + student_highestgrade +", you got the highest score!")
