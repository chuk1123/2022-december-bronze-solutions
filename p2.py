"""
USACO December 2022 Bronze - Problem 2: Feeding the Cows
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1252

Problem Summary:
N cows are positioned along a 1D line, each needing either Guernsey (G)
or Holstein (H) grass. Each cow can reach patches within K positions.
Find the minimum number of grass patches needed and show a valid configuration.

Algorithm: Greedy Interval Coverage
- Separate cows by breed type
- Process each breed with greedy placement (rightmost valid position)
- Avoid conflicts between different grass types

Time Complexity: O(n)
Space Complexity: O(n)

Author: Kevin Chu (chuk1123)
"""

def solve():
    # Read N (number of positions) and K (reach distance)
    N, K = map(int, input().split())

    # Read cow positions as a list of characters
    cows = [*input()]

    # Separate cow positions by breed
    holsteins = []  # H cow positions
    guernseys = []  # G cow positions

    # Initialize answer array with empty positions
    patch_config = ["." for i in range(N)]

    # Categorize cows by breed
    for i in range(len(cows)):
        cow = cows[i]
        if cow == "H":
            holsteins.append(i)
        else:
            guernseys.append(i)

    # Track rightmost patch position and patch count
    prev_patch_pos = -1
    patch_count = 0

    # Process Guernsey cows first with greedy placement
    for cow_pos in guernseys:
        # If this is the first cow
        if prev_patch_pos == -1:
            # Place patch as far right as possible (cow_pos + K)
            patch_pos = min(cow_pos + K, N - 1)
            patch_config[patch_pos] = "G"
            prev_patch_pos = cow_pos + K
            patch_count += 1
            continue

        # Check if current cow is already covered by previous patch
        # A cow at position cow_pos can reach patches within K distance
        if cow_pos - K <= prev_patch_pos:
            continue  # Already covered, skip
        else:
            # Need new patch - place as far right as possible
            patch_pos = min(cow_pos + K, N - 1)
            patch_config[patch_pos] = "G"
            prev_patch_pos = cow_pos + K
            patch_count += 1

    # Reset for Holstein processing
    prev_patch_pos = -1

    # Process Holstein cows with greedy placement
    for cow_pos in holsteins:
        # Check if already covered by previous H patch
        if cow_pos - K <= prev_patch_pos and prev_patch_pos != -1:
            continue

        # Calculate ideal patch position
        ideal_pos = min(cow_pos + K, N - 1)

        # Handle conflict: if a G patch is already at ideal position
        if patch_config[ideal_pos] == "G":
            # Place H patch one position to the left
            patch_config[ideal_pos - 1] = "H"

        # Place H patch at ideal position
        patch_config[ideal_pos] = "H"
        prev_patch_pos = cow_pos + K
        patch_count += 1

    # Output: total patches and configuration
    print(patch_count)
    print(*patch_config, sep="")


# Handle multiple test cases
T = int(input())
for _ in range(T):
    solve()
