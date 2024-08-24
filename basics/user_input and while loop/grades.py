prompt = "\nEnter grade, -1 to end: "
total_grade = 0
counter = 0
active = True
while active:
    grade = int(input(prompt))
    
    if grade == -1:
        active = False
    else:
        total_grade += grade 
        counter += 1
  
average_grade = total_grade / counter      
print(f"Average grade is: {average_grade:.2f}")