import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "matrix.txt")
#file_path = os.path.join(script_dir, "another_matrix.txt")

class SolveMatrix:
    def __init__(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.matrix = [list(line.strip()) for line in f if line.strip()] # Convert to 2D list
            # The if line.strip() condition ensures that empty lines are skipped.
    def display_matrix(self):
        for row in self.matrix:
            print(row)


    def decrypt_matrix(self):
        solution = ''

        num_cols = max(len(row) for row in self.matrix)  # Find longest row

        for col in range(num_cols):
            for row in range(len(self.matrix)):
                if col < len(self.matrix[row]):
                    char = self.matrix[row][col]
                    solution += char
        solution = re.sub(r'[^a-zA-Z]+', ' ', solution).strip() # regex
        
        return solution

        

my_matrix = SolveMatrix(file_path)
my_matrix.display_matrix() # list of lists
                           # my_matrix.matrix[row][col]
print(my_matrix.decrypt_matrix())

