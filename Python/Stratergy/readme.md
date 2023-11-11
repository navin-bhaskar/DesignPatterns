# Introduction

![image](https://github.com/navin-bhaskar/DesignPatterns/assets/3251693/6014f828-c3b0-40fb-921a-df768e736277)

Implements startergy design pattern to visualize various approaches to solve the 'trapping rain water' probem found [here](https://leetcode.com/problems/trapping-rain-water/) and [here](https://www.geeksforgeeks.org/trapping-rain-water/).
The startegy pattern is used here to pick one of the following startegies to solve the problem

1. Brute force
2. Pre calculation
3. Pointer approach

The main app asks the user to select one of the sample inputs and desired startegy to solve the problem.
Once the selection is made, a 'SolutionsFactory' is used to instantiate the selected solution which all derive from
BaseStartegy which has solve() method to solve and visualize the problem.

```
                                  +--------------------------+
                                  |                          |
                                  |      BaseStratergy       |
                                  |                          |
                                  +--------------------------+
                                                ^
                                                |
                                                |
                                                |
              +---------------------------------|-------------------------------------+
              |                                 |                                     |
              |                                 |                                     |
              |                                 |                                     |
              |                                 |                                     |
+--------------------------+       +--------------------------+          +--------------------------+
|                          |       |                          |          |                          |
|   BruteForceStratergy    |       | PreCalculationStratergy  |          |     PointerStratergy     |
|                          |       |                          |          |                          |
+--------------------------+       +--------------------------+          +--------------------------+

```

# Usage

To run the application you need to install and 'coloroma' libraray

```
pip install colorama
```

Once installed, from this directory, run 'app.py' by typing following command

```
python app.py
```

Once the application starts, follow the on screen instructions to select and visualize one of the solution appraoches

# Demo


https://github.com/navin-bhaskar/DesignPatterns/assets/3251693/f9cc6ded-73c6-49d6-a3df-748304f0f76e.mp4



https://github.com/navin-bhaskar/DesignPatterns/assets/3251693/93bb3050-6065-4082-9d54-072a6ffd02af


