def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    patterns = {
        " _ | ||_|": "0",
        "     |  |": "1",
        " _  _||_ ": "2",
        " _  _| _|": "3",
        "   |_|  |": "4",
        " _ |_  _|": "5",
        " _ |_ |_|": "6",
        " _   |  |": "7",
        " _ |_||_|": "8",
        " _ |_| _|": "9"
    }

    row_results = []

    for r in range(0, len(input_grid), 4):

        current_block = input_grid[r: r + 4]

        max_width = max(len(line) for line in current_block)
        grid = [line.ljust(max_width) for line in current_block]

        if max_width % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

        current_line_numbers = ""

        for i in range(0, max_width, 3):
            top = grid[0][i:i + 3]
            mid = grid[1][i:i + 3]
            bot = grid[2][i:i + 3]

            sign = top + mid + bot
            number = patterns.get(sign, "?")
            current_line_numbers += number

        row_results.append(current_line_numbers)

    return ",".join(row_results)