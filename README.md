# Mood
User inputs their mood into a Google form, and it is displayed in a matrix that can be sent to the lights.

The MoodProgramMk1 program pulls the info from a Gooogle sheet using pygsheets and parses it. The file is easily changeable, in case the available moods change or the program is modified to poll for a different type of information. One it has collected all data from the sheet, MoodProgramMk1 calls Plotter which displays the moods in a matrix, one person per row, with each person getting a unique color code that they can change in the Google sheet.

This is really a template program for taking input from a Google form, parsing it, and displaying it in a matrix.
