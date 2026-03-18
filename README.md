# Hadwiger-Nelson Unit-Distance Solver

A computational framework for exploring the Hadwiger-Nelson problem, which seeks the minimum number of colors required to color the plane such that no two points at a unit distance share a color.

## Research Context
For decades, the lower bound for the chromatic number of the plane was 4. This project is based on the research by Geoffrey Exoo and Dan Ismailescu, whose paper "The Chromatic Number of the Plane is at Least 5: A New Proof" utilized computer-assisted methods to raise this bound.



## Technical Features

* **Graph Generation (`generate_xy.py`)**: 
    * Maps data into Cartesian coordinates $(x, y)$.
    * Constructs a unit-distance graph by connecting points exactly 1 unit apart.
* **Optimization Solver (`four_color_search.py`)**: 
    * Implements a Depth-First Search (DFS) to exhaustively check coloring combinations.
    * Employs Forward Checking to prune available color sets and identify conflicts early.
    * Validates results by ensuring no adjacent vertices share the same assignment.



## Requirements
* `Python 3.x`
* `NumPy`
* `NetworkX`
* `Matplotlib`

## Execution
To run the solver on the default graph configuration:
```bash
python four_color_search.py
