# Read the file
with open('branding-deck-github/branding-deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Phased Implementation box
# This box starts at line 669 and ends before the Marketing Value highlight box
old_phased = '''                    <div class="idea-card" style="margin-top: 25px;">
                        <h4>Phased Implementation</h4>
                        
                        <p><strong>Phase 1 (Year 1):</strong></p>
                        <ul>
                            <li>Basic DJ booth structure with LED screens</li>
                            <li>Simple animated DJ Polar Ice avatar</li>
                            <li>Basic lighting effects</li>
                        </ul>
                        
                        <p style="margin-top: 15px;"><strong>Phase 2 (Year 2):</strong></p>
                        <ul>
                            <li>Add moving lights and lasers</li>
                            <li>Upgrade to larger pixel mesh screens</li>
                            <li>More complex animations</li>
                        </ul>
                        
                        <p style="margin-top: 15px;"><strong>Phase 3 (Year 3+):</strong></p>
                        <ul>
                            <li>Full production stage with multiple screens</li>
                            <li>Advanced special effects (fog, pyro, etc.)</li>
                            <li>Interactive elements</li>
                        </ul>
                    </div>

                    <div class="highlight-box"'''

new_phased = '''                    <div class="highlight-box"'''

content = content.replace(old_phased, new_phased)

# 2. Update the description text for Polar Ice Dance Party Finale
old_desc = '''<h4>A Centerpiece Attraction</h4>
                        <p>Create a spectacular DJ booth/stage where DJ Polar Ice "performs" live during the show—a visual centerpiece that brings the character to life and creates an Instagram-worthy moment.</p>'''

new_desc = '''<h4>The Grand Finale Experience</h4>
                        <p>An end-of-show attraction where Gnomies can get out and celebrate! This is the finale where guests can get out and dance, take photos with DJ Polar Ice, enjoy perfectly synced pixel mesh screen effects, and dance to Polar Ice's Arctic audio playlist—an immersive celebration that caps off THE LIGHT PARK experience with unforgettable moments and social media-worthy memories.</p>'''

content = content.replace(old_desc, new_desc)

# Write the modified content back
with open('branding-deck-github/branding-deck.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Concept #7 updated successfully!")
print("- Phased Implementation box removed")
print("- Description updated with new finale text")