import tkinter as tk

class Visualizer:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height

    def draw_array(self, arr, colors=None):
        self.canvas.delete("all")
        if len(arr) == 0:
            return
        bar_width = self.width / len(arr)
        max_value = max(arr)
        for i, value in enumerate(arr):
            scaled_height = (value / max_value) * (self.height - 20)
            x0 = i * bar_width
            y0 = self.height - scaled_height
            x1 = (i + 1) * bar_width
            y1 = self.height
            color = colors[i] if colors else "skyblue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.update_idletasks()