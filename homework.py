
    
name_pattern = re.compiler (r """
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
""")

name_pattern = re.compile((?P<first>[A-Z][a-zA-Z]+) (?P<middle>[A-Z][a-zA-Z]+) (?P<last>[A-Z][a-zA-Z]+))
for name in name_pattern.finditer(data):
    print(name_pattern)