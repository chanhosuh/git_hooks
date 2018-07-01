#!/usr/bin/env python3


def write_todo(open_file, todo):
        line = '   - ' + todo + '\n'
        open_file.write(line)


def write_todos_for_module(open_file, todo_list):
    for todo in todo_list:
        write_todo(open_file, todo)


def write_newline(open_file):
    open_file.write('\n')


def format_as_details(open_file, todo_list):
    open_file.write('   <details>\n')
    open_file.write('   <summary> Todos ({})</summary>\n\n'.format(num_todos))
    write_todos_for_module(open_file, todo_list)
    open_file.write('\n   </details>\n')


def write_header(open_file, title, level=1):
    line = '#' * level + ' ' + title + '\n'
    open_file.write(line)


def make_filepath_link(filepath):
    return '[' + filepath + '](../' + filepath + ')'


def write_filepath(open_file, filepath):
    filepath_link = make_filepath_link(filepath)
    line = str(i) + '. ' + filepath_link + '\n'
    open_file.write(line)


d = {}
with open('todos/todos.txt', 'r') as open_file:
    for line in open_file:
        if 'TODO' not in line:
            continue
        email, filepath, todo = line.lstrip('<').replace('>', '#').split('#')
        email = email.strip().replace('_', '\_')
        filepath = filepath.strip().replace('_', '\_')
        todo = todo.strip().replace('_', '\_')
        try:
            filepath_to_todos = d[email]
        except KeyError:
            d[email] = {filepath:[todo]}
        else:
           filepath_to_todos.setdefault(filepath, []).append(todo)

with open('todos/README.md', 'w') as open_file:
    for email in d:
        write_header(open_file, email, level=1)
        for i, filepath in enumerate(d[email], start=1):
            write_filepath(open_file, filepath)
            todo_list = d[email][filepath]
            num_todos = len(todo_list)
            if num_todos > 3:
                format_as_details(open_file, todo_list)
            else:
                write_todos_for_module(open_file, todo_list)
            write_newline(open_file)
        write_newline(open_file)
    write_newline(open_file)
