"""
USACO December 2022 Bronze - Problem 3: Reverse Engineering
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1253

Problem Summary:
Given M input-output examples (N-bit binary inputs → binary outputs),
determine if a sequence of if/else statements examining single variables
could produce these results. Output "OK" if possible, "LIE" if contradictory.

Algorithm: Constraint Satisfaction with Variable Elimination
- Detect immediate contradictions (same input → different outputs)
- Iteratively eliminate variables that create consistent partitions
- If all examples can be eliminated, a valid program exists

Time Complexity: O(N × M²)
Space Complexity: O(M)

Author: Kevin Chu (chuk1123)
"""

def solve():
    # Read N (number of bits) and M (number of examples)
    N, M = map(int, input().split())

    # Store input-output mappings
    # Key: binary string input, Value: expected output (0 or 1)
    io_mapping = {}

    # Flag for detecting contradictions
    has_contradiction = False

    # Read all input-output examples
    for _ in range(M):
        binary_input, output = input().split()
        output = int(output)

        # Check for immediate contradiction: same input → different outputs
        if binary_input in io_mapping and io_mapping[binary_input] != output:
            has_contradiction = True
        else:
            io_mapping[binary_input] = output

    # If we found a contradiction, no valid program exists
    if has_contradiction:
        print("LIE")
        return

    # Flag to track if a valid program can be constructed
    can_construct_program = False

    # Iteratively try to eliminate examples by finding consistent variables
    while True:
        # If we've eliminated all examples, program is valid
        if len(io_mapping) <= 1:
            can_construct_program = True
            break

        # Track if we made progress in this iteration
        made_progress = False

        # Try each bit position as a potential if-statement condition
        for bit_index in range(N):
            # Check if setting this bit to 1 creates a consistent group
            can_use_bit_equals_1 = True
            can_use_bit_equals_0 = True

            # Track mappings for each bit value
            bit1_mappings = {}  # Inputs where bit_index == '1'
            bit0_mappings = {}  # Inputs where bit_index == '0'

            # Lists of examples that would be eliminated
            eliminate_if_1 = []
            eliminate_if_0 = []

            # Analyze all remaining examples
            for binary_str in io_mapping:
                bit_value = binary_str[bit_index]
                expected_output = io_mapping[binary_str]

                # Group by bit value at this position
                if bit_value == "1":
                    # Check consistency: all inputs with bit=1 should map to same output
                    if bit_value in bit1_mappings and bit1_mappings[bit_value] != expected_output:
                        can_use_bit_equals_1 = False
                    else:
                        bit1_mappings[bit_value] = expected_output
                        eliminate_if_1.append(binary_str)

                elif bit_value == "0":
                    # Check consistency: all inputs with bit=0 should map to same output
                    if bit_value in bit0_mappings and bit0_mappings[bit_value] != expected_output:
                        can_use_bit_equals_0 = False
                    else:
                        bit0_mappings[bit_value] = expected_output
                        eliminate_if_0.append(binary_str)

            # Eliminate examples if using bit=1 creates consistency
            if can_use_bit_equals_1:
                for example in eliminate_if_1:
                    del io_mapping[example]

            # Eliminate examples if using bit=0 creates consistency
            if can_use_bit_equals_0:
                for example in eliminate_if_0:
                    del io_mapping[example]

            # Check if we made progress (eliminated at least one example)
            if (can_use_bit_equals_1 and len(bit1_mappings) > 0) or \
               (can_use_bit_equals_0 and len(bit0_mappings) > 0):
                made_progress = True
                break  # Move to next iteration

        # If we couldn't eliminate anything, we're stuck
        if not made_progress:
            break

    # Output result
    if can_construct_program:
        print("OK")
    else:
        print("LIE")


# Handle multiple test cases
T = int(input())

for _ in range(T):
    # Note: There's a blank line before each test case in the input
    blank_line = input()
    solve()
