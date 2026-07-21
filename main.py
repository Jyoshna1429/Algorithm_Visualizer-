import tkinter as tk
import random
from tkinter import ttk
from visualizer import Visualizer
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, PAUSE, STOP

WIDTH = 800
HEIGHT = 400

root = tk.Tk()
root.title("Ultimate Algorithm Visualizer")

# ---------- Controls ----------
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

algorithm_menu = ttk.Combobox(control_frame, values=["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"])
algorithm_menu.current(0)
algorithm_menu.grid(row=0, column=0, padx=10)

speed_label = tk.Label(control_frame, text="Speed:")
speed_label.grid(row=0, column=1, padx=5)
speed_slider = tk.Scale(control_frame, from_=1, to=100, orient=tk.HORIZONTAL)
speed_slider.set(50)
speed_slider.grid(row=0, column=2, padx=5)

size_label = tk.Label(control_frame, text="Array Size:")
size_label.grid(row=0, column=3, padx=5)
size_slider = tk.Scale(control_frame, from_=5, to=100, orient=tk.HORIZONTAL)
size_slider.set(30)
size_slider.grid(row=0, column=4, padx=5)

# ---------- Canvas ----------
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(pady=20)

visualizer = Visualizer(canvas, WIDTH, HEIGHT)
array = []

# ---------- Array Label ----------
array_label = tk.Label(root, text="", font=("Arial", 12))
array_label.pack(pady=5)

# ---------- Info Label ----------
info_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
info_label.pack(pady=5)

def update_array_label(arr):
    array_label.config(text=str(arr))

def get_delay():
    return max(0.001, 0.1 - (speed_slider.get() / 1000))

# ---------- Functions ----------
def generate_array():
    global array, STOP
    STOP = False
    array = [random.randint(10, 100) for _ in range(size_slider.get())]
    colors = ["blue"] * len(array)
    visualizer.draw_array(array, colors)
    update_array_label(array)
    info_label.config(text="")

def start_sorting():
    global STOP, PAUSE
    STOP = False
    PAUSE = False
    algo = algorithm_menu.get()
    delay = get_delay()
    info_label.config(text=f"Sorting with {algo}...")
    if algo == "Bubble Sort":
        bubble_sort(array, visualizer.draw_array, delay)
    elif algo == "Selection Sort":
        selection_sort(array, visualizer.draw_array, delay)
    elif algo == "Insertion Sort":
        insertion_sort(array, visualizer.draw_array, delay)
    elif algo == "Merge Sort":
        merge_sort(array, visualizer.draw_array, delay)
    elif algo == "Quick Sort":
        quick_sort(array, visualizer.draw_array, delay)
    update_array_label(array)
    info_label.config(text=f"{algo} Completed!")

def pause_resume():
    global PAUSE
    PAUSE = not PAUSE
    pause_button.config(text="Resume" if PAUSE else "Pause")

def stop_sorting():
    global STOP, PAUSE
    STOP = True
    PAUSE = False

# ---------- Buttons ----------
generate_button = tk.Button(control_frame, text="Generate Array", command=generate_array)
generate_button.grid(row=1, column=0, padx=5, pady=5)

start_button = tk.Button(control_frame, text="Start Sorting", command=start_sorting)
start_button.grid(row=1, column=1, padx=5, pady=5)

pause_button = tk.Button(control_frame, text="Pause", command=pause_resume)
pause_button.grid(row=1, column=2, padx=5, pady=5)

stop_button = tk.Button(control_frame, text="Stop", command=stop_sorting)
stop_button.grid(row=1, column=3, padx=5, pady=5)

# ---------- Initial Array ----------
generate_array()

root.mainloop()