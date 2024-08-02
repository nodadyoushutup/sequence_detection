import re
from typing import Dict, Union

PATTERNS = [
    "ABC", "abc", 
    "BCA", "bca", 
    "CAB", "cab", 
    "CBA", "cba", 
    "ACB", "acb", 
    "BAC", "bac"
]

def count_subsequences(sequence: str) -> Dict[str, int]:
    """
    Count occurrences of each pattern in the sequence.

    Args:
        sequence (str): The input string sequence consisting of the characters A, B, C, a, b, c.

    Returns:
        Dict[str, int]: A dictionary where keys are patterns and values are their counts in the sequence.
    """
    
    return {pattern: sequence.count(pattern) for pattern in PATTERNS}

def calculate_statistics(sequence: str, counts: Dict[str, int]) -> Dict[str, Union[int, float]]:
    """
    Calculate total entries, alterations, and percentage of successful alterations.

    Args:
        sequence (str): The input string sequence consisting of the characters A, B, C, a, b, c.
        counts (Dict[str, int]): A dictionary containing counts of each pattern in the sequence.

    Returns:
        Dict[str, Union[int, float]]: A dictionary containing statistics:
            - total_entries (int): Total length of the sequence.
            - total_alterations (int): Total possible alterations (length minus 2).
            - successful_alterations (int): Total count of successful pattern alterations.
            - percentage_successful (float): Percentage of successful alterations over total alterations.
    """
    
    total_entries = len(sequence)
    successful_alterations = sum(counts.values())
    total_alterations = max(0, total_entries - 2)  # Ensure non-negative
    percentage_successful = (successful_alterations / total_alterations) * 100 if total_alterations > 0 else 0
    return {
        "total_entries": total_entries,
        "total_alterations": total_alterations,
        "successful_alterations": successful_alterations,
        "percentage_successful": percentage_successful
    }

def is_valid_sequence(sequence: str) -> bool:
    """
    Check if the sequence contains only valid characters (A, B, C, a, b, c).

    Args:
        sequence (str): The input string sequence to validate.

    Returns:
        bool: True if the sequence is valid, False otherwise.
    """

    return bool(re.fullmatch(r'[ABCabc]*', sequence))

def sanitize_sequence(sequence: str) -> str:
    """
    Remove spaces and commas from the sequence.

    Args:
        sequence (str): The input string sequence to sanitize.

    Returns:
        str: The sanitized sequence without spaces or commas.
    """

    return sequence.replace(" ", "").replace(",", "")

def print_statistics(statistics: Dict[str, Union[int, float]]) -> None:
    """
    Print the calculated statistics of the sequence.

    Args:
        statistics (Dict[str, Union[int, float]]): A dictionary containing the calculated statistics.
    """
    
    print(f"Total number of entries: {statistics.get('total_entries')}")
    print(f"Total number of alterations: {statistics.get('total_alterations')}")
    print(f"Number of successful alterations: {statistics.get('successful_alterations')}")
    print(f"Percentage of successful alterations: {statistics.get('percentage_successful'):.2f}%")

def main():
    while True:
        try:
            # sequence = input("Please enter the sequence: ")
            sequence = "ABCABCBCABCACBACCCAB"
            sequence = sanitize_sequence(sequence)
            if not is_valid_sequence(sequence):
                print("Invalid sequence. Please try again using only valid sequence characters (ex: ABCabc)")
                continue
            print_statistics(
                calculate_statistics(
                    sequence, count_subsequences(sequence)
                )
            )
            welcome = input("Press the enter key if you want to enter another sequence, or type 'no' to exit: ")
            if welcome.strip().lower() == "no":
                print("Exiting the program. Goodbye!")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully.")
            break

if __name__ == "__main__":
    main()