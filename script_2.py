# Update JavaScript to remove old kalash/diya interactions and optimize for lotus animation
js_content = '''// Pink Architectural Griha Pravesh Invitation - Interactive Elements
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
    
    // Global state
    let musicPlaying = false;
    let currentLanguage = 'en';
    
    function initializeApp() {
        // Show loading screen first
        showLoadingScreen();
        
        // Initialize all interactive elements after loading
        setTimeout(() => {
            hideLoadingScreen();
            initializeInteractiveElements();
            initializeFloatingControls();
            initializeScrollAnimations();
            startContinuousAnimations();
        }, 4500);
    }
    
    function showLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        const mainContent = document.getElementById('main-content');
        
        loadingScreen.style.display = 'flex';
        mainContent.classList.add('hidden');
        
        // Animate the Om symbol
        setTimeout(() => {
            const omLoader = document.querySelector('.om-loader');
            omLoader.style.animation = 'glow 2s ease-in-out infinite alternate';
        }, 1000);
    }
    
    function hideLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        const mainContent = document.getElementById('main-content');
        
        // Fade out loading screen
        loadingScreen.style.opacity = '0';
        setTimeout(() => {
            loadingScreen.style.display = 'none';
            mainContent.classList.remove('hidden');
            
            // Start entrance animations
            startEntranceAnimations();
        }, 1000);
    }
    
    function startEntranceAnimations() {
        const heroSection = document.querySelector('.hero-section');
        const archContainer = document.querySelector('.arch-container');
        const lotusFlowers = document.querySelectorAll('.lotus');
        
        // Animate hero section
        heroSection.style.opacity = '0';
        heroSection.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            heroSection.style.transition = 'all 1s ease';
            heroSection.style.opacity = '1';
            heroSection.style.transform = 'translateY(0)';
        }, 100);
        
        // Animate arch container
        setTimeout(() => {
            archContainer.style.animation = 'fadeInUp 1.5s ease forwards';
        }, 500);
        
        // Animate lotus flowers
        setTimeout(() => {
            lotusFlowers.forEach((lotus, index) => {
                setTimeout(() => {
                    lotus.style.opacity = '1';
                    lotus.style.animation = 'float 3s ease-in-out infinite';
                    if (index === 1) {
                        lotus.style.animationDelay = '1.5s';
                    }
                }, index * 500);
            });
        }, 1000);
    }
    
    function initializeInteractiveElements() {
        // Initialize Om symbol glow effect
        const omSymbol = document.querySelector('.om-symbol');
        if (omSymbol) {
            omSymbol.addEventListener('mouseenter', () => {
                omSymbol.style.animation = 'omGlow 0.5s ease forwards';
            });
            
            omSymbol.addEventListener('mouseleave', () => {
                omSymbol.style.animation = 'omGlow 3s ease-in-out infinite alternate';
            });
        }
        
        // Initialize lotus hover effects
        const lotusFlowers = document.querySelectorAll('.lotus-petals');
        lotusFlowers.forEach(lotus => {
            lotus.addEventListener('mouseenter', () => {
                lotus.style.transform = 'scale(1.1)';
                lotus.style.transition = 'transform 0.3s ease';
            });
            
            lotus.addEventListener('mouseleave', () => {
                lotus.style.transform = 'scale(1)';
            });
        });
        
        // Initialize vine sway on hover
        const vines = document.querySelectorAll('.vine-decoration');
        vines.forEach(vine => {
            vine.addEventListener('mouseenter', () => {
                vine.style.animation = 'sway 1s ease infinite';
            });
            
            vine.addEventListener('mouseleave', () => {
                setTimeout(() => {
                    vine.style.animation = 'sway 4s ease-in-out infinite';
                }, 1000);
            });
        });
        
        // Initialize lotus-om animation interaction
        const lotusAnimation = document.querySelector('.animated-lotus');
        if (lotusAnimation) {
            lotusAnimation.addEventListener('mouseenter', () => {
                // Speed up animation on hover
                const petals = lotusAnimation.querySelectorAll('.lotus-petal');
                const omCenter = lotusAnimation.querySelector('.lotus-om-center');
                const glow = lotusAnimation.querySelector('.lotus-glow');
                
                petals.forEach(petal => {
                    petal.style.animationDuration = '2s';
                });
                if (omCenter) omCenter.style.animationDuration = '2s';
                if (glow) glow.style.animationDuration = '2s';
            });
            
            lotusAnimation.addEventListener('mouseleave', () => {
                // Reset to normal speed
                const petals = lotusAnimation.querySelectorAll('.lotus-petal');
                const omCenter = lotusAnimation.querySelector('.lotus-om-center');
                const glow = lotusAnimation.querySelector('.lotus-glow');
                
                petals.forEach(petal => {
                    petal.style.animationDuration = '4s';
                });
                if (omCenter) omCenter.style.animationDuration = '4s';
                if (glow) glow.style.animationDuration = '4s';
            });
        }
    }
    
    function initializeFloatingControls() {
        const musicToggle = document.getElementById('music-toggle');
        const langToggle = document.getElementById('lang-toggle');
        const backgroundMusic = document.getElementById('background-music');
        
        // Music toggle functionality
        musicToggle.addEventListener('click', () => {
            if (musicPlaying) {
                backgroundMusic.pause();
                musicToggle.innerHTML = '<i class="fas fa-music"></i>';
                musicToggle.style.opacity = '0.7';
                musicPlaying = false;
            } else {
                backgroundMusic.play().then(() => {
                    musicToggle.innerHTML = '<i class="fas fa-volume-up"></i>';
                    musicToggle.style.opacity = '1';
                    musicPlaying = true;
                }).catch(error => {
                    console.log('Music play failed:', error);
                    showNotification('Music could not be played. Please check your browser settings.');
                });
            }
        });
        
        // Language toggle functionality
        langToggle.addEventListener('click', () => {
            currentLanguage = currentLanguage === 'en' ? 'hi' : 'en';
            toggleLanguage();
        });
    }
    
    function toggleLanguage() {
        const translations = {
            en: {
                'invitation-text': 'Inviting Your Gracious Presence On<br>The Occasion Of <strong>Our New Home!</strong>',
                'ceremony-title': 'GRIHA<br>PRAVESH',
                'about-title': 'About Griha Pravesh',
                'confirmation-title': 'Please Confirm Your Presence!',
                'share-title': 'Share all your memorable clicks here!',
                'lang-text': 'हिं'
            },
            hi: {
                'invitation-text': 'हमारे <strong>नए घर</strong> के<br>गृह प्रवेश समारोह में<br>आपकी उपस्थिति का सम्मान',
                'ceremony-title': 'गृह<br>प्रवेश',
                'about-title': 'गृह प्रवेश के बारे में',
                'confirmation-title': 'कृपया अपनी उपस्थिति की पुष्टि करें!',
                'share-title': 'अपने यादगार पलों को यहाँ साझा करें!',
                'lang-text': 'EN'
            }
        };
        
        const elements = {
            'invitation-text': document.querySelector('.invitation-text'),
            'ceremony-title': document.querySelector('.ceremony-title'),
            'about-title': document.querySelector('.significance-text h2'),
            'confirmation-title': document.querySelector('.confirmation-header h2'),
            'share-title': document.querySelector('.share-section h2'),
            'lang-text': document.querySelector('.lang-text')
        };
        
        Object.keys(elements).forEach(key => {
            if (elements[key] && translations[currentLanguage][key]) {
                elements[key].innerHTML = translations[currentLanguage][key];
            }
        });
    }
    
    function initializeScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    
                    // Special handling for lotus animation
                    if (entry.target.classList.contains('significance-section')) {
                        const lotusAnimation = entry.target.querySelector('.animated-lotus');
                        if (lotusAnimation) {
                            // Slight delay before starting lotus animation
                            setTimeout(() => {
                                lotusAnimation.style.visibility = 'visible';
                            }, 500);
                        }
                    }
                }
            });
        }, observerOptions);
        
        // Observe sections for scroll animations
        const sections = document.querySelectorAll('.significance-section, .confirmation-section, .share-section');
        sections.forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(30px)';
            section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            observer.observe(section);
        });
        
        // Initially hide lotus animation until section is visible
        const lotusAnimation = document.querySelector('.animated-lotus');
        if (lotusAnimation) {
            lotusAnimation.style.visibility = 'hidden';
        }
    }
    
    function startContinuousAnimations() {
        // Continuous hanging decoration motion
        const beadStrings = document.querySelectorAll('.bead-string');
        beadStrings.forEach((string, index) => {
            string.style.animation = `hangingMotion 3s ease-in-out infinite ${index * 0.5}s`;
        });
        
        // Continuous leaf rustle
        const leaves = document.querySelectorAll('.leaf');
        leaves.forEach((leaf, index) => {
            leaf.style.animation = `leafRustle 3s ease-in-out infinite ${index * 0.5}s`;
        });
    }
    
    function showNotification(message) {
        const notification = document.createElement('div');
        notification.style.position = 'fixed';
        notification.style.top = '20px';
        notification.style.right = '20px';
        notification.style.background = 'var(--arch-gradient)';
        notification.style.color = 'white';
        notification.style.padding = '15px 20px';
        notification.style.borderRadius = '8px';
        notification.style.boxShadow = '0 4px 12px var(--pink-shadow)';
        notification.style.zIndex = '10001';
        notification.style.animation = 'fadeInUp 0.5s ease';
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 500);
        }, 3000);
    }
    
    // Handle background music autoplay restrictions
    document.addEventListener('click', () => {
        const backgroundMusic = document.getElementById('background-music');
        if (!musicPlaying && backgroundMusic.paused) {
            // Try to enable autoplay after user interaction
            backgroundMusic.play().then(() => {
                const musicToggle = document.getElementById('music-toggle');
                musicToggle.innerHTML = '<i class="fas fa-volume-up"></i>';
                musicToggle.style.opacity = '1';
                musicPlaying = true;
            }).catch(() => {
                // Music autoplay still blocked
            });
        }
    }, { once: true });
    
    // Handle mobile touch interactions
    if ('ontouchstart' in window) {
        const touchElements = document.querySelectorAll('.lotus-petals, .om-symbol, .animated-lotus');
        touchElements.forEach(element => {
            element.addEventListener('touchstart', () => {
                element.style.transform = 'scale(1.05)';
            });
            
            element.addEventListener('touchend', () => {
                element.style.transform = 'scale(1)';
            });
        });
    }
    
    // Initialize accessibility features
    initializeAccessibilityFeatures();
    
    function initializeAccessibilityFeatures() {
        // Keyboard navigation for custom elements
        const interactiveElements = document.querySelectorAll('.control-btn, .map-link, .animated-lotus');
        
        interactiveElements.forEach(element => {
            element.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    if (element.classList.contains('animated-lotus')) {
                        // Trigger lotus interaction
                        element.dispatchEvent(new Event('mouseenter'));
                        setTimeout(() => {
                            element.dispatchEvent(new Event('mouseleave'));
                        }, 2000);
                    } else {
                        element.click();
                    }
                }
            });
        });
        
        // Add ARIA labels for screen readers
        const omSymbol = document.querySelector('.om-symbol');
        if (omSymbol) {
            omSymbol.setAttribute('aria-label', 'Om symbol - Sacred Hindu symbol');
        }
        
        const lotusFlowers = document.querySelectorAll('.lotus-petals');
        lotusFlowers.forEach((lotus, index) => {
            lotus.setAttribute('aria-label', `Decorative lotus flower ${index + 1}`);
        });
        
        const lotusAnimation = document.querySelector('.animated-lotus');
        if (lotusAnimation) {
            lotusAnimation.setAttribute('aria-label', 'Beautiful lotus opening animation with Om symbol - Sacred Hindu symbol for prosperity');
            lotusAnimation.setAttribute('tabindex', '0');
        }
    }
    
    console.log('🏠 Griha Pravesh Invitation Loaded Successfully! ✨');
    console.log('🌸 Beautiful lotus-om animation ready! 🕉️');
});'''

# Save the updated JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Updated app.js:")
print("ADDED:")
print("- Lotus-om animation hover interaction (speeds up on hover)")
print("- Scroll-triggered visibility for lotus animation")
print("- Touch interaction support for mobile devices")
print("- Accessibility support with ARIA labels and keyboard navigation")
print("- Special entrance animation timing for lotus")
print("")
print("REMOVED:")
print("- Old diya click interactions")
print("- Kalash floating animation references")
print("")
print("🌸 INTERACTIVE FEATURES:")
print("1. Hover over lotus = animation speeds up (4s → 2s)")
print("2. Lotus appears when section scrolls into view")
print("3. Touch support for mobile devices")
print("4. Keyboard navigation (Tab + Enter)")
print("5. Screen reader friendly with ARIA labels")

print("\n🎉 LOTUS-OM ANIMATION COMPLETE!")
print("\n📁 All files updated:")
print("1. ✅ HTML: Beautiful lotus structure with 8 petals + Om center")
print("2. ✅ CSS: Pink gradient petals + golden Om + glow effect")  
print("3. ✅ JS: Interactive hover effects + accessibility")
print("")
print("🚀 Ready to upload to GitHub!")
print("Your guests will be mesmerized by the sacred lotus opening to reveal the Om symbol! 🪷✨")