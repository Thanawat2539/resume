// ===== Theme Toggle (Light / Dark) =====
// Initial theme is applied by the inline script in <head> to avoid flashing.
const themeToggle = document.getElementById('themeToggle');
const rootEl = document.documentElement;

themeToggle.addEventListener('click', () => {
    const isLight = rootEl.getAttribute('data-theme') === 'light';
    if (isLight) {
        rootEl.removeAttribute('data-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        rootEl.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
});

// ===== Back to Top =====
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    backToTop.classList.toggle('show', window.scrollY > 600);
}, { passive: true });

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ===== Navigation Scroll Effect =====
const nav = document.getElementById('mainNav');
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');

const scrollProgress = document.getElementById('scrollProgress');

window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);

    // Scroll progress bar
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
    scrollProgress.style.width = progress + '%';
}, { passive: true });

// ===== Mobile Menu Toggle =====
menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('active');
    mobileMenu.classList.toggle('open');
    document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
});

document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => {
        menuBtn.classList.remove('active');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
    });
});

// ===== Active Nav Link on Scroll =====
const sections = document.querySelectorAll('.section, .hero');
const navLinks = document.querySelectorAll('.nav-link');

const observerNav = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.id;
            navLinks.forEach(link => {
                link.classList.toggle('active', link.dataset.section === id);
            });
        }
    });
}, { threshold: 0.3, rootMargin: '-80px 0px 0px 0px' });

sections.forEach(section => observerNav.observe(section));

// ===== Reveal on Scroll (with stagger per group) =====
const revealElements = document.querySelectorAll('.reveal');

// Stagger siblings that share a parent so grids cascade in
revealElements.forEach(el => {
    const siblings = Array.from(el.parentElement.children).filter(c => c.classList.contains('reveal'));
    const index = siblings.indexOf(el);
    el.style.transitionDelay = Math.min(index, 6) * 0.08 + 's';
});

const observerReveal = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observerReveal.unobserve(entry.target);
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

revealElements.forEach(el => observerReveal.observe(el));

// ===== Cursor-follow spotlight on cards =====
const spotlightCards = document.querySelectorAll(
    '.timeline-content, .edu-card, .skill-category, .contact-card, .cert-card'
);

spotlightCards.forEach(card => {
    card.classList.add('spotlight');
    card.addEventListener('pointermove', (e) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - rect.left) + 'px');
        card.style.setProperty('--my', (e.clientY - rect.top) + 'px');
    });
});

// ===== Skill Bar Animation =====
const skillFills = document.querySelectorAll('.skill-fill');

const observerSkills = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const fill = entry.target;
            const width = fill.dataset.width;
            fill.style.width = width + '%';
        }
    });
}, { threshold: 0.5 });

skillFills.forEach(fill => observerSkills.observe(fill));

// ===== Counter Animation =====
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    counters.forEach(counter => {
        const target = parseInt(counter.dataset.target);
        const duration = 1500;
        const start = performance.now();

        function update(currentTime) {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease out cubic
            const ease = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(ease * target);
            
            counter.textContent = current;
            
            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }

        requestAnimationFrame(update);
    });
}

const heroSection = document.querySelector('.hero');
const observerCounter = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            setTimeout(animateCounters, 600);
            observerCounter.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

observerCounter.observe(heroSection);

// ===== Smooth scroll for all anchor links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ===== Parallax effect for background glows =====
// Use the `translate` property (not `transform`) so it composes with the
// floatGlow keyframe animation instead of overriding it.
let ticking = false;
const glows = document.querySelectorAll('.bg-glow');
window.addEventListener('scroll', () => {
    if (!ticking) {
        requestAnimationFrame(() => {
            const scrollY = window.scrollY;
            glows.forEach((glow, i) => {
                const speed = 0.05 + i * 0.02;
                glow.style.translate = `0 ${scrollY * speed}px`;
            });
            ticking = false;
        });
        ticking = true;
    }
}, { passive: true });
