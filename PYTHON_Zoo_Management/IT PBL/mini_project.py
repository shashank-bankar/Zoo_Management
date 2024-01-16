arr1, result = [], []
num = int(input("Enter the no of elements for array: "))
print("Enter the ", num, " elements of arr: ")
# for i in range(0, num):
# arr1.append(int(input()))
j = 0
while j < num:
    arr1.append(int(input()))
    j += 1
arr2 = arr1[::-1]
# Using for loop
# for i in range(num):
# result.append(arr1[i] + arr2[i])
# Using while loop
k = 0
while k < num:
    result.append(arr1[k] + arr2[k])
    k += 1
print("Given matrix: ", arr1)
print("Reverse matrix: ", arr2)
print("Resultant matrix: ", result)