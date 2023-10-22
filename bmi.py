import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()

    bmi = weight / (height * height)
    result_label.config(text=f'Your BMI: {bmi:.2f}')

    category, recommendation = get_bmi_category(bmi, age, gender)
    category_label.config(text=f'Category: {category}')
    recommendation_label.config(text=recommendation)

    add_data_to_graph(age, bmi)

def get_bmi_category(bmi, age, gender):
    if age < 18:
        return "BMI for children and teenagers", "Please consult a pediatrician."
    elif gender == "Male" and age >= 18:
        if bmi < 18.5:
            return "Underweight", "You may need to gain some weight."
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight", "Your weight is in a healthy range."
        elif 25 <= bmi < 29.9:
            return "Overweight", "You may need to lose some weight."
        else:
            return "Obese", "You are at risk."
    elif gender == "Female" and age >= 18:
        if bmi < 17.5:
            return "Underweight", "You may need to gain some weight."
        elif 17.5 <= bmi < 23.9:
            return "Normal Weight", "Your weight is in a healthy range."
        elif 24 <= bmi < 28.9:
            return "Overweight", "You may need to lose some weight."
        else:
            return "Obese", "You are at risk."
    else:
        return "Category Not Found", "Please consult a healthcare professional."

def add_data_to_graph(age, bmi):
    ages.append(age)
    bmis.append(bmi)

    ax.clear()
    ax.plot(ages, bmis, marker='o', linestyle='-')
    ax.set_xlabel('Age')
    ax.set_ylabel('BMI')
    ax.set_title('BMI Over Time')
    canvas.draw()

def close_window():
    window.destroy()

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("500x750")
window.resizable(False, False)

input_frame = tk.Frame(window)
input_frame.pack(pady=20)

tk.Label(input_frame, text="Height (m):").grid(row=0, column=0, padx=10, pady=5)
height_entry = tk.Entry(input_frame)
height_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(input_frame)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Age:").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(input_frame)
age_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("Male")
gender_option_menu = ttk.Combobox(input_frame, textvariable=gender_var, values=["Male", "Female"])
gender_option_menu.grid(row=3, column=1, padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, bg="blue", fg="white")
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Bahnschrift", 16))
result_label.pack()

category_label = tk.Label(window, text="", font=("Bahnschrift", 14))
category_label.pack()

recommendation_label = tk.Label(window, text="", font=("Bahnschrift", 12))
recommendation_label.pack()

graph_frame = tk.Frame(window)
graph_frame.pack(pady=20)

ages, bmis = [], []
fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack()

close_button = tk.Button(window, text="Close", command=close_window, bg="red", fg="white")
close_button.pack(pady=10)

window.mainloop()
