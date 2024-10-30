You are tasked with writing an algorithm for a theater seating selection system based on a Model interpreted from the image above.
 The theater has three seating categories: Gold, Silver, and Bronze, 
 each containing multiple sections (A, B, C, etc.) with rows of seats. 
 The number of seats in each row varies, and some rows may have designated staircases represented by the a whitespace.

Your task is to:

Allow users to select seats by inputting the section (e.g., "A"), row letter (e.g., "A", "B"), and seat number (e.g., 5).
Ensure that once a seat is selected by a user, it cannot be selected again by another user.
If a user attempts to select a seat that has already been chosen or is unavailable (e.g., "S" for staircase), notify them and ask for a different seat.
Update the seating model to reflect the selection and allow other users to continue selecting valid seats. , choose a suitable structure to maintain persistency.

##solution##
Step 1: Initialize the Seating Model
We'll set up a data structure that represents our theater's seating layout. This structure will use nested dictionaries to represent categories (Gold, Silver, Bronze), sections within each category (A, B, etc.), and rows within each section (A, B, C, etc.). Each row will have an array of seats, where each seat can be:

True for available seats,
False for taken seats, or
"S" for staircases.

Step 2: Define the Seat Selection Function
We'll create a function called select_seat that:

Validates Input: Checks if the specified category, section, row, and seat number exist.
Checks Seat Availability: Confirms whether the seat is available, taken, or a staircase.
Updates Seat Status: If available, it marks the seat as taken (False) and returns a confirmation message.
Step 3: Add Persistence with File Save and Load Functions
To ensure that the seating arrangement persists between program runs, we'll use JSON files to save the seating_model after each seat selection and load it when the program starts.

Saving: We’ll create save_seating_model to write the current seating data to a JSON file.
Loading: We’ll create load_seating_model to read the data back from the JSON file on startup.