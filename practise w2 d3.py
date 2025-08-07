import tkinter as tk
from tkinter import messagebox

# Global variables to track the game state
current_player = "X"
board = [""] * 9  # Empty board with 9 positions
buttons = []  # List to store all button widgets
game_over = False

def create_window():
    """Create the main game window"""
    window = tk.Tk()
    window.title("Tic-Tac-Toe Game")
    window.geometry("400x550")
    window.resizable(False, False)
    return window

def check_winner():
    """Check if there's a winner or if the game is a tie"""
    global game_over

    # All possible winning combinations (rows, columns, diagonals)
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check for a winner
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            game_over = True
            messagebox.showinfo("Game Over", f"Player {board[combo[0]]} wins!")
            return True

    # Check for a tie (all positions filled)
    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a tie!")
        return True

    return False

def button_click(position):
    """Handle button clicks"""
    global current_player

    # If game is over or position is already taken, do nothing
    if game_over or board[position] != "":
        return

    # Place the current player's mark
    board[position] = current_player
    buttons[position].config(text=current_player, state="disabled")

    # Check if this move wins the game
    if not check_winner():
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"
        update_status_label()

def reset_game():
    """Reset the game to start over"""
    global current_player, board, game_over

    current_player = "X"
    board = [""] * 9
    game_over = False

    # Reset all buttons
    for button in buttons:
        button.config(text="", state="normal")

    update_status_label()

def update_status_label():
    """Update the status label to show current player"""
    status_label.config(text=f"Current Player: {current_player}")

def create_game_board(window):
    """Create the 3x3 grid of buttons"""
    global buttons

    # Create a frame for the game board
    board_frame = tk.Frame(window)
    board_frame.pack(pady=10)

    # Create 9 buttons in a 3x3 grid
    for i in range(9):
        row = i // 3  # Calculate row (0, 1, or 2)
        col = i % 3   # Calculate column (0, 1, or 2)

        button = tk.Button(
            board_frame,
            text="",
            width=6,
            height=3,
            font=("Arial", 20, "bold"),
            command=lambda pos=i: button_click(pos)
        )
        button.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(button)

def create_controls(window):
    """Create the control buttons and status label"""
    global status_label

    # Status label to show current player
    status_label = tk.Label(
        window,
        text=f"Current Player: {current_player}",
        font=("Arial", 12)
    )
    status_label.pack(pady=5)

    # Reset button
    reset_button = tk.Button(
        window,
        text="New Game",
        font=("Arial", 12),
        command=reset_game
    )
    reset_button.pack(pady=5)

def main():
    """Main function to start the game"""
    # Create the main window
    window = create_window()

    # Add a title label
    title_label = tk.Label(
        window,
        text="Tic-Tac-Toe",
        font=("Arial", 16, "bold")
    )
    title_label.pack(pady=10)

    # Create the game board
    create_game_board(window)

    # Create controls (status and reset button)
    create_controls(window)

    # Start the game loop
    window.mainloop()

# Run the game when the script is executed
if __name__ == "__main__":
    main()

