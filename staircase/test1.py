import json

# Step 1: Initialize seating model
seating_model = {
    "Gold": {
        "A": {"A": [True, True, "S", True], "B": [True, "S", True, True]},
        "B": {"A": [True, True, True, True], "B": [True, True, "S", True]},
    },
    "Silver": {
        "A": {"A": [True, True, True, True], "B": [True, "S", True, True]},
    },
    "Bronze": {
        "A": {"A": [True, True, True, True], "B": [True, True, "S", True]},
    },
}

# Step 2: Define the seat selection function
def select_seat(seating_model, category, section, row, seat_num):
    # Validate the input
    if category not in seating_model:
        return "Invalid category. Choose Gold, Silver, or Bronze."
    if section not in seating_model[category]:
        return f"Invalid section in {category} category."
    if row not in seating_model[category][section]:
        return f"Invalid row in section {section}."
    if seat_num < 1 or seat_num > len(seating_model[category][section][row]):
        return f"Seat number {seat_num} is out of range."

    # Convert seat number to zero-based index
    seat_index = seat_num - 1
    seat_status = seating_model[category][section][row][seat_index]

    # Check if the seat is available, taken, or a staircase
    if seat_status == "S":
        return "This is a staircase; please choose a different seat."
    elif seat_status is False:
        return "This seat is already taken. Please choose another seat."

    # Book the seat by setting it to False
    seating_model[category][section][row][seat_index] = False
    save_seating_model(seating_model)  # Persist changes
    return f"Seat {seat_num} in {category} category, section {section}, row {row} has been successfully booked."

# Step 3: Define functions for saving and loading the seating model to/from a JSON file
def save_seating_model(seating_model, filename="seating_model.json"):
    with open(filename, "w") as f:
        json.dump(seating_model, f)

def load_seating_model(filename="seating_model.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # If no file exists yet, return the initial model
        return seating_model

# Load the seating model at the start of the program
seating_model = load_seating_model()

# Example usage
print(select_seat(seating_model, "Gold", "A", "A", 1))  # Expected: Seat booked
print(select_seat(seating_model, "Gold", "A", "A", 1))  # Expected: Already taken
print(select_seat(seating_model, "Gold", "A", "A", 3))  # Expected: Staircase
print(select_seat(seating_model, "Gold", "C", "A", 1))  # Expected: Invalid section
print(select_seat(seating_model, "Silver", "A", "B", 2))  # Expected: Staircase
