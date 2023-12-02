"""Moduel to run the daily challenges. 
Exectue with: `python .\bootstrap.py <day>`. 
"""

import sys
import os
import runpy


def run_solution(day):
    # Format the day string to match the folder naming convention
    day_formatted = f"day_{int(day):02d}"  # Converts '1' to '01', '10' to '10', etc.

    # Path to the directory containing bootstrap.py
    bootstrap_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the sol.py file
    solution_path = os.path.join(bootstrap_dir, day_formatted, "sol.py")

    # Check if the file exists before attempting to run it
    if not os.path.isfile(solution_path):
        print(f"Solution file for day {day} does not exist.")
        return

    # Execute the sol.py script
    runpy.run_path(solution_path, run_name="__main__")


if __name__ == "__main__":
    # Expect the day to be passed as an argument
    if len(sys.argv) != 2:
        print("Usage: python bootstrap.py <day>")
        sys.exit(1)

    run_solution(sys.argv[1])
