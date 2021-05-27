'''
Given an array of unique integers numbers, your task is to return all element pairs with the minimal absolute difference, in ascending order. Lower number in the pairs should come first.

Formally, return an array of pairs (arrays of size 2), of the form [i, j], where i is less than j. The pairs themselves should also be listed in ascending order within the resulting array, ordered firstly by the first number in pair, and in case of a tie by the second number.

NOTE: The pairs are not necessarily adjacent elements in numbers.

Example

For numbers = [6, 2, 4, 10], the output should be closestNumbers(numbers) = [[2, 4], [4, 6]].

The minimal absolute difference between any two elements in the array is 2, and there are two pairs with this difference: (a[0], a[2]) = (6, 4) and (a[1], a[2]) = (2, 4).
'''