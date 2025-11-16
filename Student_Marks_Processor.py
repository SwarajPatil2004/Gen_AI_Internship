import numpy as np

# Input and output file names
input_file = "student_marks.txt"
output_file = "student_results.txt"

try:
    # Read student marks data from file
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                reg_num = parts[0]
                exam_mark = float(parts[1])
                coursework_mark = float(parts[2])
                data.append((reg_num, exam_mark, coursework_mark))
    
    if not data:
        print("Error: No data found in file.")
    else:
        # Create structured NumPy array
        dtype = [('reg_num', 'U20'), ('exam', 'f4'), ('coursework', 'f4'), 
                 ('overall', 'f4'), ('grade', 'U2')]
        students = np.zeros(len(data), dtype=dtype)
        
        # Compute overall marks and assign grades
        for i, (reg_num, exam, coursework) in enumerate(data):
            overall = exam * 0.6 + coursework * 0.4  # 60% exam, 40% coursework
            
            # Assign grade
            if overall >= 70:
                grade = 'A'
            elif overall >= 60:
                grade = 'B'
            elif overall >= 50:
                grade = 'C'
            elif overall >= 40:
                grade = 'D'
            else:
                grade = 'F'
            
            students[i] = (reg_num, exam, coursework, overall, grade)
        
        # Sort students by overall mark (descending)
        students = np.sort(students, order='overall')[::-1]
        
        # Write results to output file
        with open(output_file, 'w') as f:
            f.write("Reg_Number\tExam\tCoursework\tOverall\tGrade\n")
            for student in students:
                f.write(f"{student['reg_num']}\t{student['exam']:.2f}\t"
                       f"{student['coursework']:.2f}\t{student['overall']:.2f}\t"
                       f"{student['grade']}\n")
        
        print(f"Results written to {output_file}")
        
        # Display grade statistics
        print("\nGrade Statistics:")
        for grade in ['A', 'B', 'C', 'D', 'F']:
            count = np.sum(students['grade'] == grade)
            print(f"Grade {grade}: {count}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except ValueError:
    print("Error: Invalid data format in file.")
except Exception as e:
    print(f"Error: {e}")