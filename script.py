# Create the complete HTML file for the pink architectural Griha Pravesh invitation
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Griha Pravesh - New Home Blessing Ceremony</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;900&family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Loading Screen -->
    <div id="loading-screen" class="loading-screen">
        <div class="loading-container">
            <div class="om-loader">ॐ</div>
            <div class="loading-text">Welcome to our new home celebration</div>
            <div class="loading-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </div>

    <!-- Floating Controls -->
    <div class="floating-controls">
        <button id="music-toggle" class="control-btn" title="Toggle Background Music">
            <i class="fas fa-music"></i>
        </button>
        <button id="lang-toggle" class="control-btn" title="Switch Language">
            <span class="lang-text">हिं</span>
        </button>
    </div>

    <!-- Background Music -->
    <audio id="background-music" loop>
        <source src="https://www.soundjay.com/misc/sounds/magic-chime-02.mp3" type="audio/mpeg">
        <source src="https://www.zapsplat.com/music/temple-bell-single-ring-2/" type="audio/ogg">
    </audio>

    <!-- Main Content -->
    <div id="main-content" class="main-content hidden">
        <!-- Hero Section with Architectural Arch -->
        <section class="hero-section">
            <div class="background-pattern"></div>
            
            <!-- Lotus Flowers -->
            <div class="lotus-container">
                <div class="lotus left-lotus">
                    <div class="lotus-petals">🌸</div>
                </div>
                <div class="lotus right-lotus">
                    <div class="lotus-petals">🌸</div>
                </div>
            </div>

            <!-- Main Arch Structure -->
            <div class="arch-container">
                <!-- Green Decorative Vines -->
                <div class="vine-decoration left-vine">
                    <span class="leaf">🍃</span>
                    <span class="leaf">🍂</span>
                    <span class="leaf">🍃</span>
                </div>
                <div class="vine-decoration right-vine">
                    <span class="leaf">🍃</span>
                    <span class="leaf">🍂</span>
                    <span class="leaf">🍃</span>
                </div>

                <!-- Hanging Decorations -->
                <div class="hanging-decorations">
                    <div class="bead-string">
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                    </div>
                    <div class="bead-string">
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                    </div>
                    <div class="bead-string">
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                    </div>
                    <div class="bead-string">
                        <span class="bead"></span>
                        <span class="bead"></span>
                        <span class="bead"></span>
                    </div>
                </div>

                <!-- Om Symbol -->
                <div class="om-symbol">ॐ</div>

                <!-- Main Content Inside Arch -->
                <div class="arch-content">
                    <h1 class="invitation-text">
                        Invite Your Gracious Presence On<br>
                        The Occasion Of Their New Home's
                    </h1>
                    
                    <h2 class="ceremony-title">GRIHA<br>PRAVESH</h2>
                    
                    <div class="event-details">
                        <div class="detail-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span class="detail-text">Saturday, November 16th, 2024<br>AT 8:00 PM</span>
                        </div>
                        
                        <div class="detail-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span class="detail-text">445 W. Mount Eden Road,<br>Anchorage, AK 99504</span>
                        </div>
                        
                        <div class="detail-item">
                            <i class="fas fa-phone"></i>
                            <span class="detail-text">+1 123 456 789</span>
                        </div>
                        
                        <a href="https://maps.app.goo.gl/w9DeHLFnaat1LC4N6" target="_blank" class="map-link">
                            <i class="fas fa-location-dot"></i>
                            Find my home!
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Ceremony Details Section -->
        <section class="ceremony-details">
            <div class="container">
                <h2 class="section-title">शुभ विवाह - Ceremony Timeline</h2>
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-time">8:00 PM</div>
                        <div class="timeline-content">
                            <h3>Ganesha Puja & Welcome</h3>
                            <p>Invoking Lord Ganesha's blessings for the new home</p>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">8:30 PM</div>
                        <div class="timeline-content">
                            <h3>Kalash Sthapana</h3>
                            <p>Sacred pot ceremony for prosperity and abundance</p>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">9:00 PM</div>
                        <div class="timeline-content">
                            <h3>Griha Pravesh Ceremony</h3>
                            <p>First sacred entry into the new home with family</p>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-time">9:30 PM</div>
                        <div class="timeline-content">
                            <h3>Dinner & Celebrations</h3>
                            <p>Community feast and joyful celebrations with all guests</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Cultural Significance Section -->
        <section class="significance-section">
            <div class="container">
                <div class="significance-content">
                    <div class="significance-text">
                        <h2>About Griha Pravesh</h2>
                        <p>Griha Pravesh is a sacred Hindu ceremony performed when entering a new home for the first time. This auspicious ritual involves prayers for prosperity, peace, and positive energy in the new dwelling.</p>
                        <p>The ceremony includes invoking Lord Ganesha to remove obstacles, performing Vastu Shanti for harmonizing the space with natural elements, and seeking blessings from elders and deities for a happy and prosperous life in the new home.</p>
                        
                        <div class="dress-code">
                            <h3>Dress Code</h3>
                            <p>Traditional Indian attire is preferred. Please wear bright, auspicious colors like red, gold, green, or yellow.</p>
                        </div>
                    </div>
                    
                    <div class="significance-visual">
                        <div class="kalash-visual">
                            <div class="kalash">🏺</div>
                            <div class="kalash-leaves">🍿🥭🍿</div>
                            <div class="diya-pair">
                                <span class="diya">🪔</span>
                                <span class="diya">🪔</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- RSVP Form Section -->
        <section class="rsvp-section">
            <div class="container">
                <div class="rsvp-header">
                    <h2>Please Confirm Your Attendance</h2>
                    <p>Your presence will make our celebration complete!</p>
                </div>
                
                <form id="rsvp-form" class="rsvp-form" action="https://formspree.io/f/xrbznbzw" method="POST">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="guest_name">
                                <i class="fas fa-user"></i>
                                Your Name *
                            </label>
                            <input type="text" id="guest_name" name="guest_name" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">
                                <i class="fas fa-envelope"></i>
                                Email Address *
                            </label>
                            <input type="email" id="email" name="email" required>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="phone">
                                <i class="fas fa-phone"></i>
                                Phone Number
                            </label>
                            <input type="tel" id="phone" name="phone">
                        </div>
                        
                        <div class="form-group">
                            <label for="guests_count">
                                <i class="fas fa-users"></i>
                                Number of Guests *
                            </label>
                            <select id="guests_count" name="guests_count" required>
                                <option value="">Select number of guests</option>
                                <option value="1">1 Guest</option>
                                <option value="2">2 Guests</option>
                                <option value="3">3 Guests</option>
                                <option value="4">4 Guests</option>
                                <option value="5+">5+ Guests</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="dietary_preferences">
                            <i class="fas fa-utensils"></i>
                            Dietary Preferences
                        </label>
                        <select id="dietary_preferences" name="dietary_preferences">
                            <option value="">No specific preferences</option>
                            <option value="vegetarian">Vegetarian</option>
                            <option value="vegan">Vegan</option>
                            <option value="jain">Jain Vegetarian</option>
                            <option value="gluten-free">Gluten-free</option>
                            <option value="other">Other (please specify in message)</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="special_message">
                            <i class="fas fa-comment"></i>
                            Special Message or Requests
                        </label>
                        <textarea id="special_message" name="special_message" rows="4" placeholder="Any special requests or blessings for the new home..."></textarea>
                    </div>
                    
                    <!-- Hidden field for form identification -->
                    <input type="hidden" name="_subject" value="New RSVP for Griha Pravesh Ceremony">
                    <input type="hidden" name="_next" value="#thank-you">
                    <input type="hidden" name="_captcha" value="false">
                    
                    <button type="submit" class="submit-btn">
                        <i class="fas fa-paper-plane"></i>
                        <span class="btn-text">Send RSVP</span>
                        <span class="loading-spinner hidden">
                            <i class="fas fa-spinner fa-spin"></i>
                        </span>
                    </button>
                </form>
                
                <!-- Success/Error Messages -->
                <div id="form-success" class="form-message success-message hidden">
                    <i class="fas fa-check-circle"></i>
                    <h3>Thank You!</h3>
                    <p>Your RSVP has been received. We look forward to celebrating with you!</p>
                </div>
                
                <div id="form-error" class="form-message error-message hidden">
                    <i class="fas fa-exclamation-triangle"></i>
                    <h3>Oops! Something went wrong</h3>
                    <p>Please try again or contact us directly at +1 123 456 789</p>
                </div>
            </div>
        </section>

        <!-- Share Section -->
        <section class="share-section">
            <div class="container">
                <h2>Share The Celebration</h2>
                <p>Help us spread the joy by sharing this invitation</p>
                
                <div class="share-buttons">
                    <button class="share-btn whatsapp" onclick="shareInvitation('whatsapp')">
                        <i class="fab fa-whatsapp"></i>
                        WhatsApp
                    </button>
                    <button class="share-btn email" onclick="shareInvitation('email')">
                        <i class="fas fa-envelope"></i>
                        Email
                    </button>
                    <button class="share-btn copy" onclick="copyInvitationLink()">
                        <i class="fas fa-copy"></i>
                        Copy Link
                    </button>
                    <button class="share-btn facebook" onclick="shareInvitation('facebook')">
                        <i class="fab fa-facebook"></i>
                        Facebook
                    </button>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-blessing">
                        <div class="om-small">ॐ</div>
                        <p>मय भगवान आपके नए घर में खुशियां की बरसात करें</p>
                        <p><em>May God shower happiness in your new home</em></p>
                    </div>
                    
                    <div class="footer-contact">
                        <p>For any queries, please contact:</p>
                        <p><strong>The Sharma Family</strong></p>
                        <p>Phone: <a href="tel:+11234567890">+1 123 456 789</a></p>
                        <p>Email: <a href="mailto:family@example.com">family@example.com</a></p>
                    </div>
                </div>
                
                <div class="footer-bottom">
                    <p>&copy; 2024 Griha Pravesh Celebration - Made with ❤️ for our new beginning</p>
                </div>
            </div>
        </footer>
    </div>

    <script src="app.js"></script>
</body>
</html>'''

# Save the HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Created index.html")
print(f"File size: {len(html_content)} characters")