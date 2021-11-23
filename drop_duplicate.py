f_in = open('hanspell_result.txt', 'r', encoding='utf8')
f_out = open('drop_duplicate.txt', 'w', encoding='utf8')
ff = open('lines.txt', 'w', encoding='utf8')

lines = f_in.readlines(10000)

for line in lines:
    ff.write(line)

lines = list(set(lines))

for line in lines:
    f_out.write(line)
    f_out.write('\n')