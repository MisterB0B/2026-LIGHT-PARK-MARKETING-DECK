# Read CSS file
with open('branding-deck-github/branding-deck-styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add enhanced mobile optimizations
mobile_optimizations = '''
/* Enhanced Mobile Optimizations */
@media (max-width: 768px) {
    /* Improve touch targets */
    .nav-links li a {
        padding: 18px 20px;
        font-size: 16px;
        min-height: 56px;
    }
    
    /* Hamburger button improvements */
    #hamburger-btn {
        width: 50px;
        height: 50px;
        padding: 12px;
    }
    
    #hamburger-btn span {
        height: 3px;
        margin: 5px 0;
    }
    
    /* Slide content optimization */
    .slide {
        padding: 40px 20px;
    }
    
    .slide h2 {
        font-size: 28px;
        margin-bottom: 25px;
    }
    
    .idea-card, .benefit-box, .highlight-box {
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* Grid layouts on mobile */
    .two-column {
        grid-template-columns: 1fr;
        gap: 30px;
    }
    
    .benefits-grid {
        grid-template-columns: 1fr;
    }
    
    /* Text readability */
    .idea-card p, .benefit-box p {
        font-size: 15px;
        line-height: 1.7;
    }
    
    /* Icon sizes */
    .icon {
        font-size: 28px;
    }
    
    /* Navigation panel */
    #nav-links.active {
        width: 85%;
    }
}

/* Extra small devices */
@media (max-width: 480px) {
    .slide h2 {
        font-size: 24px;
    }
    
    .idea-card h4, .benefit-box h4 {
        font-size: 18px;
    }
    
    .idea-card p, .benefit-box p {
        font-size: 14px;
    }
    
    ul {
        padding-left: 20px;
    }
    
    li {
        margin-bottom: 8px;
        font-size: 14px;
    }
}

/* Tablet optimizations */
@media (min-width: 769px) and (max-width: 1024px) {
    .two-column {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    
    .benefits-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
'''

# Append to CSS file
with open('branding-deck-github/branding-deck-styles.css', 'a', encoding='utf-8') as f:
    f.write(mobile_optimizations)

print("Mobile optimizations added successfully!")
print("- Enhanced touch targets")
print("- Improved readability on small screens")
print("- Better spacing and layouts")
print("- Responsive grid adjustments")