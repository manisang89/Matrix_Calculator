# Matrix Operations Streamlit App

## Overview
This is a simple **Streamlit** web application for performing basic matrix operations such as:
- Addition
- Subtraction
- Multiplication
- Scalar Multiplication
- Transpose
- Determinant
- Inverse

The application takes user inputs for matrix dimensions and values, then computes the selected operation and displays the result.

## Features
- **User-friendly UI**: Simple and interactive interface with dropdowns and input fields.
- **Real-time computation**: Perform operations instantly upon input.
- **Error handling**: Handles invalid input scenarios such as incorrect matrix dimensions.
- **Custom styling**: Enhanced UI with larger fonts and styled buttons.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:
```sh
pip install streamlit numpy
```

## Running the Application
To start the Streamlit app, run the following command in your terminal or command prompt:
```sh
streamlit run app.py
```
Replace `app.py` with the actual filename containing the code.

## Usage Instructions
1. Select an operation from the dropdown menu.
2. Enter the matrix dimensions and values as comma-separated numbers.
3. Click the **Calculate** button to compute the result.
4. The computed matrix is displayed on the screen.

## Error Handling
- If input dimensions do not match the required conditions, an error message is displayed.
- The inverse operation checks if the determinant is **zero** before computing the inverse.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **NumPy** (for matrix computations)

## Author
Developed by **Manikesh**

## License
This project is licensed under the MIT License.

