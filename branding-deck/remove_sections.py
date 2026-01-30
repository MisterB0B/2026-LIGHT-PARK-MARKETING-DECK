import re

# Read the file
with open('branding-deck-github/branding-deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Content Calendar Strategy section
# This section is inside a div with class "highlight-box" and starts with "Content Calendar Strategy"
pattern1 = r'<div class="highlight-box" style="margin-top: 30px;">\s*<h3>Content Calendar Strategy</h3>.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*'
content = re.sub(pattern1, '', content, flags=re.DOTALL)

# Remove Next Steps section
# This section starts with "Next Steps" heading and includes 3 boxes
pattern2 = r'<div style="margin-top: 50px; text-align: center;">\s*<h3 style="color: var\(--primary-purple\); margin-bottom: 20px;">Next Steps</h3>.*?</div>\s*</div>\s*</section>\s*'
content = re.sub(pattern2, '</section>\n', content, flags=re.DOTALL)

# Write the modified content back
with open('branding-deck-github/branding-deck.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Sections removed successfully!")