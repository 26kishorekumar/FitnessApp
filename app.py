import tkinter as tk
from tkinter import messagebox

class FitnessTrackerApp:
    """
    A simple GUI application for tracking fitness workouts using Tkinter.
    """
    def __init__(self, master):
        """Initializes the application UI and state."""
        self.master = master
        master.title("ACEestFitness and Gym")

        self.workouts = []

        # --- UI Elements ---
        # Labels and Entries for adding workouts
        self.workout_label = tk.Label(master, text="Workout:")
        self.workout_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.workout_entry = tk.Entry(master)
        self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

        self.duration_label = tk.Label(master, text="Duration (minutes):")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.duration_entry = tk.Entry(master)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(master, text="Add Workout", command=self.handle_add_workout)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Workouts", command=self.handle_view_workouts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_workout_logic(self, workout, duration_str):
        """
        Handles the core logic for adding a workout.
        This is separated from the GUI for testability.
        Returns a tuple (status, message).
        """
        if not workout or not duration_str:
            return ("error", "Please enter both workout and duration.")

        try:
            duration = int(duration_str)
            if duration <= 0:
                return ("error", "Duration must be a positive number.")
            self.workouts.append({"workout": workout, "duration": duration})
            return ("success", f"'{workout}' added successfully!")
        except ValueError:
            return ("error", "Duration must be a number.")

    def handle_add_workout(self):
        """
        Gets data from entry fields and uses the logic function
        to process it, then shows a message box.
        """
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

        status, message = self.add_workout_logic(workout, duration_str)

        if status == "success":
            messagebox.showinfo("Success", message)
            self.workout_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", message)

    def get_workout_summary(self):
        """
        Returns a formatted string of all logged workouts.
        Separated from GUI for testability.
        """
        if not self.workouts:
            return "No workouts logged yet."

        workout_list = "Logged Workouts:\n"
        for i, entry in enumerate(self.workouts):
            workout_list += f"{i+1}. {entry['workout']} - {entry['duration']} minutes\n"
        return workout_list.strip()

    def handle_view_workouts(self):
        """
        Gets the workout summary and displays it in a message box.
        """
        summary = self.get_workout_summary()
        messagebox.showinfo("Workouts", summary)


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
