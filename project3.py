# -------------------------------
# Global Variable (G in LEGB)
school_name = "ABC School"

# -------------------------------
# Function to show Local (L) and Nonlocal (E) variables
def student_info():
    # Local Variable (L)
    student_name = "Savitri"

    # Nested function to show Nonlocal (E)
    def inner():
        nonlocal student_name  # Nonlocal / Enclosing Variable
        student_name = "Kavita"
        print("Inside inner() -> Nonlocal Variable (E):", student_name)

    inner()
    print("Inside student_info() -> Local Variable (L):", student_name)

# -------------------------------
# Class to show Instance and Class variables
class Student:
    # Class Variable
    school = "XYZ School"  # shared by all objects

    def __init__(self, name, age, height, is_adult):
        # Instance Variables
        self.name = name          # str
        self.age = age            # int
        self.height = height      # float
        self.is_adult = is_adult  # bool
        self.subjects = ["Math", "English"]  # list
        self.grades = ("A", "B")             # tuple
        self.details = {"city":"Delhi"}      # dict
        self.unique_codes = {101, 102}      # set
        self.extra = None                    # NoneType

    def show(self):
        # Access Local variable inside method
        local_var = "I am local here"
        print("\nInside show() -> Local Variable (L):", local_var)
        print("Instance Variables:", self.name, self.age, self.height, self.is_adult)
        print("List:", self.subjects)
        print("Tuple:", self.grades)
        print("Dictionary:", self.details)
        print("Set:", self.unique_codes)
        print("NoneType:", self.extra)
        print("Class Variable:", Student.school)
        print("Global Variable:", school_name)
        print("Built-in Function Example (B): Length of subjects =", len(self.subjects))

# -------------------------------
# Call function to show Local & Nonlocal variables
student_info()

# -------------------------------
# Create object to show Instance & Class variables + Data types + LEGB
print("\n--- OOP & LEGB Example ---")
s1 = Student("Savitri", 24, 5.3, True)
s1.show()
