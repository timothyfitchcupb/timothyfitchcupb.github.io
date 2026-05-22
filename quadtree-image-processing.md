---
layout: project
title: Quadtree Image Processing
project_id: quadtree-image-processing
screenshot_note: These screenshots show the project being compiled, run, and tested from the command line.
screenshots:
  - src: images/quadtree-output.png
    alt: Quadtree project compile and test output
    caption: Fresh clone, compile commands, program output, and passing quadtree tests.
  - src: images/quadtree-code-running.png
    alt: Quadtree code running in terminal
    caption: Terminal run showing the quadtree executable and validation test results.
---

### Overview

This project implements a quadtree in C++ to process a small grayscale image represented as a two-dimensional array of intensity values. The quadtree recursively divides the image into four quadrants until each region is similar enough in color or the maximum depth is reached.

### What It Demonstrates

This project fits the portfolio well because it shows core computer science fundamentals outside of web development: recursive algorithms, tree-based data structures, dynamic memory management, class design, and test-driven validation of behavior.

### Project Snapshot

- Built for CSPB 2270 as a final data-structures project
- Represents an image as grayscale intensity values
- Uses recursive subdivision to model image regions as quadtree nodes
- Stops subdivision when a region is homogeneous enough based on a threshold
- Includes tests for root creation, subdivision, average color, leaf detection, and homogeneous-region behavior

### Core Implementation

The implementation centers on two classes:

- `QuadTreeNode`, which stores a region's position, size, average color, and four child pointers
- `QuadTree`, which owns the root node, recursively subdivides regions, calculates average colors, and checks whether a region is homogeneous

The destructor recursively deletes child nodes, which is important because the tree allocates nodes dynamically as regions subdivide.

### How to Run Locally

```bash
git clone https://github.com/timothyfitch/CSPB2270quadtrees.git
cd CSPB2270quadtrees
g++ -o quadtree Main.cpp QuadTree.cpp
g++ -o test QuadTree.cpp test.cpp
./quadtree
./test
```

### Future Improvements

- Add support for loading real image files instead of hard-coded grayscale arrays
- Generate visual before/after compression output
- Add command-line options for threshold and depth
- Track compression ratio and node count statistics
- Replace raw child pointers with safer ownership patterns
