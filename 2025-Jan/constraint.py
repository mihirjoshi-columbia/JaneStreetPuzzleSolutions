filename = "no9.txt"
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()  # Remove any trailing newline or spaces
        if len(line) == 0:
            continue
        if line[-1] == '5' and line[-5] == '2' and line[0] == '0':
            # Print the original line
            print("BREAK")
            print(line)
            # Generate and print all circular shifts (excluding the original,
            # which was already printed)
            shifted = line
            for _ in range(1, len(line)):
                # Circular shift: move last character to the front
                shifted = shifted[-1] + shifted[:-1]
                print(shifted)


