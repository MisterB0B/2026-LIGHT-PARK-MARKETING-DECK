# Social Media Thumbnail Setup Guide

## Overview
Meta tags have been added to `index.html` to display the cover image as a thumbnail when the link is shared on social media platforms.

---

## What Was Added

### Open Graph Tags (Facebook, LinkedIn, WhatsApp)
```html
<meta property="og:type" content="website">
<meta property="og:url" content="https://yourdomain.com/">
<meta property="og:title" content="THE LIGHT PARK 2026 - Marketing & Branding Hub">
<meta property="og:description" content="Explore comprehensive 2026 marketing and branding concepts...">
<meta property="og:image" content="https://yourdomain.com/cover-image.png">
```

### Twitter Card Tags
```html
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://yourdomain.com/">
<meta property="twitter:title" content="THE LIGHT PARK 2026 - Marketing & Branding Hub">
<meta property="twitter:description" content="Explore comprehensive 2026 marketing and branding concepts...">
<meta property="twitter:image" content="https://yourdomain.com/cover-image.png">
```

---

## IMPORTANT: Update URLs After Deployment

After deploying your site, you MUST update the placeholder URLs in the meta tags:

### Step 1: Find Your Deployed URL
After deploying to Netlify, Vercel, or GitHub Pages, you'll get a URL like:
- Netlify: `https://your-site-name.netlify.app`
- Vercel: `https://your-site-name.vercel.app`
- GitHub Pages: `https://username.github.io/repo-name`

### Step 2: Update Meta Tags
Open `index.html` and replace ALL instances of `https://yourdomain.com/` with your actual URL:

**Find:**
```html
<meta property="og:url" content="https://yourdomain.com/">
<meta property="og:image" content="https://yourdomain.com/cover-image.png">
<meta property="twitter:url" content="https://yourdomain.com/">
<meta property="twitter:image" content="https://yourdomain.com/cover-image.png">
```

**Replace with (example for Netlify):**
```html
<meta property="og:url" content="https://light-park-hub.netlify.app/">
<meta property="og:image" content="https://light-park-hub.netlify.app/cover-image.png">
<meta property="twitter:url" content="https://light-park-hub.netlify.app/">
<meta property="twitter:image" content="https://light-park-hub.netlify.app/cover-image.png">
```

### Step 3: Redeploy
After updating the URLs, redeploy your site so the changes take effect.

---

## Testing Your Thumbnail

### Facebook/LinkedIn Debugger
1. Go to: https://developers.facebook.com/tools/debug/
2. Enter your site URL
3. Click "Debug"
4. You should see your cover image as the thumbnail
5. If not showing, click "Scrape Again"

### Twitter Card Validator
1. Go to: https://cards-dev.twitter.com/validator
2. Enter your site URL
3. Click "Preview card"
4. You should see your cover image

### WhatsApp
1. Send your URL in a WhatsApp chat
2. The thumbnail should appear automatically

---

## Supported Platforms

✅ **Facebook** - Shows cover image when link is shared
✅ **LinkedIn** - Shows cover image in posts
✅ **Twitter** - Shows large image card
✅ **WhatsApp** - Shows thumbnail preview
✅ **Slack** - Shows link preview with image
✅ **Discord** - Shows embed with image
✅ **iMessage** - Shows link preview
✅ **Telegram** - Shows preview with image

---

## Troubleshooting

### Image Not Showing
1. **Check URL**: Make sure you updated `https://yourdomain.com/` to your actual domain
2. **Image Path**: Ensure `cover-image.png` is in the root directory
3. **Image Size**: Cover image should be at least 1200×630px (current: 1024×1024px ✓)
4. **Clear Cache**: Use Facebook Debugger to scrape again
5. **Wait**: Sometimes it takes a few minutes for social platforms to cache the image

### Wrong Image Showing
1. Clear the cache using Facebook Debugger
2. Make sure the image URL is absolute (includes full domain)
3. Check that cover-image.png hasn't been renamed or moved

### Description Not Showing
1. Verify meta description tags are present
2. Some platforms may use their own description
3. Try clearing cache and re-sharing

---

## Image Requirements

### Recommended Sizes
- **Facebook/LinkedIn**: 1200×630px (current: 1024×1024px works)
- **Twitter**: 1200×675px or 1:1 ratio
- **General**: 1200×630px is the universal standard

### Current Image
- **File**: cover-image.png
- **Size**: 910KB
- **Dimensions**: 1024×1024px
- **Format**: PNG
- **Status**: ✅ Meets requirements

---

## Custom Domain Setup

If you're using a custom domain (e.g., `thelightpark.com`):

1. Update all meta tag URLs to use your custom domain:
```html
<meta property="og:url" content="https://thelightpark.com/">
<meta property="og:image" content="https://thelightpark.com/cover-image.png">
```

2. Ensure your custom domain is properly configured with your hosting provider

3. Test with Facebook Debugger after DNS propagation (can take 24-48 hours)

---

## Quick Reference

### What Each Tag Does

| Tag | Purpose |
|-----|---------|
| `og:type` | Tells platforms this is a website |
| `og:url` | The canonical URL of your page |
| `og:title` | Title shown in social media preview |
| `og:description` | Description shown in preview |
| `og:image` | The thumbnail image URL |
| `twitter:card` | Type of Twitter card (large image) |
| `twitter:image` | Twitter-specific image URL |

---

## Example Preview

When someone shares your link, they'll see:

**Title**: THE LIGHT PARK 2026 - Marketing & Branding Hub

**Description**: Explore comprehensive 2026 marketing and branding concepts including creative concepts, strategic playbook, and themed area designs.

**Image**: [Your AI-generated cover image with neon purple and teal text]

---

## Next Steps

1. ✅ Meta tags added to index.html
2. ⏳ Deploy your site
3. ⏳ Update URLs in meta tags with your actual domain
4. ⏳ Redeploy
5. ⏳ Test with Facebook Debugger
6. ⏳ Share and enjoy!

---

**Status**: ✅ Meta tags configured (URLs need updating after deployment)  
**Last Updated**: January 29, 2025