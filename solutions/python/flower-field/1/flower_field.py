def annotate(garden):
    if not garden:
        return []

    height = len(garden)
    width = len(garden[0])

    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
        for char in row:
            if char not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

    offsets = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),           (0,1),
        (1,-1), (1,0), (1,1),
    ] # Steps from each position for neighbours

    result = []
    
    for r in range(height):
        row_str = ""
        for c in range(width):
            if garden[r][c] == "*":
                row_str += "*"
            else:
                count = 0
                for dr,dc in offsets:
                    nr,nc = r + dr, c + dc
                    if 0 <= nr < height and 0 <= nc < width:
                        if garden[nr][nc] == "*":
                            count += 1
                
                row_str += str(count) if count > 0 else " "
                
        result.append(row_str)
    return result