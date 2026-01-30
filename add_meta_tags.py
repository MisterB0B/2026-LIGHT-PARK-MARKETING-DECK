# Read the file
with open('light-park-hub/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Meta tags to insert
meta_tags = '''
    <!-- Primary Meta Tags -->
    <meta name="title" content="THE LIGHT PARK 2026 - Marketing & Branding Hub">
    <meta name="description" content="Explore comprehensive 2026 marketing and branding concepts including creative concepts, strategic playbook, and themed area designs.">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://yourdomain.com/">
    <meta property="og:title" content="THE LIGHT PARK 2026 - Marketing & Branding Hub">
    <meta property="og:description" content="Explore comprehensive 2026 marketing and branding concepts including creative concepts, strategic playbook, and themed area designs.">
    <meta property="og:image" content="https://yourdomain.com/cover-image.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://yourdomain.com/">
    <meta property="twitter:title" content="THE LIGHT PARK 2026 - Marketing & Branding Hub">
    <meta property="twitter:description" content="Explore comprehensive 2026 marketing and branding concepts including creative concepts, strategic playbook, and themed area designs.">
    <meta property="twitter:image" content="https://yourdomain.com/cover-image.png">
    '''

# Find the title tag and insert meta tags after it
import re
pattern = r'(<title>.*?</title>)'
replacement = r'\1' + meta_tags

content = re.sub(pattern, replacement, content)

# Write back
with open('light-park-hub/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Meta tags added successfully!")
print("✓ Open Graph tags for Facebook/LinkedIn")
print("✓ Twitter Card tags")
print("✓ Cover image set as thumbnail")