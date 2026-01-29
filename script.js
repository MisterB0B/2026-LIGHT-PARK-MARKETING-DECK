// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const mobileNav = document.getElementById('mobile-nav');
    const navOverlay = document.getElementById('nav-overlay');
    const navLinks = document.querySelectorAll('.nav-link');
    const body = document.body;

    // Check if elements exist
    if (!hamburgerBtn || !mobileNav || !navOverlay) {
        console.error('Required elements not found');
        return;
    }

    // Function to open menu
    function openMenu() {
        hamburgerBtn.classList.add('active');
        mobileNav.classList.add('active');
        navOverlay.classList.add('active');
        hamburgerBtn.setAttribute('aria-expanded', 'true');
        body.classList.add('menu-open');
    }

    // Function to close menu
    function closeMenu() {
        hamburgerBtn.classList.remove('active');
        mobileNav.classList.remove('active');
        navOverlay.classList.remove('active');
        hamburgerBtn.setAttribute('aria-expanded', 'false');
        body.classList.remove('menu-open');
    }

    // Toggle menu on hamburger button click
    hamburgerBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        if (hamburgerBtn.classList.contains('active')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // Close menu when clicking overlay
    navOverlay.addEventListener('click', function() {
        closeMenu();
    });

    // Close menu when clicking on a nav link (for home link)
    navLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            // Only close menu for internal links (home)
            if (this.getAttribute('href').startsWith('#')) {
                closeMenu();
            }
        });
    });

    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && hamburgerBtn.classList.contains('active')) {
            closeMenu();
        }
    });

    // Close menu when window is resized to desktop size
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (window.innerWidth >= 1024 && hamburgerBtn.classList.contains('active')) {
                closeMenu();
            }
        }, 250);
    });

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Add loading animation to cards
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    cards.forEach(function(card) {
        observer.observe(card);
    });

    // Prevent default touch behavior on iOS for better performance
    if ('ontouchstart' in window) {
        document.addEventListener('touchstart', function() {}, { passive: true });
    }

    // Log successful initialization
    console.log('THE LIGHT PARK Hub initialized successfully');
});