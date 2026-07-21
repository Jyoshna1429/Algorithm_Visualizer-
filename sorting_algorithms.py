import time

# Pause and stop control variables
PAUSE = False
STOP = False

def wait(delay):
    global PAUSE, STOP
    step = 0.01
    elapsed = 0
    while elapsed < delay:
        if STOP:
            break
        while PAUSE:
            time.sleep(0.05)
        time.sleep(step)
        elapsed += step

def bubble_sort(arr, draw_array, delay=0.05):
    global STOP
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            colors = ["blue"] * n
            colors[j] = "red"
            colors[j+1] = "red"
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_array(arr, colors)
            wait(delay)
            if STOP:
                return
        colors = ["green" if x >= n-i-1 else "blue" for x in range(n)]
        draw_array(arr, colors)
        wait(delay)
    draw_array(arr, ["green"]*n)

def selection_sort(arr, draw_array, delay=0.05):
    global STOP
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            colors = ["blue"] * n
            colors[i] = "yellow"
            colors[j] = "red"
            colors[min_idx] = "orange"
            draw_array(arr, colors)
            wait(delay)
            if arr[j] < arr[min_idx]:
                min_idx = j
            if STOP:
                return
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colors = ["green" if x <= i else "blue" for x in range(n)]
        draw_array(arr, colors)
        wait(delay)
    draw_array(arr, ["green"]*n)

def insertion_sort(arr, draw_array, delay=0.05):
    global STOP
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            colors = ["red" if x == j+1 or x == j+2 else "blue" for x in range(n)]
            draw_array(arr, colors)
            wait(delay)
            if STOP:
                return
        arr[j+1] = key
        colors = ["green" if x <= i else "blue" for x in range(n)]
        draw_array(arr, colors)
        wait(delay)
    draw_array(arr, ["green"]*n)

def merge_sort(arr, draw_array, delay=0.05):
    global STOP
    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m+1, r)
            merge(arr, l, m, r)
            if STOP:
                return
    def merge(arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            colors = ["green" if l <= x <= r else "blue" for x in range(len(arr))]
            draw_array(arr, colors)
            wait(delay)
            k += 1
            if STOP:
                return
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            colors = ["green" if l <= x <= r else "blue" for x in range(len(arr))]
            draw_array(arr, colors)
            wait(delay)
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            colors = ["green" if l <= x <= r else "blue" for x in range(len(arr))]
            draw_array(arr, colors)
            wait(delay)
    merge_sort_recursive(arr, 0, len(arr)-1)
    draw_array(arr, ["green"]*len(arr))

def quick_sort(arr, draw_array, delay=0.05):
    global STOP
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi-1)
            quick_sort_recursive(arr, pi+1, high)
            if STOP:
                return
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            colors = ["blue"] * len(arr)
            colors[high] = "orange"
            colors[j] = "red"
            colors[i] = "yellow" if i >= 0 else "blue"
            draw_array(arr, colors)
            wait(delay)
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            if STOP:
                return i+1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        draw_array(arr, ["green" if x <= i+1 else "blue" for x in range(len(arr))])
        wait(delay)
        return i+1
    quick_sort_recursive(arr, 0, len(arr)-1)
    draw_array(arr, ["green"]*len(arr))