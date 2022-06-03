blank_lines_counter = 0
lines_with_issues = {}
style_issues = {'S001': 'Too long',
                'S002': 'Indentation is not a multiple of four',
                'S003': 'Unnecessary semicolon',
                'S004': 'At least two spaces required before inline comments',
                'S005': 'TODO found',
                'S006': 'More than two blank lines used before this line'}


def add_line(line, issue_code):
    global lines_with_issues
    try:
        lines_with_issues[line].append(issue_code)
    except KeyError:
        lines_with_issues[line] = [issue_code]


def log_issue(issue_lines_dict):
    for line in issue_lines_dict:
        for issue_code in issue_lines_dict[line]:
            print(f"Line {line}: {issue_code} {style_issues[issue_code]}")


def check_s001(line, line_num):
    if len(line) > 79:
        add_line(line_num, "S001")


def check_s002(line, line_num):
    if (len(line) - len(line.lstrip())) % 4 != 0:
        add_line(line_num, "S002")


def check_s003(line, line_num):
    if ";" in line:
        smcol_indxs = []
        current_index = line.index(';')
        for _ in range(line.count(";")):
            index = line.find(";", current_index)
            smcol_indxs.append(index)
            current_index += 1

        qmark = None
        qmark_first_indx = 0
        qmark_second_indx = 0
        if "'" in line or '"' in line:
            if "'" in line:
                qmark = "'"
            elif '"' in line:
                qmark = '"'
            qmark_first_indx = line.find(qmark)
            qmark_second_indx = line.find(qmark, qmark_first_indx + 1)
        
        for i in smcol_indxs:
            if "#" in line and qmark:
                if i < line.index("#"):
                    if not qmark_first_indx < i < qmark_second_indx:
                        add_line(line_num, "S003")
                        break
            elif qmark and not qmark_first_indx < i < qmark_second_indx:
                    add_line(line_num, "S003")
                    break
            elif "#" in line and i < line.index("#"):
                add_line(line_num, "S003")
                break
            

def check_s004(line, line_num):
    if "#" in line:
        hsign_indx = line.index("#")
        if line[hsign_indx - 2: hsign_indx] != "  ":
            add_line(line_num, "S004")


def check_s005(line, line_num):
    if "todo" in line:
        if "#" in line and line.index("#") < line.index("todo"):
            add_line(line_num, "S005")


def check_s006(line_num):
    global blank_lines_counter
    if blank_lines_counter > 2:
        blank_lines_counter = 0
        add_line(line_num, "S006")


def main():
    global blank_lines_counter
    line_counter = 0

    file = open("testfile.txt", "r")

    for line in file:
        line_counter += 1
        if line.isspace():
            blank_lines_counter += 1
        else:
            line = line.lower()
            check_s001(line, line_counter)
            check_s002(line, line_counter)
            check_s003(line, line_counter)
            check_s004(line, line_counter)
            check_s005(line, line_counter)
            check_s006(line_counter)

    file.close()
    log_issue(lines_with_issues)


main()
