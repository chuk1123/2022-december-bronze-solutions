# 🏆 USACO December 2022 Bronze Solutions

> My Python solutions for the USA Computing Olympiad (USACO) December 2022 Bronze Division contest

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![USACO](https://img.shields.io/badge/USACO-Bronze-cd7f32.svg)](http://www.usaco.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📖 About

This repository contains my solutions to all three problems from the [USACO December 2022 Bronze Division](http://www.usaco.org/index.php?page=dec22results) contest. All solutions are written in Python 3 and implement efficient algorithms tailored to each problem's constraints.

### What is USACO?

The **USA Computing Olympiad (USACO)** is a competitive programming competition for pre-college students. It features four divisions (Bronze, Silver, Gold, Platinum) and runs multiple contests throughout the academic year. The Bronze division focuses on fundamental algorithms, data structures, and problem-solving techniques.

## 🎯 Problems & Solutions

| Problem | Algorithm | Difficulty | Time Complexity | Solution |
|---------|-----------|------------|----------------|----------|
| [Problem 1: Cow College](#problem-1-cow-college) | Greedy + Sorting | ⭐⭐ | O(n log n) | [p1.py](p1.py) |
| [Problem 2: Feeding the Cows](#problem-2-feeding-the-cows) | Greedy Interval Coverage | ⭐⭐⭐ | O(n) | [p2.py](p2.py) |
| [Problem 3: Reverse Engineering](#problem-3-reverse-engineering) | Constraint Elimination | ⭐⭐⭐⭐ | O(N × M²) | [p3.py](p3.py) |

---

### Problem 1: Cow College

**📝 Problem Link**: [USACO December 2022 Bronze Problem 1](http://www.usaco.org/index.php?page=viewproblem2&cpid=1251)

#### Problem Summary

Farmer John wants to start a cow college and needs to determine the optimal tuition price. Each of N cows has a maximum amount they're willing to pay. If tuition is set at price P, all cows willing to pay at least P will enroll. Find the tuition that maximizes revenue and the maximum revenue possible.

#### Approach

**Algorithm**: Greedy with Sorting

1. Sort all willingness-to-pay values in descending order
2. For each unique price point, calculate potential revenue: `price × students_at_this_price`
3. Track the maximum revenue and corresponding optimal price
4. Output both values

**Why This Works**: By sorting in descending order, we can efficiently calculate how many cows would enroll at each price point. The optimal price must be one of the existing willingness-to-pay values.

#### Complexity
- **Time**: O(n log n) due to sorting
- **Space**: O(n) for storing sorted values

#### Key Insights
- The optimal price is always one of the input values (no benefit to choosing in-between prices)
- Greedy approach works because sorting allows us to efficiently count enrollment at each price

---

### Problem 2: Feeding the Cows

**📝 Problem Link**: [USACO December 2022 Bronze Problem 2](http://www.usaco.org/index.php?page=viewproblem2&cpid=1252)

#### Problem Summary

N cows are positioned along a 1D line, each needing either Guernsey (G) or Holstein (H) grass. Each cow can reach patches within K units. Determine the minimum number of grass patches needed to feed all cows and show one valid configuration.

#### Approach

**Algorithm**: Greedy Interval Coverage

1. Separate cows into two lists by breed (Holstein and Guernsey)
2. Process Guernsey cows first:
   - Place patches as far right as possible (position + K)
   - Skip cows already covered by previous patches
3. Process Holstein cows similarly, avoiding conflicts with G patches
4. Output total count and patch configuration

**Why This Works**: The greedy strategy of placing patches as far right as possible ensures maximum coverage for upcoming cows, minimizing total patches needed. Processing breeds separately prevents type conflicts.

#### Complexity
- **Time**: O(n) - single pass through cow positions
- **Space**: O(n) - storing positions and patch array

#### Key Insights
- Greedy placement (rightmost valid position) is optimal for interval coverage
- Separating by breed avoids complex conflict resolution
- Each patch can cover multiple cows of the same breed

---

### Problem 3: Reverse Engineering

**📝 Problem Link**: [USACO December 2022 Bronze Problem 3](http://www.usaco.org/index.php?page=viewproblem2&cpid=1253)

#### Problem Summary

Given M input-output examples where inputs are N-bit binary strings and outputs are binary (0 or 1), determine if a sequence of if/else statements examining single bits could produce these results. Detect contradictions or confirm feasibility.

#### Approach

**Algorithm**: Constraint Satisfaction with Elimination

1. **Detect obvious contradictions**: Same input producing different outputs → "LIE"
2. **Iteratively eliminate consistent variables**:
   - For each bit position, test if fixing it to 0 or 1 creates consistency
   - Check if all inputs with that bit value map to the same output
   - Remove those inputs from further consideration
3. **Final check**:
   - If all inputs eliminated → "OK" (program exists)
   - Otherwise → "LIE" (contradictory requirements)

**Why This Works**: A valid program can be constructed if and only if we can iteratively eliminate all inputs by finding bits that partition inputs into consistent groups. If we get stuck with contradictory examples, no program exists.

#### Complexity
- **Time**: O(N × M²) - N bits, M examples, checking consistency
- **Space**: O(M) - storing input-output mappings

#### Key Insights
- Early contradiction detection saves computation
- Greedy elimination works: any valid elimination order leads to same result
- Empty mapping set indicates all examples can be satisfied

---

## 🚀 Usage

### Prerequisites

- Python 3.8 or higher
- No external libraries required (uses only Python standard library)

### Running Solutions

Each solution reads from standard input and writes to standard output, following USACO conventions.

#### Running Locally

```bash
# Problem 1: Cow College
python3 p1.py < input1.txt

# Problem 2: Feeding the Cows
python3 p2.py < input2.txt

# Problem 3: Reverse Engineering
python3 p3.py < input3.txt
```

#### Interactive Testing

You can also run solutions interactively and type input manually:

```bash
python3 p1.py
# Then type your input and press Ctrl+D (Unix) or Ctrl+Z (Windows) when done
```

### Input Format

Refer to the official USACO problem statements (linked above) for detailed input specifications. Each problem follows standard competitive programming I/O format.

## 📁 Repository Structure

```
2022-december-bronze-solutions/
├── p1.py                      # Problem 1: Cow College
├── p2.py                      # Problem 2: Feeding the Cows
├── p3.py                      # Problem 3: Reverse Engineering
├── README.md                  # This file
├── LICENSE                    # MIT License
└── Community files/
    ├── CONTRIBUTING.md        # Contributing guidelines
    ├── CODE_OF_CONDUCT.md     # Code of conduct
    ├── ISSUE_TEMPLATE.md      # Issue template
    └── PULL_REQUEST_TEMPLATE.md  # PR template
```

## 💡 Learning Resources

If you're preparing for USACO or competitive programming, check out these resources:

- **[USACO Guide](https://usaco.guide/)** - Comprehensive training resource with curated problems
- **[USACO Training Pages](https://train.usaco.org/)** - Official training platform
- **[Competitive Programmer's Handbook](https://cses.fi/book/book.pdf)** - Free algorithms textbook
- **[USACO Bronze Guide](https://usaco.guide/bronze)** - Bronze-specific problem solving techniques

### Key Bronze Division Topics

- Simulation
- Sorting
- Greedy Algorithms
- Set and Map Data Structures
- Ad Hoc Problem Solving

## 🤝 Contributing

While these are personal contest solutions, suggestions for improvements are welcome! If you have:
- More efficient algorithms
- Clearer code explanations
- Found bugs or edge cases
- Alternative solution approaches

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **USACO** for providing high-quality competitive programming problems
- **Kevin Chu** ([chuk1123](https://github.com/chuk1123)) - Solutions author
- The competitive programming community for techniques and insights

## 📮 About the Author

These solutions were created by Kevin Chu as part of USACO contest participation. Check out my other competitive programming solutions:

- [2023 January Silver Solutions](https://github.com/chuk1123/2023-Janurary-Silver-Solutions) (C++)

---

**Happy Coding!** 🐮💻

*If you found these solutions helpful, consider starring this repository!*
