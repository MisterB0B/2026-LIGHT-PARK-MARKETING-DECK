import re

# Meta tags template
def get_meta_tags(title, description, image_path):
    return f'''
    <!-- Primary Meta Tags -->
    <meta name="title" content="{title}">
    <meta name="description" content="{description}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://yourdomain.com/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://yourdomain.com/{image_path}">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://yourdomain.com/">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{description}">
    <meta property="twitter:image" content="https://yourdomain.com/{image_path}">
    '''

# Update Playbook
print("Updating Playbook meta tags...")
with open('light-park-hub/playbook/index.html', 'r', encoding='utf-8') as f:
    playbook_content = f.read()

playbook_meta = get_meta_tags(
    "THE LIGHT PARK - Creative Playbook 2026",
    "Strategic playbook for THE LIGHT PARK 2026 season with detailed timelines, ROI analysis, and implementation roadmap.",
    "cover-image.png"
)

# Find title tag and insert meta tags after it
pattern = r'(<title>.*?</title>)'
playbook_content = re.sub(pattern, r'\1' + playbook_meta, playbook_content)

with open('light-park-hub/playbook/index.html', 'w', encoding='utf-8') as f:
    f.write(playbook_content)
print("✓ Playbook meta tags added")

# Update Branding Deck
print("\nUpdating Branding Deck meta tags...")
with open('light-park-hub/branding-deck/branding-deck.html', 'r', encoding='utf-8') as f:
    branding_content = f.read()

branding_meta = get_meta_tags(
    "THE LIGHT PARK - Creative Concepts",
    "Explore 20 comprehensive branding concepts including DJ Polar Ice, Pixel Penguin, Gnomies Universe, and innovative marketing strategies.",
    "cover-image.png"
)

branding_content = re.sub(pattern, r'\1' + branding_meta, branding_content)

with open('light-park-hub/branding-deck/branding-deck.html', 'w', encoding='utf-8') as f:
    f.write(branding_content)
print("✓ Branding Deck meta tags added")

# Update Themed Areas
print("\nUpdating Themed Areas meta tags...")
with open('light-park-hub/themed-areas/index.html', 'r', encoding='utf-8') as f:
    themed_content = f.read()

# Check if meta tags already exist
if 'og:image' not in themed_content:
    themed_meta = get_meta_tags(
        "THE LIGHT PARK - Themed Areas",
        "Experience 25 immersive themed areas featuring spectacular light displays, interactive elements, and unforgettable holiday magic.",
        "cover-image.png"
    )
    
    themed_content = re.sub(pattern, r'\1' + themed_meta, themed_content)
    
    with open('light-park-hub/themed-areas/index.html', 'w', encoding='utf-8') as f:
        f.write(themed_content)
    print("✓ Themed Areas meta tags added")
else:
    print("✓ Themed Areas already has meta tags")

print("\n✓ All pages updated with social media meta tags!")
print("✓ All pages will use cover-image.png as thumbnail")
print("\nIMPORTANT: After deployment, update 'https://yourdomain.com/' with your actual URL")