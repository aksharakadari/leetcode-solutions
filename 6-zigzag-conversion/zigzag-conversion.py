class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        # Edge case: if rows are 1 or string is short, no zigzag forms
        if num_rows <= 1 or len(s) <= num_rows:
            return s

        # Track strings for each row
        rows = ["" for _ in range(num_rows)]
        current_row = 0
        going_down = False

        # Iterate through each character
        for char in s:
            rows[current_row] += char
            
            # Reverse direction if we hit the top or bottom row
            if current_row == 0 or current_row == num_rows - 1:
                going_down = not going_down
            
            # Move up or down based on current direction
            current_row += 1 if going_down else -1

        # Combine all rows into a single string
        return "".join(rows)
