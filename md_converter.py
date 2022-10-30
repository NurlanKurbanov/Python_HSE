import pathlib

INPUT_CODE_DELIMITER = "# ---end----"


def read_data(file_name):
    p = pathlib.Path("..") / file_name
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
    md_link = '-'.join(title.lower().split())

    res = f"""+ [{title}](#{md_link})

## {title}
{description}

```python
{code.strip()}
```
"""

    return res


def convert_data(data):
    file_info, code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(file_info)
    res = prepare_md_format(title, description, code)
    return res


def main():
    # if not pathlib.Path.exists(pathlib.Path(".") / "collection.txt"):
    #     exit(12)
    task_file_name = "1_2.py"
    # old_file_name = 'collection.txt'

    content = read_data(task_file_name)
    # old_content = read_data(old_file_name)

    res = convert_data(content)
    write_data(task_file_name, res)


if __name__ == "__main__":
    main()
