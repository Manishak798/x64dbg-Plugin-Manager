def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted list:", unsorted_list)
    
    bubble_sort(unsorted_list)
    
    print("Sorted list:", unsorted_list)
