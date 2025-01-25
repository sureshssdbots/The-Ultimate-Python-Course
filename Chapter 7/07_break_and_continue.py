for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    



def process_numbers(numbers, target):
    print("Using continue to skip even numbers:")
    for num in numbers:
        if num % 2 == 0:
            continue  # Even numbers will be skipped
        print(num)

    print("\nUsing pass as a placeholder:")
    for num in numbers:
        if num == target:
            pass  # Placeholder for future code
        print(num)

    print("\nUsing break to stop loop when target is found:")
    for num in numbers:
        if num == target:
            print(f"Found target {target}, breaking the loop!")
            break
        print(num)

    print("\nUsing else with loop:")
    for num in numbers:
        if num == target:
            print(f"Found target {target}, breaking the loop!")
            break
        print(num)
    else:
        print("Loop completed successfully without finding the target.")

    print("\nUsing a flag to indicate if target is found:")
    found = False
    for num in numbers:
        if num == target:
            found = True
            break
        print(num)

    if found:
        print(f"Target {target} found using a flag!")
    else:
        print("Target not found using a flag.")

    print("\nUsing return to exit the function immediately:")
    for num in numbers:
        if num == target:
            return f"Found target {target} and exiting function!"

    return "Target not found."


# Driver code
numbers = list(range(1, 11))
target = 5

result = process_numbers(numbers, target)
print("\nFunction Result:", result)

