import re

# Read current privacy.html
with open('privacy.html', 'r') as f:
    html = f.read()

# I will replace the script block at the bottom
script_block = """
  <script src="assets/main.js"></script>
  <script>
    document.querySelectorAll('.lang-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.lang-tab').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.policy-content').forEach(s => s.classList.remove('active'));
        btn.classList.add('active');
        const contentId = 'lang-' + btn.getAttribute('data-lang');
        const content = document.getElementById(contentId);
        if(content) content.classList.add('active');
      });
    });
  </script>
</body>
"""

html = re.sub(r'<script src="assets/main.js"></script>.*?</body>', script_block, html, flags=re.DOTALL)

with open('privacy.html', 'w') as f:
    f.write(html)
print("Script updated")
