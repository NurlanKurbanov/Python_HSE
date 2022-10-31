import pathlib

INPUT_CODE_DELIMITER = "# ---end----"
MD_CONTENT_DELIMITER = '<!---md_file_delimiter--->'


def is_empty(data):
    if len(data) == 0 or data == '\n':
        return True
    return False


def read_data(file_name):
    p = pathlib.Path(".") / file_name
    file = p.open()
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file_name = file_name[:-3]
    file_name += '.md'
    txt = open(file_name, 'w')
    txt.write(data)
    txt.close()


def prepare_md_titles(data):
    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description '):
            description = line.replace('# description', '')

    return title, description


def prepare_md_format(title, description, code):
    res = f"""## {title}

{description}

```python
{code.strip()}
```
"""
    return res


def prepare_md_link(title):
    md_link = '-'.join(title.lower().split())
    res = f"+ [{title}](#{md_link})"
    return res


def prepare_new_md_content(new_md_link, new_md_code, old_md_content):
    if old_md_content is None:
        result_md = f"{new_md_link}\n{MD_CONTENT_DELIMITER}\n\n{new_md_code}"
    else:
        old_md_link, old_md_code = old_md_content.split(MD_CONTENT_DELIMITER)
        result_md = f"{old_md_link}{new_md_link}\n{MD_CONTENT_DELIMITER}{old_md_code}\n\n{new_md_code}"
    return result_md


def convert_data(data, old_md_content):
    file_info, code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(file_info)
    new_md_code = prepare_md_format(title, description, code)
    new_md_link = prepare_md_link(title)
    res = prepare_new_md_content(new_md_link, new_md_code, old_md_content)  # <-old_md_content
    return res


def main():
    task_file_name = "2_2.py"
    old_file_name = "collection.md"

    content = read_data(task_file_name)
    if not pathlib.Path.exists(pathlib.Path(".") / "collection.md"):
        old_md_content = None
    else:
        old_md_content = read_data(old_file_name)
        if is_empty(old_md_content):
            old_md_content = None

    res = convert_data(content, old_md_content)
    write_data(old_file_name, res)


if __name__ == "__main__":
    main()
