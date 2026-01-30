# Read the file
with open('branding-deck-github/branding-deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update slide number comments
replacements = [
    ('<!-- SLIDE 15: EXPECTED OUTCOMES -->', '<!-- SLIDE 16: EXPECTED OUTCOMES -->'),
    ('<!-- SLIDE 16: ROI ANALYSIS -->', '<!-- SLIDE 17: ROI ANALYSIS -->'),
    ('<!-- SLIDE 17: MOBILE APP DEVELOPMENT -->', '<!-- SLIDE 18: MOBILE APP DEVELOPMENT -->'),
    ('<!-- SLIDE 18: CALL TO ACTION -->', '<!-- SLIDE 19: CALL TO ACTION -->'),
    ('<!-- SLIDE 19: THANK YOU -->', '<!-- SLIDE 20: THANK YOU -->'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write the modified content back
with open('branding-deck-github/branding-deck.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide numbers updated successfully!")
print("- Expected Outcomes: 15 → 16")
print("- ROI Analysis: 16 → 17")
print("- Mobile App Development: 17 → 18")
print("- Call to Action: 18 → 19")
print("- Thank You: 19 → 20")
print("\nTotal slides: 20")