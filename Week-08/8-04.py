Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.There is only one repeated number in nums, return this repeated number. Solve the problem using set.

Example 1:

Input: nums = [1,3,4,2,2]

Output: 2



Example 2:

Input: nums = [3,1,3,4,2]

Output: 3



For example:

Input	                    Result

1 3 4 4 2	                 4



Coding:

n =input().split(" ")

n = list(n)

for i in range(len(n)):

    for j in range(i+1,len(n)):

        if n[i] == n[j]:

            print(n[i])

            exit(0)

