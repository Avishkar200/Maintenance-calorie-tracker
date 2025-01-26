import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_calories():
    try:
        age = int(age_entry.get())
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        activity_level = activity_var.get()

        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        if activity_level == "Sedentary":
            calories = bmr * 1.2
        elif activity_level == "Lightly active":
            calories = bmr * 1.375
        elif activity_level == "Moderately active":
            calories = bmr * 1.55
        elif activity_level == "Very active":
            calories = bmr * 1.725
        else:
            calories = bmr * 1.9

        result_label.config(text=f"Daily Calorie Needs: {calories:.2f} kcal")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for age, weight, and height.")

# Create the main window
root = tk.Tk()
root.title("Calorie Counter")
root.geometry("400x550")
root.configure(bg="#f0f8ff")

# Add a heading at the very top
heading_label = tk.Label(root, text="Calorie Counter", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#0078d7")
heading_label.pack(pady=10)  # Add spacing below the heading

# Create a frame for centering the rest of the content
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(expand=True)

# Create a style
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f8ff", foreground="#333")
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), background="#4caf50", foreground="#fff")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TRadiobutton", font=("Arial", 12), background="#f0f8ff")
style.configure("TOptionMenu", font=("Arial", 12), background="#fff")

# Create labels and input fields
age_label = ttk.Label(frame, text="Age:")
age_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
age_entry = ttk.Entry(frame)
age_entry.grid(row=0, column=1, padx=10, pady=10)

gender_label = ttk.Label(frame, text="Gender:")
gender_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
gender_var = tk.StringVar(value="Male")
male_radio = ttk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
female_radio = ttk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=1, column=2, padx=10, pady=5, sticky="w")

weight_label = ttk.Label(frame, text="Weight (kg):")
weight_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
weight_entry = ttk.Entry(frame)
weight_entry.grid(row=2, column=1, padx=10, pady=10)

height_label = ttk.Label(frame, text="Height (cm):")
height_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
height_entry = ttk.Entry(frame)
height_entry.grid(row=3, column=1, padx=10, pady=10)

activity_label = ttk.Label(frame, text="Activity Level:")
activity_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
activity_var = tk.StringVar(value="Sedentary")
activity_menu = ttk.OptionMenu(frame, activity_var, "Sedentary", "Lightly active", "Moderately active", "Very active", "Super active")
activity_menu.grid(row=4, column=1, padx=10, pady=10)

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate", command=calculate_calories)
calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

# Result label
result_label = ttk.Label(frame, text="", font=("Arial", 14, "bold"), foreground="#0078d7", background="#f0f8ff")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
