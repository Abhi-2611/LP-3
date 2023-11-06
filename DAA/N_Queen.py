import time

def solve_n_queens(board_size):
    def is_safe(row, col, queens):
        # Check if it's safe to place a queen at a given position (row, col)
        for r, c in queens:
            if col == c or abs(row - r) == abs(col - c):
                return False
        return True

    def print_solution(queens):
        # Display the N-Queens solution
        for row in range(board_size):
            row_str = ""
            for col in range(board_size):
                if (row, col) in queens:
                    row_str += "Q "
                else:
                    row_str += ". "
            print(row_str)
        print("\n")

    def backtrack(row, queens):
        if row == board_size:
            # All queens are placed, print the solution
            print_solution(queens)
        else:
            for col in range(board_size):
                if is_safe(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens)
                    queens.pop()

    queens = []  # List to store the positions of queens

    if board_size < 1:
        print("No valid board size provided.")
    elif board_size == 1:
        # Special case for board size 1 (trivial solution)
        queens.append((0, 0))
        print_solution(queens)
    elif board_size < 4:
        print(f"No solution exists for board size {board_size}.")
    else:
        start_time = time.time()
        backtrack(0, queens)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time to find solutions: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    board_size = int(input("Enter the board size : "))
    solve_n_queens(board_size)