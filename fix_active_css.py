with open('assets/site.css', 'r') as f:
    css = f.read()

active_css = """
.links a.active {
  color: var(--green) !important;
  font-weight: 600;
}
"""

if ".links a.active" not in css:
    with open('assets/site.css', 'a') as f:
        f.write("\n" + active_css)
    print("Active link CSS added")
