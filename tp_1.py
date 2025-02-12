import csv
import os
import msvcrt  # For detecting any key press on Windows

def load_csv_data(filename):
    """Load data from a CSV file. Return None if the file doesn't exist."""
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_csv_data(filename, data):
    """Save data to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Name', 'ID', 'Grade']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def press_any_key_to_exit():
    """Wait for any key press to exit the program."""
    print("\nPress any key to exit...")
    msvcrt.getch()  # Wait for a key press
    exit()  # Immediately terminate the program

def main():
    """Main program to manage student grades."""
    filename = "students.csv"

    # Check for the file's existence
    while not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        user_input = input("Press Enter to exit or create the file and type 'continue' to proceed: ").strip().lower()
        if user_input == "":
            press_any_key_to_exit()

    # Load data from the file
    data = load_csv_data(filename)

    while True:
        print("\nStudent Grade Management System")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Save and exit")
        print("Type 'exit' to quit without saving.")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'exit':
            press_any_key_to_exit()
        elif choice == '1':
            # Add a new student
            try:
                name = input("Enter student name: ").strip()
                student_id = input("Enter student ID: ").strip()

                # Check for duplicate ID
                if any(student['ID'] == student_id for student in data):
                    print("Error: Student ID already exists.")
                    continue

                grade = float(input("Enter student grade: "))
                data.append({'Name': name, 'ID': student_id, 'Grade': grade})
                print("Student added successfully!")
            except ValueError:
                print("Error: Grade must be a number.")
        elif choice == '2':
            # View all students
            if not data:
                print("No student data available.")
            else:
                print("\nStudent Records:")
                print("Name\tID\tGrade")
                for student in data:
                    print(f"{student['Name']}\t{student['ID']}\t{student['Grade']}")
        elif choice == '3':
            # Search for a student
            student_id = input("Enter student ID to search: ").strip()
            for student in data:
                if student['ID'] == student_id:
                    print(f"Found: Name: {student['Name']}, Grade: {student['Grade']}")
                    break
            else:
                print("Student not found.")
        elif choice == '4':
            # Save and exit
            save_csv_data(filename, data)
            press_any_key_to_exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()