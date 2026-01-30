# THE LIGHT PARK Hub - Deployment Guide

## Quick Start

This guide will help you deploy THE LIGHT PARK 2026 Marketing & Branding Hub to various hosting platforms.

## Option 1: GitHub Pages (Recommended)

### Step 1: Create GitHub Repository
1. Go to https://github.com and sign in
2. Click "New Repository"
3. Name it: `light-park-hub-2026`
4. Set to Public or Private
5. Click "Create Repository"

### Step 2: Upload Files
```bash
# Initialize git in the light-park-hub folder
cd light-park-hub
git init
git add .
git commit -m "Initial commit - THE LIGHT PARK Hub"

# Connect to GitHub
git remote add origin https://github.com/YOUR-USERNAME/light-park-hub-2026.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to repository Settings
2. Click "Pages" in left sidebar
3. Under "Source", select "main" branch
4. Click "Save"
5. Your site will be live at: `https://YOUR-USERNAME.github.io/light-park-hub-2026/`

**Deployment Time**: 2-5 minutes

---

## Option 2: Netlify (Easiest)

### Method A: Drag & Drop
1. Go to https://netlify.com
2. Sign up or log in
3. Click "Add new site" → "Deploy manually"
4. Drag the entire `light-park-hub` folder
5. Site goes live immediately!

### Method B: GitHub Integration
1. Push code to GitHub (see Option 1)
2. Go to Netlify dashboard
3. Click "Add new site" → "Import from Git"
4. Connect GitHub and select repository
5. Click "Deploy site"

**Deployment Time**: Instant (drag & drop) or 1-2 minutes (GitHub)

**Custom Domain**: Available in site settings

---

## Option 3: Vercel

### Step 1: Install Vercel CLI (Optional)
```bash
npm install -g vercel
```

### Step 2: Deploy
```bash
cd light-park-hub
vercel
```

Or use the Vercel dashboard:
1. Go to https://vercel.com
2. Click "Add New" → "Project"
3. Import from GitHub or drag folder
4. Click "Deploy"

**Deployment Time**: 1-2 minutes

---

## Option 4: Traditional Web Hosting

### Compatible Hosts
- Bluehost
- HostGator
- GoDaddy
- SiteGround
- Any host with FTP/SFTP access

### Step 1: Connect via FTP
Use an FTP client like FileZilla:
- Host: Your hosting provider's FTP address
- Username: Your FTP username
- Password: Your FTP password
- Port: 21 (or 22 for SFTP)

### Step 2: Upload Files
1. Navigate to `public_html` or `www` folder
2. Upload all files from `light-park-hub` folder
3. Maintain folder structure
4. Ensure `index.html` is in root

### Step 3: Set Permissions
- Files: 644
- Folders: 755

**Deployment Time**: 5-15 minutes (depending on upload speed)

---

## Option 5: AWS S3 + CloudFront

### Step 1: Create S3 Bucket
1. Go to AWS S3 Console
2. Create new bucket: `light-park-hub-2026`
3. Enable "Static website hosting"
4. Set index document: `index.html`

### Step 2: Upload Files
```bash
aws s3 sync light-park-hub/ s3://light-park-hub-2026/ --acl public-read
```

### Step 3: Configure CloudFront (Optional)
1. Create CloudFront distribution
2. Set origin to S3 bucket
3. Enable HTTPS
4. Set default root object: `index.html`

**Deployment Time**: 5-10 minutes (+ 15-20 minutes for CloudFront propagation)

---

## Post-Deployment Checklist

### Test All Features
- [ ] Homepage loads correctly
- [ ] Logo displays properly
- [ ] Hamburger menu opens/closes
- [ ] All three navigation cards work
- [ ] Branding deck loads
- [ ] Playbook loads
- [ ] Themed areas loads
- [ ] Mobile responsiveness works
- [ ] Touch interactions smooth
- [ ] Images load correctly

### Mobile Testing
- [ ] Test on iPhone (Safari)
- [ ] Test on Android (Chrome)
- [ ] Test on tablet
- [ ] Check touch targets
- [ ] Verify menu behavior
- [ ] Test landscape orientation

### Performance Testing
- [ ] Run Google PageSpeed Insights
- [ ] Check Lighthouse scores
- [ ] Verify load times < 3 seconds
- [ ] Test on slow 3G connection

### Browser Testing
- [ ] Chrome (desktop & mobile)
- [ ] Firefox
- [ ] Safari (desktop & mobile)
- [ ] Edge
- [ ] Samsung Internet

---

## Custom Domain Setup

### GitHub Pages
1. Go to repository Settings → Pages
2. Enter custom domain
3. Add CNAME record in DNS:
   - Type: CNAME
   - Name: www (or @)
   - Value: YOUR-USERNAME.github.io

### Netlify
1. Go to Site Settings → Domain Management
2. Click "Add custom domain"
3. Follow DNS configuration instructions
4. SSL certificate auto-generated

### Vercel
1. Go to Project Settings → Domains
2. Add custom domain
3. Configure DNS as instructed
4. SSL certificate auto-generated

---

## SSL/HTTPS

All recommended platforms provide free SSL certificates:
- **GitHub Pages**: Automatic with custom domain
- **Netlify**: Automatic (Let's Encrypt)
- **Vercel**: Automatic (Let's Encrypt)
- **CloudFront**: Use AWS Certificate Manager

---

## Troubleshooting

### Issue: Images Not Loading
**Solution**: Check file paths are relative, not absolute

### Issue: Links Not Working
**Solution**: Verify folder structure is maintained

### Issue: Mobile Menu Not Working
**Solution**: Check JavaScript is loading (script.js)

### Issue: Styles Not Applied
**Solution**: Verify styles.css is in same folder as index.html

### Issue: 404 Errors on Subpages
**Solution**: Ensure all three folders (branding-deck, playbook, themed-areas) are uploaded

---

## Performance Optimization

### Image Optimization
- Cover image: Already optimized (910KB)
- Logo: Already optimized (20KB)
- Consider WebP format for further optimization

### Caching
Add to `.htaccess` (if using Apache):
```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

### CDN Integration
- Use Cloudflare for free CDN
- Enable auto-minification
- Enable Brotli compression

---

## Monitoring & Analytics

### Google Analytics
Add before `</head>` in index.html:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Hotjar (User Behavior)
Add tracking code to understand user interactions

---

## Maintenance

### Regular Updates
- Check for broken links monthly
- Update content as needed
- Monitor performance metrics
- Review mobile compatibility

### Backup Strategy
- Keep local copy of all files
- Use version control (Git)
- Export from hosting platform regularly

---

## Support Resources

- **GitHub Pages**: https://docs.github.com/pages
- **Netlify**: https://docs.netlify.com
- **Vercel**: https://vercel.com/docs
- **AWS S3**: https://docs.aws.amazon.com/s3

---

**Need Help?** Contact THE LIGHT PARK technical team.

**Version**: 1.0.0  
**Last Updated**: January 29, 2025