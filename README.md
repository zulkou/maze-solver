# Maze Solver
## Description
A maze generator one packed with its solver. Both is using DFS algorithm. This project is one of the guided project in [boot.dev](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271).

## How to Use This Project
Run shell below to download the project:
```bash
git clone https://github.com/zulkou/maze-solver.git
cd maze-solver
```
Make sure you already have tkinter installed, if not, run `pip install tk`.
### Customization
You can customize where the maze start, number of rows and columns, and also the size of the cells. You just need to edit the `maze` variable in the `main()` function with this format:
```py
Maze(start_x, start_y, num_rows, num_cols, size_cell_x, size_cell_y, win)
```
## How to Play The Game
To run it, run this shell command in `maze-solver` directory:
```
python3 -m main
```
Enjoy the maze creation!
