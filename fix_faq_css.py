with open('assets/site.css', 'r') as f:
    css = f.read()

faq_css = """
/* FAQ Redesign */
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-width: 800px;
  margin: 0 auto;
}
.faq-item {
  background: var(--surface2);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 20px 24px;
  transition: all 0.3s ease;
}
.faq-item summary {
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  list-style: none;
  outline: none;
  position: relative;
}
.faq-item summary::-webkit-details-marker {
  display: none;
}
.faq-content {
  margin-top: 16px;
  color: var(--muted);
  line-height: 1.6;
}
.faq-item[open] {
  border-color: var(--green);
}
"""

if "FAQ Redesign" not in css:
    with open('assets/site.css', 'a') as f:
        f.write("\n" + faq_css)
    print("FAQ CSS added")
else:
    print("FAQ CSS already there")
