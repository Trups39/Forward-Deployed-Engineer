# Forward-Deployed-Engineer
FDE Technical Screen
# Package Sorter

This repository contains the implementation of a package sorting system that classifies packages based on their volume, mass, and dimensions. The sorting system helps in categorizing packages into one of three stacks: **STANDARD**, **SPECIAL**, or **REJECTED**.

## Features
- Classifies packages based on the following criteria:
  - **Bulky**: A package is considered bulky if its volume is greater than or equal to 1,000,000 cm³ or one of its dimensions is greater than or equal to 150 cm.
  - **Heavy**: A package is considered heavy if its mass is greater than or equal to 20 kg.
  - **Stacks**:
    - **STANDARD**: Standard packages (not bulky or heavy).
    - **SPECIAL**: Bulky or heavy packages.
    - **REJECTED**: Packages that are both bulky and heavy.

## Files
- `sort.py`: Contains the main sorting logic.
- `strategies.py`: Defines the strategies for classifying packages.
- `test_sort.py`: Includes test cases to verify the sorting logic.

## Requirements
No external dependencies required.

## Usage

You can run the sorting function by calling `sort()` with the width, height, length, and mass of the package.

Example:
```python
from sort import sort

result = sort(200, 200, 50, 15)
print(result)  # Output: SPECIAL
