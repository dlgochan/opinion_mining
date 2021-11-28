import json

f_input = open("./result.json", mode="r")
f_output = open("fix.json", mode="w", encoding='utf8')
str = []
fix = []

str = f_input.readlines() 

for j in str:
    f_output.write(json.loads(j)) # json -> dict
    f_output.write('\n')