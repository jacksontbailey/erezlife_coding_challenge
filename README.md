# erezlife_coding_challenge

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

## Description

This Python project was created for a coding challenge at eRezLife.

### Table of Contents

1. [Authors](#authors)
2. [Installation](#installation)
3. [Functions](#functions)
4. [Classes](#classes)
5. [Environment Variables](#environment-variables)
6. [License](#license)

## Authors

- [@JacksonTBailey](https://www.github.com/JacksonTBailey)

## Installation

The project has several dependencies, which are listed in the `requirements.txt` file. Some of these packages are not used directly, but are required as dependencies for other packages. It is recommended to use a virtual environment (venv) to install these dependencies.

1. Clone the repository to your local machine.

2. Install the required packages listed in `requirements.txt` using `pip install -r requirements.txt`. Note that not all of these packages are used directly, some of them come with other packages that were installed.

3. Create a virtual environment for your project using your preferred method.

4. Create a `.env` file in the root directory of the project and add all of the variables found in the [Environment Variables](#environment-variables) section.


## Functions

The module contains the following functions:

- **`get_student_applications()`**: This function retrieves student information along with the number of applications each student has.
- **`generate_nested_structure()`**: Recursively generates a nested structure of HTML-like tags based on the given array of letters.
- **`process_shapes()`**: Reads shape data from the input CSV file, calculates the perimeter and area for each shape, and writes the results to the output CSV file.

## Classes

The module contains the following classes:

- **`QuestionHandler`**: The QuestionHandler class provides a menu-driven interface for handling different questions. It allows the user to select and execute specific questions related to database operations, HTML parsing, nested structure generation, and file processing.
- **`DatabaseConfig`**: Class representing the configuration settings for PostgreSQL database connection and table creation.
- **`Shape`**: Base class representing a geometric shape.
- **`Square(Shape)`**: Class representing a square shape derived from the Shape class.
- **`Circle(Shape)`**: Class representing a circle shape derived from the Shape class.
- **`Pentagon(Shape)`**: Class representing a pentagon shape derived from the Shape class.
- **`Triangle(Shape)`**: Class representing a triangle shape derived from the Shape class.
- **`HTMLParser`**: Class for parsing raw HTML strings and generating properly formatted output.
- **`DummyDataGenerator`**: Class for generating dummy student and application data.

## Usage

To use this module, you will need to download Postgres. You can download it by following the instructions on the [PostgreSQL Downloads](https://www.postgresql.org/download/).

Here's a step-by-step guide on how to use this module:

### Step 1: Install the Required Libraries

Ensure that you have the required libraries installed, namely psycopg2, python-dotenv, pyinputplus, and faker. For ease of use, I have included a requirements.txt file. You can view the instructions for this in the [Installation](#installation) section of this document.

### Step 2: Set Up Your Environment

- Create all of the required variables in the ".env" file in the project directory. Check out the [Environment Variables](#environment-variables) section for more details.

### Step 3: Run the Main File

Run the main.py file. This will initialize the program in the terminal where you will engage with the prompts.


That's it! With these steps, you can use this module to interact with the erezlife_coding_challenge.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `database_name`=your_database_name_here
- `database_user`=your_database_username_here
- `database_pass`=your_database_password_here
- `database_host`=your_database_host_address_here
- `database_port`=your_database_port_number_here

## License

MIT License

Copyright (c) 2023 Jackson Bailey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
