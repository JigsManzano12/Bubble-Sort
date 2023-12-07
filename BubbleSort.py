def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Display the current state of the array with swapped elements highlighted
                print(f"Step {i + 1}, Comparing {arr[j]} and {arr[j + 1]}: {arr[:j]} [{arr[j]}] {arr[j + 1:]}")

        # Display the current state of the array after each pass
        print(f"Step {i + 1}: {arr}")

        if not swapped:
            break


# Driver code to test above
if __name__ == "__main__":
    # Take user input for the array
    input_array = input("Enter the elements of the array (space-separated): ")
    arr = list(map(int, input_array.split()))

    # Display the original array
    print("Original array:", arr)

    # Perform bubble sort and display steps
    bubbleSort(arr)

    # Display the sorted array
    print("\nSorted array:", arr)
