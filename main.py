import sys
from gator_leaderboard_system import process_input, write_to_output

if __name__ == "__main__":
    input_filename = sys.argv[1]
    process_input(input_filename)
    write_to_output(input_filename)