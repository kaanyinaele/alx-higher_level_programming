# Python Exception Handling Project

## Description
This project focuses on implementing various functionalities using Python, specifically handling exceptions. The tasks cover safe list printing, safe printing of integers, printing and counting integers in a list, performing integer division with debug information, dividing two lists element-wise, raising type and name exceptions, and more.

## Project Structure
The project includes multiple Python scripts, each addressing a specific task. Below is an overview of the key components:

1. **safe_print_list.py**
   - Functionality: Prints the first x elements of a list safely.
   - Usage: 12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5

2. **safe_print_integer.py**
   - Functionality: Prints an integer using {:d}.format() and returns True if successful, False otherwise.
   - Usage: 89
-89
School is not an integer

3. **safe_print_list_integers.py**
   - Functionality: Prints the first x integers in a list and returns the real number of integers printed.
   - Usage: 12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5

4. **safe_print_division.py**
   - Functionality: Divides two integers, prints the result, and handles exceptions.
   - Usage: Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None

5. **list_division.py**
   - Functionality: Divides element by element two lists and returns a new list with division results.
   - Usage: [5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]

6. **raise_exception.py**
   - Functionality: Raises a type exception.
   - Usage: Exception raised

7. **raise_exception_msg.py**
   - Functionality: Raises a name exception with a provided message.
   - Usage: C is fun

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Files should end with a new line
- README.md file at the root of the project folder is mandatory
- Code should follow Pycodestyle (version 2.8.*)
- All files must be executable

## How to Use
1. Clone the repository to your local machine.
2. Navigate to the project folder.
3. Make the Python scripts executable using the command .
4. Run the scripts as .

## Testing
Each script includes a test section that demonstrates the functionality. Execute the provided test scripts (e.g., , , etc.) to verify the correct implementation.

## Author
https://github.com/kaanyinaele

