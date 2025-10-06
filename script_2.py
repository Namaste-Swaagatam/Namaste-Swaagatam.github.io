# Create the complete JavaScript file for the pink architectural theme
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
            initializeRSVPForm();
            initializeScrollAnimations();
            initializeSharingFeatures();
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
        
        // Initialize diya flicker effects
        const diyas = document.querySelectorAll('.diya');
        diyas.forEach((diya, index) => {
            diya.addEventListener('click', () => {
                diya.style.animation = 'flicker 0.5s ease';
                setTimeout(() => {
                    diya.style.animation = 'flicker 2s ease-in-out infinite alternate';
                    if (index === 1) {
                        diya.style.animationDelay = '0.5s';
                    }
                }, 500);
            });
        });
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
                'invitation-text': 'Invite Your Gracious Presence On<br>The Occasion Of Their New Home\\'s',
                'ceremony-title': 'GRIHA<br>PRAVESH',
                'section-timeline': 'Ceremony Timeline',
                'about-title': 'About Griha Pravesh',
                'rsvp-title': 'Please Confirm Your Attendance',
                'rsvp-subtitle': 'Your presence will make our celebration complete!',
                'share-title': 'Share The Celebration',
                'lang-text': 'हिं'
            },
            hi: {
                'invitation-text': 'हमारे नए घर के<br>गृह प्रवेश समारोह में<br>आपकी उपस्थिति का सम्मान',
                'ceremony-title': 'गृह<br>प्रवेश',
                'section-timeline': 'समारोह कार्यक्रम',
                'about-title': 'गृह प्रवेश के बारे में',
                'rsvp-title': 'कृपया अपनी उपस्थिति की पुष्टि करें',
                'rsvp-subtitle': 'आपकी उपस्थिति से हमारा उत्सव पूर्ण होगा!',
                'share-title': 'उत्सव साझा करें',
                'lang-text': 'EN'
            }
        };
        
        const elements = {
            'invitation-text': document.querySelector('.invitation-text'),
            'ceremony-title': document.querySelector('.ceremony-title'),
            'section-timeline': document.querySelector('.section-title'),
            'about-title': document.querySelector('.significance-text h2'),
            'rsvp-title': document.querySelector('.rsvp-header h2'),
            'rsvp-subtitle': document.querySelector('.rsvp-header p'),
            'share-title': document.querySelector('.share-section h2'),
            'lang-text': document.querySelector('.lang-text')
        };
        
        Object.keys(elements).forEach(key => {
            if (elements[key] && translations[currentLanguage][key]) {
                elements[key].innerHTML = translations[currentLanguage][key];
            }
        });
    }
    
    function initializeRSVPForm() {
        const form = document.getElementById('rsvp-form');
        const submitBtn = document.querySelector('.submit-btn');
        const successMessage = document.getElementById('form-success');
        const errorMessage = document.getElementById('form-error');
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Show loading state
            const btnText = submitBtn.querySelector('.btn-text');
            const spinner = submitBtn.querySelector('.loading-spinner');
            
            submitBtn.disabled = true;
            btnText.style.display = 'none';
            spinner.classList.remove('hidden');
            
            try {
                // Get form data
                const formData = new FormData(form);
                
                // Add timestamp
                formData.append('submission_time', new Date().toLocaleString());
                
                // Submit to Formspree
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    // Success
                    form.style.display = 'none';
                    successMessage.classList.remove('hidden');
                    
                    // Reset form after delay
                    setTimeout(() => {
                        form.reset();
                        form.style.display = 'block';
                        successMessage.classList.add('hidden');
                        resetSubmitButton();
                    }, 5000);
                    
                    // Show celebration animation
                    showCelebrationAnimation();
                    
                } else {
                    throw new Error('Form submission failed');
                }
                
            } catch (error) {
                console.error('Form submission error:', error);
                errorMessage.classList.remove('hidden');
                setTimeout(() => {
                    errorMessage.classList.add('hidden');
                }, 5000);
                resetSubmitButton();
            }
        });
        
        function resetSubmitButton() {
            const btnText = submitBtn.querySelector('.btn-text');
            const spinner = submitBtn.querySelector('.loading-spinner');
            
            submitBtn.disabled = false;
            btnText.style.display = 'inline';
            spinner.classList.add('hidden');
        }
        
        // Form validation
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            field.addEventListener('blur', () => {
                validateField(field);
            });
            
            field.addEventListener('input', () => {
                if (field.classList.contains('invalid')) {
                    validateField(field);
                }
            });
        });
        
        function validateField(field) {
            if (!field.value.trim()) {
                field.classList.add('invalid');
                field.style.borderColor = '#E57373';
            } else {
                field.classList.remove('invalid');
                field.style.borderColor = '#E0E0E0';
            }
        }
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
                }
            });
        }, observerOptions);
        
        // Observe sections for scroll animations
        const sections = document.querySelectorAll('.ceremony-details, .significance-section, .rsvp-section, .share-section');
        sections.forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(30px)';
            section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            observer.observe(section);
        });
        
        // Observe timeline items
        const timelineItems = document.querySelectorAll('.timeline-item');
        timelineItems.forEach((item, index) => {
            item.style.opacity = '0';
            item.style.transform = 'translateX(-30px)';
            item.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
            observer.observe(item);
        });
    }
    
    function initializeSharingFeatures() {
        // This will be called from HTML onclick events
        window.shareInvitation = function(platform) {
            const url = window.location.href;
            const text = 'Join us for our Griha Pravesh ceremony! 🏠✨';
            
            switch(platform) {
                case 'whatsapp':
                    window.open(`https://wa.me/?text=${encodeURIComponent(text + ' ' + url)}`, '_blank');
                    break;
                case 'email':
                    window.open(`mailto:?subject=${encodeURIComponent('Griha Pravesh Invitation')}&body=${encodeURIComponent(text + '\\n\\n' + url)}`, '_blank');
                    break;
                case 'facebook':
                    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
                    break;
            }
        };
        
        window.copyInvitationLink = function() {
            navigator.clipboard.writeText(window.location.href).then(() => {
                showNotification('Invitation link copied to clipboard!');
            }).catch(() => {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = window.location.href;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                showNotification('Invitation link copied!');
            });
        };
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
        
        // Continuous kalash float
        const kalash = document.querySelector('.kalash');
        if (kalash) {
            kalash.style.animation = 'float 3s ease-in-out infinite';
        }
    }
    
    function showCelebrationAnimation() {
        // Create celebration effect
        const celebration = document.createElement('div');
        celebration.style.position = 'fixed';
        celebration.style.top = '0';
        celebration.style.left = '0';
        celebration.style.width = '100%';
        celebration.style.height = '100%';
        celebration.style.pointerEvents = 'none';
        celebration.style.zIndex = '10000';
        celebration.innerHTML = '🎉🌸🎊🌺🎉🌸🎊🌺';
        celebration.style.fontSize = '2rem';
        celebration.style.display = 'flex';
        celebration.style.justifyContent = 'center';
        celebration.style.alignItems = 'center';
        celebration.style.animation = 'fadeInUp 1s ease, glow 2s ease-in-out infinite alternate';
        
        document.body.appendChild(celebration);
        
        setTimeout(() => {
            celebration.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(celebration);
            }, 1000);
        }, 3000);
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
    
    // Handle form field animations
    const formInputs = document.querySelectorAll('.form-group input, .form-group select, .form-group textarea');
    formInputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentElement.style.transform = 'scale(1.02)';
            input.parentElement.style.transition = 'transform 0.3s ease';
        });
        
        input.addEventListener('blur', () => {
            input.parentElement.style.transform = 'scale(1)';
        });
    });
    
    // Handle mobile touch interactions
    if ('ontouchstart' in window) {
        const touchElements = document.querySelectorAll('.lotus-petals, .diya, .om-symbol');
        touchElements.forEach(element => {
            element.addEventListener('touchstart', () => {
                element.style.transform = 'scale(1.1)';
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
        const interactiveElements = document.querySelectorAll('.control-btn, .map-link, .submit-btn, .share-btn');
        
        interactiveElements.forEach(element => {
            element.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    element.click();
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
        
        // Announce form submission status to screen readers
        const formMessages = document.querySelectorAll('.form-message');
        formMessages.forEach(message => {
            message.setAttribute('role', 'status');
            message.setAttribute('aria-live', 'polite');
        });
    }
    
    console.log('🏠 Griha Pravesh Invitation Loaded Successfully! ✨');
    console.log('🌸 May this new home bring joy and prosperity! 🙏');
});'''

# Save the JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Created app.js")
print(f"File size: {len(js_content)} characters")

print("\n🎉 ALL FILES READY FOR GITHUB UPLOAD!")
print("\n📁 Files created:")
print("1. index.html - Main invitation page")
print("2. style.css - Pink architectural styling")  
print("3. app.js - Interactive functionality")

print("\n🚀 NEXT STEPS:")
print("1. Go to your GitHub repository")
print("2. Upload these 3 files (drag & drop or use 'Add file' > 'Upload files')")
print("3. Commit the changes")
print("4. Your invitation will be live at: https://vithikaa.github.io")

print("\n📧 EMAIL SETUP:")
print("1. Sign up at formspree.io (free)")
print("2. Create a form and get your form ID")
print("3. Replace 'xrbznbzw' in index.html with your form ID")
print("4. Start receiving RSVP responses via email!")

print("\n🎨 Features included:")
print("✅ Pink architectural arch design (matches your image)")
print("✅ Lotus flowers with animations")
print("✅ Green decorative vines")
print("✅ Om symbol with glow effects")
print("✅ Map link: 'Find my home!' -> https://maps.app.goo.gl/w9DeHLFnaat1LC4N6")
print("✅ RSVP form with email functionality")
print("✅ Mobile responsive design")
print("✅ Background music toggle")
print("✅ Language switcher (English/Hindi)")
print("✅ Social sharing buttons")
print("✅ All ceremony sections preserved")