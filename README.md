# Package Sorting System

This Python script is designed to automate the sorting of packages in Thoughtful's robotic automation factory. It classifies packages into different stacks: STANDARD, SPECIAL, and REJECTED, based on their volume and mass.

## Objective

To streamline the dispatch process of packages by automatically determining the appropriate stack for each package using predefined criteria for bulkiness and weight.

## Getting Started

These instructions will get you  project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x

Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing

Clone this repository to your local machine to get started.

```
git clone https://github.com/dsaakash/Package-Sorting-System.git
```

Navigate to the cloned directory.

```
cd path_to_cloned_repo
```

### Usage

The script can be run from the command line or integrated into a larger Python project. To run the script from the command line:

1. Open a terminal.
2. Navigate to the project directory.
3. Run the script using Python.

Example:

```
python sort_package.py
```

You can also import the `sort_package` function into another Python script and use it as part of a larger system.

```python
from sort_package import sort_package

# Example package sorting
print(sort_package(120, 80, 60, 22))  # Output will be the stack classification
```

## Functionality

The script defines a function `sort_package(width, height, length, mass)` that classifies packages based on their dimensions (in centimeters) and mass (in kilograms).

- **Parameters**:
  - `width`: Width of the package in cm.
  - `height`: Height of the package in cm.
  - `length`: Length of the package in cm.
  - `mass`: Mass of the package in kg.

- **Returns**: A string indicating the stack where the package should be placed ("STANDARD", "SPECIAL", "REJECTED").

## Testing

The script includes a simple test suite at the bottom. To add more tests, simply call the `sort_package` function with different parameters and print the result to verify correct behavior.




## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


