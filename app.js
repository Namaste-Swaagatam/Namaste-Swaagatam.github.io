// Loading Screen Functionality
window.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    setTimeout(() => {
        if (loadingScreen) loadingScreen.style.display = 'none';
    }, 1500);
});

// Navigation Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        navToggle.classList.toggle('active');
    });
});

// Language Toggle
document.addEventListener('DOMContentLoaded', () => {
    const langToggle = document.getElementById('lang-toggle');
    let lang = 'en';
    langToggle.addEventListener('click', () => {
        lang = lang === 'en' ? 'hi' : 'en';
        document.querySelectorAll('[data-en]').forEach(el => {
            el.textContent = el.getAttribute(`data-${lang}`);
        });
        langToggle.querySelector('.lang-text').textContent = lang === 'en' ? 'हिं' : 'En';
    });
});

// Music Toggle
document.addEventListener('DOMContentLoaded', () => {
    const musicToggle = document.getElementById('music-toggle');
    const bgMusic = document.getElementById('bg-music');
    let playing = false;
    musicToggle.addEventListener('click', () => {
        if (!playing) {
            bgMusic.play();
        } else {
            bgMusic.pause();
        }
        playing = !playing;
        musicToggle.classList.toggle('active', playing);
    });
});

// RSVP Form Submission
document.addEventListener('DOMContentLoaded', () => {
    const rsvpForm = document.getElementById('rsvp-form');
    const rsvpSuccess = document.getElementById('rsvp-success');
    if (rsvpForm) {
        rsvpForm.addEventListener('submit', function(e) {
            e.preventDefault();
            rsvpForm.style.display = 'none';
            rsvpSuccess.classList.remove('hidden');
        });
    }
});

// Share Buttons
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.share-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const url = window.location.href;
            if (btn.dataset.share === 'whatsapp') {
                window.open(`https://wa.me/?text=${encodeURIComponent(url)}`, '_blank');
            } else if (btn.dataset.share === 'copy') {
                navigator.clipboard.writeText(url);
                btn.textContent = '✅';
                setTimeout(() => btn.textContent = '🔗', 1000);
            }
        });
    });
});

// Diya Animation (Optional: "lighting" effect)
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.diya').forEach((diya, i) => {
        setTimeout(() => {
            diya.setAttribute('data-lit', 'true');
            diya.classList.add('lit');
        }, 700 + i * 300);
    });
});

// Floating Petals Animation (Optional)
document.addEventListener('DOMContentLoaded', () => {
    const petals = document.querySelectorAll('.floating-petals .petal');
    petals.forEach((petal, i) => {
        petal.style.animationDelay = `${i * 0.6}s`;
    });
});