def get_hf(filename):
    with open(filename, 'r') as f: html = f.read()
    import re
    header = re.search(r'<header.*?</header>', html, re.DOTALL)
    footer = re.search(r'<footer.*?</footer>', html, re.DOTALL)
    return (header.group(0) if header else "NO HDR", footer.group(0) if footer else "NO FTR")

h1, f1 = get_hf('index.html')
h2, f2 = get_hf('support.html')
h3, f3 = get_hf('privacy.html')

if h1 == h2 and h2 == h3: print("HEADERS MATCH")
else: print("HEADERS DIFFER")
if f1 == f2 and f2 == f3: print("FOOTERS MATCH")
else: print("FOOTERS DIFFER")

with open('header.html', 'w') as f: f.write(h1)
with open('footer.html', 'w') as f: f.write(f1)
