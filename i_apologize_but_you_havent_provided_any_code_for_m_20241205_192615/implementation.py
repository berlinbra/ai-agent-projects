Certainly! Here's a Python function that implements the bubble sort algorithm with comprehensive comments explaining how it works:

```python
def bubble_sort(arr):
    """
    Sorts an array in ascending order using the bubble sort algorithm.

    The bubble sort algorithm repeatedly steps through the array, compares adjacent
    elements, and swaps them if they are in the wrong order. This process is repeated
    until no more swaps are needed, indicating that the array is sorted.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array in ascending order.
    """
    n = len(arr)

    # Outer loop: iterate n-1 times
    for i in range(n - 1):
        # Flag to check if any swaps occurred during the current pass
        swapped = False

        # Inner loop: compare adjacent elements and swap if necessary
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred during the current pass, the array is already sorted
        if not swapped:
            break

    return arr
```

Let's go through the code and comments step by step:

1. The function `bubble_sort` takes an input array `arr` as a parameter.
2. The variable `n` is assigned the length of the input array.
3. The outer loop runs `n-1` times, representing the number of passes required to sort the array. Each pass moves the largest unsorted element to its correct position.
4. Inside the outer loop, a flag variable `swapped` is initialized to `False`. This flag is used to keep track of whether any swaps occurred during the current pass.
5. The inner loop iterates from the first element to the second-to-last unsorted element. It compares adjacent elements and swaps them if they are in the wrong order.
6. If the current element is greater than the next element, they are swapped using tuple unpacking. The flag `swapped` is set to `True` to indicate that a swap occurred.
7. After each pass, if no swaps occurred (`swapped` is `False`), it means the array is already sorted, and the algorithm can terminate early.
8. Finally, the sorted array is returned.

The bubble sort algorithm has a time complexity of O(n^2) in the worst and average cases, where n is the number of elements in the array. It is not the most efficient sorting algorithm for large datasets but can be useful for small arrays or partially sorted arrays.

The main idea behind bubble sort is to repeatedly compare adjacent elements and swap them if they are in the wrong order until the entire array is sorted. With each pass, the largest unsorted element "bubbles up" to its correct position at the end of the unsorted portion of the array.

I hope this explanation helps you understand the bubble sort algorithm and its implementation in Python!