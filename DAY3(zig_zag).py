def convert(s: str, numRows : int) -> str:
    #edge case -> if only one row is present return the string as it is
    if numRows == 1 or numRows >= len(s):
      return s
    
    # create a list of empty strings for each row
    rows = [''] * numRows
    current_rows = 0
    below = False

    #transverse each character in the string
    for char in s:
        #Add the character to the current row
        rows[current_rows] += char
        #Change the direction of we reach the top or bottom row
        if current_rows == 0 or current_rows == numRows - 1 :
            below = not below
            #join all the rows to make the final string
            current_rows += 1 if below else -1
            # Join all the rows to make the final string
   
        return ''.join(rows)

# Input for the program
s = input("Enter the string: ")
numRows = int(input("Enter the number of rows: "))

# Call the function and print the result
result = convert(s, numRows)
print("Zigzag Conversion Result:", result)