# Activity 6: Recursive Array Toolkit

def sum_array(arr, i=0):
    if i == len(arr):
        return 0

    return arr[i] + sum_array(arr, i + 1)


def find_largest(arr, i=0):
    if len(arr) == 0:
        raise ValueError("Array must not be empty.")

    if i == len(arr) - 1:
        return arr[i]

    largest_rest = find_largest(arr, i + 1)

    if arr[i] > largest_rest:
        return arr[i]
    else:
        return largest_rest


def count_number(arr, target, i=0):
    if i == len(arr):
        return 0

    if arr[i] == target:
        return 1 + count_number(arr, target, i + 1)
    else:
        return count_number(arr, target, i + 1)



print("1. SUM THE ARRAY")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([-2, 5, -3, 10]))


print("\n2. FIND THE LARGEST NUMBER")
print(find_largest([8]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 2, 3, 15]))
print(find_largest([-10, -5, -2, -8]))


print("\n3. COUNT A CHOSEN NUMBER")
print(count_number([], 5))
print(count_number([2, 5, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 7))

1. What should the sum of an empty array be?
Answer: The sum of an empty array should be 0.

2. How can you separate one number from the rest of the array?
Answer: Use arr[0] to get the first number.

3. How does the remaining array become a smaller version of the problem?
Answer: Use arr[1:] to remove the first number.

4. What is the simplest array whose largest value is already known?
Answer: An array containing only one number.

5. How can you compare one number with the largest value from the rest of the array?
Answer: Use the max() function to compare them.

6. What should your function do if given an empty array?
Answer: It should raise a ValueError because finding the largest number requires a nonempty array.

7. What should the count be when there are no numbers left to examine?
Answer: The count should be 0.

8. How should the current number affect the count?
Answer: If the current number matches the target, add 1. Otherwise, add 0.

9. How will each call move closer to the end of the array?
Answer: Each recursive call uses arr[1:] to process the remaining elements until the array becomes empty.


Array: [5, 10, -3, 8, 5, 2]
Sum: 27
Largest Number: 10
Count of 5: 2

Additional Tests:
Sum of empty array: 0
Sum of one number: 7
Largest of one number: 9
Largest with negative numbers: -3
Count in empty array: 0
Count of missing number: 0
