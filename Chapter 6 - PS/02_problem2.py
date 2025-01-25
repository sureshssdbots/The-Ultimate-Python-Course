# पहला तरीका 
marks1 = int(input("Enter Marks 1: "))  
marks2 = int(input("Enter Marks 2: "))  
marks3 = int(input("Enter Marks 3: "))  

 Calculating total percentage
total_percentage = (marks1 + marks2 + marks3) / 3  

 Check if student has passed all conditions
if (total_percentage >= 40 and marks1 > 33 and marks2 > 33 and marks3 > 33):  
    print('You are passed with', total_percentage, '%')  
    
else:
    print('You have failed with', total_percentage, '%')  


##दूसरा तरीका
# Taking input for marks of three subjects
marks = [int(input(f"Enter Marks {i+1}: ")) for i in range(3)]  # List comprehension to take input for 3 subjects

# Calculate the total percentage and check pass/fail conditions
total_percentage = sum(marks) / 3  # Calculating average percentage
print(f'You are {"passed" if total_percentage >= 40 and all(d > 33 for d in marks) else "failed"} with {total_percentage}%')
