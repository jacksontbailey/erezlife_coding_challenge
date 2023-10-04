import csv
from core.challenges.question_4.shape_classes.circle import Circle
from core.challenges.question_4.shape_classes.pentagon import Pentagon
from core.challenges.question_4.shape_classes.square import Square
from core.challenges.question_4.shape_classes.triangle import Triangle

def process_shapes(input_filename, output_filename):
    """
    Reads shape data from the input CSV file, calculates the perimeter and area for each shape,
    and writes the results to the output CSV file.

    Args:
        input_filename (str): Path to the input CSV file containing shape data.
        output_filename (str): Path to the output CSV file where results will be written.

    Raises:
        FileNotFoundError: If the input CSV file is not found.
        Exception: For other unexpected errors during processing.
    """
    
    results = []
    try:
        with open(input_filename, 'r+') as file:
            for line in file:
                shape_data = line.strip().split(',')
                if shape_data[0] == 'triangle':
                    shape = Triangle(shape_data[1])
                elif shape_data[0] == 'square':
                    shape = Square(shape_data[1])
                elif shape_data[0] == 'pentagon':
                    shape = Pentagon(shape_data[1])
                elif shape_data[0] == 'circle':
                    shape = Circle(shape_data[1])
                else:
                    print(f"Error: Invalid shape '{shape_data[0]}' in the input file.")
                    continue
                
                perimeter = shape.calculate_perimeter()
                area = shape.calculate_area()
                results.append([shape.name, shape.side_length, perimeter, area])
                print(f"A {shape.name} with side length {shape.side_length} u has a perimeter of {perimeter:.2f} u and an area of {area:.2f} u^2")
        
        with open(output_filename, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Shape', 'Side Length', 'Perimeter', 'Area'])
            writer.writerows(results)
        print(f"Results written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Main function
if __name__ == "__main__":
    input_file = "shapes.csv"
    output_file = "output.csv"
    process_shapes(input_file, output_file)