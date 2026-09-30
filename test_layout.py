with open('assets/site.css', 'r') as f:
    css = f.read()
if 'main {\n  flex: 1;\n}' in css:
    print("Flex 1 is on main.")
else:
    print("Flex 1 NOT on main.")
