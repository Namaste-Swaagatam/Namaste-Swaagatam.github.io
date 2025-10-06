# Update JavaScript to remove language toggle functionality completely
js_content = '''// Pink Architectural Griha Pravesh Invitation - Interactive Elements
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
    
    // Global state
    let musicPlaying = false;
    
    function initializeApp() {
        // Show loading screen first
        showLoadingScreen();
        
        // Initialize all interactive elements after loading
        setTimeout(() => {
            hideLoadingScreen();
            initializeInteractiveElements();
            initializeMusicControl();
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
        
        // Initialize rangoli-om animation interaction
        const rangoliAnimation = document.querySelector('.rangoli-container');
        if (rangoliAnimation) {
            rangoliAnimation.addEventListener('mouseenter', () => {
                // Speed up animation on hover
                const patterns = rangoliAnimation.querySelectorAll('.rangoli-pattern');
                const omCenter = rangoliAnimation.querySelector('.rangoli-om-center');
                const particles = rangoliAnimation.querySelector('.rangoli-particles');
                
                patterns.forEach(pattern => {
                    pattern.style.animationDuration = '2s';
                });
                if (omCenter) omCenter.style.animationDuration = '2s';
                if (particles) particles.style.animationDuration = '2s';
            });
            
            rangoliAnimation.addEventListener('mouseleave', () => {
                // Reset to normal speed
                const patterns = rangoliAnimation.querySelectorAll('.rangoli-pattern');
                const omCenter = rangoliAnimation.querySelector('.rangoli-om-center');
                const particles = rangoliAnimation.querySelector('.rangoli-particles');
                
                patterns.forEach(pattern => {
                    pattern.style.animationDuration = '4s';
                });
                if (omCenter) omCenter.style.animationDuration = '4s';
                if (particles) particles.style.animationDuration = '4s';
            });
        }
    }
    
    function initializeMusicControl() {
        const musicToggle = document.getElementById('music-toggle');
        const backgroundMusic = document.getElementById('background-music');
        
        if (!musicToggle || !backgroundMusic) {
            console.log('Music elements not found');
            return;
        }
        
        // Music toggle functionality
        musicToggle.addEventListener('click', () => {
            if (musicPlaying) {
                backgroundMusic.pause();
                musicToggle.innerHTML = '<i class="fas fa-music"></i>';
                musicToggle.style.opacity = '0.7';
                musicPlaying = false;
                showNotification('Music paused');
            } else {
                backgroundMusic.play().then(() => {
                    musicToggle.innerHTML = '<i class="fas fa-volume-up"></i>';
                    musicToggle.style.opacity = '1';
                    musicPlaying = true;
                    showNotification('Music playing');
                }).catch(error => {
                    console.log('Music play failed:', error);
                    showNotification('Music file not found. Please upload "background-music.mp3" to your repository.');
                });
            }
        });
        
        // Check if audio file exists
        backgroundMusic.addEventListener('canplaythrough', () => {
            console.log('Audio file loaded successfully');
        });
        
        backgroundMusic.addEventListener('error', (e) => {
            console.log('Audio file error:', e);
            showNotification('Audio file not found. Upload "background-music.mp3" to your repository.');
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
                    
                    // Special handling for rangoli animation
                    if (entry.target.classList.contains('significance-section')) {
                        const rangoliAnimation = entry.target.querySelector('.rangoli-container');
                        if (rangoliAnimation) {
                            // Slight delay before starting rangoli animation
                            setTimeout(() => {
                                rangoliAnimation.style.visibility = 'visible';
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
        
        // Initially hide rangoli animation until section is visible
        const rangoliAnimation = document.querySelector('.rangoli-container');
        if (rangoliAnimation) {
            rangoliAnimation.style.visibility = 'hidden';
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
        notification.style.top = '80px';
        notification.style.right = '20px';
        notification.style.background = 'var(--arch-gradient)';
        notification.style.color = 'white';
        notification.style.padding = '12px 18px';
        notification.style.borderRadius = '8px';
        notification.style.boxShadow = '0 4px 12px var(--pink-shadow)';
        notification.style.zIndex = '10001';
        notification.style.animation = 'fadeInUp 0.5s ease';
        notification.style.fontSize = '0.9rem';
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 500);
        }, 3000);
    }
    
    // Handle background music autoplay restrictions
    document.addEventListener('click', () => {
        const backgroundMusic = document.getElementById('background-music');
        if (backgroundMusic && !musicPlaying && backgroundMusic.paused) {
            // Try to enable autoplay after user interaction
            backgroundMusic.play().then(() => {
                const musicToggle = document.getElementById('music-toggle');
                if (musicToggle) {
                    musicToggle.innerHTML = '<i class="fas fa-volume-up"></i>';
                    musicToggle.style.opacity = '1';
                    musicPlaying = true;
                }
            }).catch(() => {
                // Music autoplay still blocked
                console.log('Autoplay still blocked');
            });
        }
    }, { once: true });
    
    // Handle mobile touch interactions
    if ('ontouchstart' in window) {
        const touchElements = document.querySelectorAll('.lotus-petals, .om-symbol, .rangoli-container');
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
        const interactiveElements = document.querySelectorAll('.control-btn, .map-link, .rangoli-container');
        
        interactiveElements.forEach(element => {
            element.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    if (element.classList.contains('rangoli-container')) {
                        // Trigger rangoli interaction
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
        
        const rangoliAnimation = document.querySelector('.rangoli-container');
        if (rangoliAnimation) {
            rangoliAnimation.setAttribute('aria-label', 'Beautiful rangoli pattern animation with Om symbol - Sacred Hindu design for prosperity');
            rangoliAnimation.setAttribute('tabindex', '0');
        }
    }
    
    console.log('🏠 Griha Pravesh Invitation Loaded Successfully! ✨');
    console.log('🌺 Beautiful rangoli-om animation ready! 🕉️');
});'''

# Save the updated JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Updated app.js:")
print("1. ✅ Completely removed language toggle functionality")
print("2. ✅ Enhanced music control with error handling")
print("3. ✅ Added audio file existence checking")
print("4. ✅ Better error messages for missing audio")
print("5. ✅ Rangoli animation hover interaction")
print("6. ✅ Improved notification positioning")
print("7. ✅ Enhanced accessibility for rangoli")
print("8. ✅ Mobile touch support for rangoli")

print("\n🎵 AUDIO FILE SOLUTION:")
print("To fix the audio issue, you need to:")
print("1. Upload your audio file to GitHub repository")
print("2. Name it exactly: 'background-music.mp3'")
print("3. Place it in the same folder as index.html")
print("4. GitHub will serve it from: https://yourusername.github.io/background-music.mp3")
print("\n📁 If you have a different audio format:")
print("- Convert to MP3 format")
print("- Or update HTML src to match your filename")
print("\n🎉 ALL UPDATES COMPLETE!")
print("- Rangoli animation with golden Om center")
print("- Perfect footer centering")
print("- Corrected punctuation")
print("- No more Hindi toggle")
print("- Audio troubleshooting included")