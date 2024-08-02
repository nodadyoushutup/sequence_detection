# Sequence Pattern Analysis

## Overview

The Sequence Pattern Analysis program is a Python script designed to analyze a string sequence consisting of characters `A`, `B`, `C`, `a`, `b`, and `c`. It counts the occurrences of specified patterns within the sequence, calculates relevant statistics, and provides a user-friendly interface to interact with the script.

## Features

- **Pattern Counting:** The script identifies and counts the occurrences of specific patterns: `"ABC"`, `"abc"`, `"BCA"`, `"bca"`, `"CAB"`, `"cab"`, `"CBA"`, `"cba"`, `"ACB"`, `"acb"`, `"BAC"`, and `"bac"`.
- **Statistics Calculation:** It calculates and displays:
  - Total number of entries in the sequence.
  - Total possible alterations (length minus 2).
  - Total count of successful pattern alterations.
  - Percentage of successful alterations over total alterations.
- **Input Validation:** Ensures that the input sequence contains only valid characters.
- **User Interaction:** Allows users to input sequences and displays results continuously until the user decides to exit.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository or download the script file:
```bash
git clone <repository-url>
cd sequence_detection
```
    
### Usage

Run the script:
```bash
python sequence.py
```

Enter a sequence of characters consisting of `A`, `B`, `C`, `a`, `b`, and `c` when prompted:
```
Please enter the sequence: ABCabcCAB
```

The program will output the following statistics:
```
Total number of entries: 9
Total number of alterations: 7
Number of successful alterations: 2
Percentage of successful alterations: 28.57%
```

You can enter another sequence or type "no" to exit the program.

## Functions

### `count_subsequences(sequence: str) -> Dict[str, int]`

Counts the occurrences of each pattern in the sequence.

### `calculate_statistics(sequence: str, counts: Dict[str, int]) -> Dict[str, Union[int, float]]`

Calculates statistics based on the pattern counts in the sequence.

### `is_valid_sequence(sequence: str) -> bool`

Checks if the sequence contains only valid characters.

### `sanitize_sequence(sequence: str) -> str`

Removes spaces and commas from the sequence.

### `print_statistics(statistics: Dict[str, Union[int, float]]) -> None`

Prints the calculated statistics of the sequence.

### `main()`

Handles user input and program flow, prompting for sequences and displaying results.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
