Certainly! Here's a Python function that implements the bubble sort algorithm with comprehensive comments:

```python
def bubble_sort(arr):
    """
    Sorts the input array using the bubble sort algorithm.

    Bubble sort is a simple sorting algorithm that repeatedly steps through
    the list, compares adjacent elements, and swaps them if they are in the
    wrong order. The algorithm gets its name from the way smaller elements
    "bubble" to the top of the list with each iteration.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """

    # Get the length of the array
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swap occurred in the current pass
        swapped = False

        # Last i elements are already in place, so we only need to compare
        # the remaining unsorted elements
        for j in range(n - i - 1):
            # If the current element is greater than the next element,
            # swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred in the current pass, the array is already
        # sorted, and we can exit the loop early
        if not swapped:
            break

    # Return the sorted array
    return arr
```

Explanation:

1. The function `bubble_sort` takes an input array `arr` as a parameter.

2. We get the length of the array using `len(arr)` and store it in the variable `n`.

3. We start a loop that traverses through all the elements of the array using `for i in range(n)`. This loop represents the number of passes required to sort the array.

4. In each pass, we initialize a flag variable `swapped` to `False`. This flag will be used to check if any swapping occurred in the current pass.

5. We start another loop that compares adjacent elements in the unsorted portion of the array using `for j in range(n - i - 1)`. The range is `n - i - 1` because the last `i` elements are already in their correct positions after the previous passes.

6. Inside the inner loop, we compare the current element `arr[j]` with the next element `arr[j + 1]`. If the current element is greater than the next element, we swap them using the tuple assignment `arr[j], arr[j + 1] = arr[j + 1], arr[j]`. We also set the `swapped` flag to `True` to indicate that a swap occurred.

7. After the inner loop completes, we check the value of the `swapped` flag. If no swapping occurred in the current pass (`swapped` is `False`), it means the array is already sorted, and we can exit the outer loop early using the `break` statement.

8. Finally, we return the sorted array.

The bubble sort algorithm has a time complexity of O(n^2) in the worst and average cases, where n is the number of elements in the array. In the best case, where the array is already sorted, the time complexity is O(n) since the algorithm will exit early after the first pass.