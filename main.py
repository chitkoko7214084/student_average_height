#Author Chit Ko Ko


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])




total_heights=0
for num in student_heights:
    total_heights=total_heights+num


count = 0

# Iterate through the list and increment the count for each element
for _ in student_heights:
    count += 1

average_height = total_heights / count


print(round(average_height))




