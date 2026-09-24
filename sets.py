python_students = {"Rajesh", "Arun", "Kumar", "Priya"}
java_students = {"Arun", "Vijay", "Kumar", "Meena"}

all_students = python_students | java_students
both_courses = python_students & java_students
python_only = python_students - java_students
java_only = java_students - python_students

print(all_students)
print(both_courses)
print(python_only)
print(java_only)
