import sys
import os
import re


blank_lines_counter = 0
lines_with_issues = {}
style_issues = {'S001': 'Too long',
                'S002': 'Indentation is not a multiple of four',
                'S003': 'Unnecessary semicolon',
                'S004': 'At least two spaces required before inline comments',
                'S005': 'TODO found',
                'S006': 'More than two blank lines used before this line',
                'S007': 'Too many spaces after construction_name',
                'S008': 'Class name should be written in CamelCase',
                'S009': 'Function name should be written in snake_case'}


def add_line(path, line, issue_code):
    global lines_with_issues
    if path not in lines_with_issues:
        lines_with_issues[path] = {}
    if line not in lines_with_issues[path]:
        lines_with_issues[path][line] = []
    lines_with_issues[path][line].append(issue_code)


def log_issue(issue_lines_dict):
    for path in issue_lines_dict:
        for line in issue_lines_dict[path]:
            for issue_code in issue_lines_dict[path][line]:
                print(f"{path}: Line {line}: {issue_code} {style_issues[issue_code]}")


def check_s001(path, line, line_num):
    if len(line) > 79:
        add_line(path, line_num, "S001")


def check_s002(path, line, line_num):
    if (len(line) - len(line.lstrip())) % 4 != 0:
        add_line(path, line_num, "S002")


def check_s003(path, line, line_num):
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
                        add_line(path, line_num, "S003")
                        break
            elif qmark and not qmark_first_indx < i < qmark_second_indx:
                add_line(path, line_num, "S003")
                break
            elif "#" in line and i < line.index("#"):
                add_line(path, line_num, "S003")
                break
            elif "#" not in line and not qmark:
                add_line(path, line_num, "S003")
                break


def check_s004(path, line, line_num):
    if "#" in line and line.index("#") != 0:
        hsign_indx = line.index("#")
        if line[hsign_indx - 2: hsign_indx] != "  ":
            add_line(path, line_num, "S004")


def check_s005(path, line, line_num):
    line = line.lower()
    if "todo" in line:
        if "#" in line and line.index("#") < line.index("todo"):
            add_line(path, line_num, "S005")


def check_s006(path, line_num):
    global blank_lines_counter
    if blank_lines_counter > 2:
        blank_lines_counter = 0
        add_line(path, line_num, "S006")


def check_s007(path, line, line_num):
    constr_name = None
    if "def" in line:
        constr_name = "def"
    elif "class" in line:
        constr_name = "class"
    if constr_name:
        indx = line.index(constr_name) + len(constr_name)
        if line[indx:indx+2] == "  ":
            add_line(path, line_num, "S007")


def check_s008(path, line, line_num):
    if "class" in line:
        indx = line.index("class") + len("class")
        class_name = []
        for i in range(indx, len(line)):
            if line[i] != " ":
                class_name.append(line[i])
        class_name = "".join(class_name)
        #print(class_name)

        pattern = r"[A-Z]\w*[A-Z]?\w*\(?[A-Z]\w*[A-Z]?\w*\)?:"
        ismatch = bool(re.match(pattern, class_name))
        if not ismatch:
            add_line(path, line_num, "S008")


def check_s009(path, line, line_num):
    if "def" in line:
        indx = line.index("def") + len("def")
        func_name = []
        for i in range(indx, len(line)):
            if line[i] != " ":
                func_name.append(line[i])
        func_name = "".join(func_name)

        if func_name != func_name.lower():
            add_line(path, line_num, "S009")


def check_code(path, line, line_num):
    check_s001(path, line, line_num)
    check_s002(path, line, line_num)
    check_s003(path, line, line_num)
    check_s004(path, line, line_num)
    check_s005(path, line, line_num)
    check_s006(path, line_num)
    check_s007(path, line, line_num)
    check_s008(path, line, line_num)
    check_s009(path, line, line_num)


def main():
    global blank_lines_counter
    line_counter = 0
    path_from_arg = sys.argv[1]
    files_to_check = []

    if os.path.isdir(path_from_arg):
        for dirpath, dirnames, files in os.walk(path_from_arg):
            for file_name in files:
                if file_name.endswith(".py"):
                    files_to_check.append(os.path.join(dirpath, file_name))
    else:
        files_to_check.append(path_from_arg)

    files_to_check.sort()

    for file_path in files_to_check:
        with open(file_path, 'r') as file:
            for line in file:
                line_counter += 1
                if line.isspace():
                    blank_lines_counter += 1
                else:
                    check_code(file_path, line, line_counter)
                    blank_lines_counter = 0
        line_counter = 0
        blank_lines_counter = 0

    log_issue(lines_with_issues)


main()
