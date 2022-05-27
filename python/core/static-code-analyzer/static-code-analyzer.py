issue_lines = []
counter = 0


def print_issue_lines(lines_list):
    for num in lines_list:
        print(f"Line {num}: S001 Too long")


file = open(input(), "r")

for line in file:
    counter += 1
    if len(line) > 79:
        issue_lines.append(counter)
file.close()

print_issue_lines(issue_lines)
