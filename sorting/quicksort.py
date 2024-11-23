from random import randint


def quicksort(arr: list[int], low: int, high: int):
    """
    Time complexity: best case O(nlog(n)), worst case O(n^2)
    - best case is if partition is in the middle of the array

    Args:
        arr (list[int]): array to be sorted
        low (int): index of lowest element
        high (int): index of highest element
    """

    def partition(low: int, high: int):
        # choose random pivot element
        chosen_pivot = randint(low, high)
        arr[chosen_pivot], arr[high] = arr[high], arr[chosen_pivot]
        pivot = arr[high]
        # partition index (index with element which is smaller than pivot)
        i = low

        for j in range(low, high):
            print(f"{arr}, i: {i}, j: {j}")
            if arr[j] <= pivot:
                print(f"swap {i} {j}")
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # swap pivot number (at end of arr) with its position
        arr[i], arr[high] = arr[high], arr[i]

        return i

    if low < high:
        pivot = partition(low, high)

        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


def main():
    arr = [4, 1, 5, 10, 8, -1, 50, 90]

    quicksort(arr, 0, len(arr) - 1)

    print(arr)


if __name__ == "__main__":
    main()
