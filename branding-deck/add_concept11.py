# Read the file
with open('branding-deck-github/branding-deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Read Concept #11 content
with open('branding-deck-github/concept11.html', 'r', encoding='utf-8') as f:
    concept11_content = f.read().strip()

# Find the location to insert (after YouTube Channel section ends, before Expected Outcomes)
insert_marker = '</section>\n\n        \n\n        <!-- SLIDE 15: EXPECTED OUTCOMES -->'

# Replace with Concept #11 inserted
replacement = f'''</section>

        
        <!-- SLIDE 14: IDEA 11 - THE GRAND TENT ENTRANCE -->
        {concept11_content}

        <!-- SLIDE 15: EXPECTED OUTCOMES -->'''

content = content.replace(insert_marker, replacement)

# Write the modified content back
with open('branding-deck-github/branding-deck.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Concept #11 added successfully!")
print("- Inserted as Slide 14")
print("- Positioned after YouTube Channel (Slide 13)")
print("- Before Expected Outcomes (now Slide 15)")