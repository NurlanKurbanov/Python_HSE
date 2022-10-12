import pathlib

p = pathlib.Path("..") / "2_4.py"
f = p.open()

lines = f.readlines()
ln0 = lines[0]
title = ln0[8:]
ln1 = lines[1]
desc = ln1[14:]

txt = open(f'{title[:-1]}.txt', 'w')
title_hyphen = '-'.join(title.split())
txt.write(f'+ [{title[:-1]}](#{title_hyphen})\n')
txt.write(f'## {title}')
txt.write(f'### {desc}')

f.close()
f = p.open()
code = (f.read()).split("# ---end----")[1]
txt.write(f'```\n {code} \n ```')

f.close()
txt.close()

