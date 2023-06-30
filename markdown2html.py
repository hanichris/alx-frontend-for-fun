#!/usr/bin/python3
"""Markdown to HTML converter."""
from pathlib import Path
import re
import sys


markdown_dict = {
    '#': '<h1> </h1>',
    '##': '<h2> </h2>',
    '###': '<h3> </h3>',
    '####': '<h4> </h4>',
    '#####': '<h5> </h5>',
    '######': '<h6> </h6>',
    '-': '<ul> </ul>'
    }

if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    files = sys.argv[1], sys.argv[2]
    path = Path(files[0])
    if not path.is_file():
        sys.stderr.write(f"Missing {files[0]}\n")
        sys.exit(1)

    # Load file contents into memory.
    with path.open(encoding='utf-8') as f:
        lines = f.readlines()

    # Process memory content into required format.
    open_list_flag = close_list_flag = 0
    for line in lines:
        markdown_tag, text = re.split(r'(#+(?=#?))', line)[1:]
        text = text.strip()
        if open_list_flag:
            if markdown_tag == '-' or markdown_tag == '*':
                pass
            else:
                open_list_flag = 0
                close_list_flag = 1
        # html_tags = markdown_dict[markdown_tag].split()
        # print(f'{html_tags[0]}{text}{html_tags[-1]}')

    # # Write out the formatted output to a file.
    # with open(files[1], mode='w', encoding='utf-8') as f:
    #         f.write(output)
