# Create the updated HTML file with all the requested changes
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
                        Inviting Your Gracious Presence On<br>
                        The Occasion Of <strong>Our New Home!</strong>
                    </h1>
                    
                    <h2 class="ceremony-title">GRIHA<br>PRAVESH</h2>
                    
                    <div class="event-details">
                        <div class="detail-item">
                            <i class="fas fa-calendar-alt"></i>
                            <span class="detail-text">Sunday, 26th October, 2025<br>AT 8:00 PM</span>
                        </div>
                        
                        <div class="detail-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span class="detail-text">1004, Block, Sattva Bliss, Budigere Road,<br>Nimbekaipura Rd, off Old Madras Road,<br>Bengaluru, Karnataka 560049</span>
                        </div>
                        
                        <div class="detail-item">
                            <i class="fas fa-phone"></i>
                            <span class="detail-text">+91 8237886137</span>
                        </div>
                        
                        <a href="https://maps.app.goo.gl/w9DeHLFnaat1LC4N6" target="_blank" class="map-link compact">
                            <i class="fas fa-location-dot"></i>
                            Find my home
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

        <!-- Presence Confirmation Section -->
        <section class="confirmation-section">
            <div class="container">
                <div class="confirmation-header">
                    <h2>Please Confirm Your Presence</h2>
                </div>
                
                <div class="confirmation-content">
                    <p>Your presence will make our celebration complete!</p>
                    <p>Please let us know if you will be joining us for this auspicious occasion.</p>
                </div>
            </div>
        </section>

        <!-- Share Section -->
        <section class="share-section">
            <div class="container">
                <h2>Share all your memorable clicks here!</h2>
                
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
                        <p>भगवान इस घर में खुशियों की बरसात करें</p>
                        <p><em>May God shower happiness in this home</em></p>
                    </div>
                    
                    <div class="footer-contact">
                        <p>Please contact:</p>
                        <p>Phone: <a href="tel:+918237886137">+91 8237886137</a></p>
                    </div>
                </div>
                
                <div class="footer-bottom">
                    <p>&copy; 2025 Griha Pravesh Celebration - Made with ❤️ for our new beginning</p>
                </div>
            </div>
        </footer>
    </div>

    <script src="app.js"></script>
</body>
</html>'''

# Save the updated HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Updated index.html with all requested changes:")
print("1. ✅ 'Inviting your gracious presence On the occasion of Our New Home!' (with bold)")
print("2. ✅ Date changed to 'Sunday, 26th October, 2025'")
print("3. ✅ Address updated to Sattva Bliss, Budigere Road address")
print("4. ✅ Phone number changed to +91 8237886137")
print("5. ✅ Map button text changed to 'Find my home' (compact)")
print("6. ✅ Dress code component removed")
print("7. ✅ Changed 'attendance' to 'presence'")
print("8. ✅ RSVP form component removed")
print("9. ✅ Share section title changed to 'Share all your memorable clicks here!'")
print("10. ✅ Subtitle removed from share section")
print("11. ✅ Email link removed from footer")
print("12. ✅ Blessing changed to 'भगवान इस घर में खुशियों की बरसात करें' with English translation")
print("13. ✅ Footer contact simplified, year changed to 2025")