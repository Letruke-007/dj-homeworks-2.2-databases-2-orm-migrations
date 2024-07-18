with open('school.json', 'r', encoding='utf-8') as file:
    content = file.read()

with open('school_fixed.json', 'w', encoding='utf-8') as file:
    file.write(content)