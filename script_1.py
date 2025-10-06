# Create the complete CSS file for the pink architectural theme
css_content = ''':root {
  /* Theme Colors Based on Pink Architectural Design */
  --primary-pink: #E91E63;
  --deep-pink: #D81B60;
  --light-pink: #F48FB1;
  --cream-bg: #FFF8E7;
  --accent-green: #4CAF50;
  --dark-green: #388E3C;
  --gold: #FFD700;
  --white: #FFFFFF;
  --dark-text: #2C1810;
  --light-gray: #F5F5F5;
  --shadow: rgba(0, 0, 0, 0.2);
  --pink-shadow: rgba(233, 30, 99, 0.3);
  
  /* Gradients */
  --arch-gradient: linear-gradient(135deg, var(--primary-pink) 0%, var(--deep-pink) 100%);
  --lotus-gradient: radial-gradient(circle, var(--light-pink) 0%, var(--primary-pink) 100%);
  --green-gradient: linear-gradient(45deg, var(--accent-green) 0%, var(--dark-green) 100%);
  
  /* Spacing */
  --container-max-width: 1200px;
  --section-padding: 4rem 0;
  --border-radius: 12px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--cream-bg);
  color: var(--dark-text);
  line-height: 1.6;
  overflow-x: hidden;
}

.container {
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 1rem;
}

.hidden {
  display: none !important;
}

/* ===== LOADING SCREEN ===== */
.loading-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, var(--cream-bg) 0%, #FFF0E6 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000;
  transition: opacity 1s ease;
}

.loading-container {
  text-align: center;
  animation: fadeInUp 1s ease;
}

.om-loader {
  font-size: 4rem;
  color: var(--primary-pink);
  animation: glow 2s ease-in-out infinite alternate;
  margin-bottom: 1rem;
  font-family: 'Noto Sans Devanagari', serif;
}

.loading-text {
  font-size: 1.2rem;
  color: var(--dark-text);
  margin-bottom: 2rem;
  opacity: 0.8;
}

.loading-dots {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
}

.loading-dots span {
  width: 12px;
  height: 12px;
  background: var(--primary-pink);
  border-radius: 50%;
  animation: bounce 1.4s ease-in-out infinite both;
}

.loading-dots span:nth-child(1) { animation-delay: -0.32s; }
.loading-dots span:nth-child(2) { animation-delay: -0.16s; }

/* ===== FLOATING CONTROLS ===== */
.floating-controls {
  position: fixed;
  top: 2rem;
  right: 2rem;
  display: flex;
  gap: 1rem;
  z-index: 1000;
}

.control-btn {
  width: 50px;
  height: 50px;
  border: none;
  border-radius: 50%;
  background: var(--arch-gradient);
  color: var(--white);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px var(--pink-shadow);
  transition: all 0.3s ease;
  font-size: 1.1rem;
}

.control-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--pink-shadow);
}

.lang-text {
  font-family: 'Noto Sans Devanagari', serif;
  font-weight: 600;
}

/* ===== HERO SECTION ===== */
.hero-section {
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  background: var(--cream-bg);
}

.background-pattern {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 20% 80%, rgba(233, 30, 99, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(76, 175, 80, 0.03) 0%, transparent 50%);
  z-index: 1;
}

/* ===== LOTUS FLOWERS ===== */
.lotus-container {
  position: absolute;
  top: 10%;
  width: 100%;
  z-index: 3;
}

.lotus {
  position: absolute;
  top: 0;
}

.left-lotus {
  left: 10%;
  animation: float 3s ease-in-out infinite;
}

.right-lotus {
  right: 10%;
  animation: float 3s ease-in-out infinite 1.5s;
}

.lotus-petals {
  font-size: 4rem;
  filter: drop-shadow(0 4px 8px rgba(233, 30, 99, 0.3));
  animation: glow 2s ease-in-out infinite alternate;
}

/* ===== MAIN ARCH STRUCTURE ===== */
.arch-container {
  position: relative;
  background: var(--arch-gradient);
  border-radius: 50px 50px 20px 20px;
  max-width: 500px;
  width: 90%;
  min-height: 700px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 2rem;
  box-shadow: 
    0 20px 40px var(--pink-shadow),
    inset 0 2px 0 rgba(255, 255, 255, 0.1);
  z-index: 2;
  
  /* Scalloped edges effect */
  background-image: 
    radial-gradient(circle at 25% 0%, transparent 20px, var(--primary-pink) 21px),
    radial-gradient(circle at 75% 0%, transparent 20px, var(--deep-pink) 21px);
}

/* ===== DECORATIVE VINES ===== */
.vine-decoration {
  position: absolute;
  top: -20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 4;
}

.left-vine {
  left: -30px;
  animation: sway 4s ease-in-out infinite;
}

.right-vine {
  right: -30px;
  animation: sway 4s ease-in-out infinite 2s;
}

.leaf {
  font-size: 2rem;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
  animation: leafRustle 3s ease-in-out infinite;
}

.leaf:nth-child(2) {
  animation-delay: 0.5s;
}

.leaf:nth-child(3) {
  animation-delay: 1s;
}

/* ===== HANGING DECORATIONS ===== */
.hanging-decorations {
  position: absolute;
  top: -10px;
  display: flex;
  gap: 20px;
  z-index: 3;
}

.bead-string {
  display: flex;
  flex-direction: column;
  gap: 5px;
  animation: hangingMotion 3s ease-in-out infinite;
}

.bead-string:nth-child(2) { animation-delay: 0.5s; }
.bead-string:nth-child(3) { animation-delay: 1s; }
.bead-string:nth-child(4) { animation-delay: 1.5s; }

.bead {
  width: 6px;
  height: 6px;
  background: var(--gold);
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* ===== OM SYMBOL ===== */
.om-symbol {
  font-family: 'Noto Sans Devanagari', serif;
  font-size: 3rem;
  color: var(--white);
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  margin-bottom: 1rem;
  animation: omGlow 3s ease-in-out infinite alternate;
}

/* ===== ARCH CONTENT ===== */
.arch-content {
  text-align: center;
  color: var(--white);
  width: 100%;
}

.invitation-text {
  font-family: 'Inter', sans-serif;
  font-size: 1.1rem;
  font-weight: 400;
  line-height: 1.4;
  margin-bottom: 2rem;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  opacity: 0.95;
}

.ceremony-title {
  font-family: 'Playfair Display', serif;
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 2rem;
  text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
  color: var(--gold);
  animation: titleGlow 2s ease-in-out infinite alternate;
}

/* ===== EVENT DETAILS ===== */
.event-details {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-align: left;
}

.detail-item i {
  font-size: 1.2rem;
  color: var(--gold);
  width: 25px;
  text-align: center;
}

.detail-text {
  font-size: 0.95rem;
  line-height: 1.3;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.map-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--gold);
  color: var(--dark-text);
  padding: 12px 24px;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 600;
  margin-top: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(255, 215, 0, 0.3);
}

.map-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 215, 0, 0.4);
  background: #FFC107;
}

/* ===== CEREMONY DETAILS SECTION ===== */
.ceremony-details {
  padding: var(--section-padding);
  background: var(--white);
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 3rem;
  color: var(--primary-pink);
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 3px;
  background: var(--arch-gradient);
  border-radius: 2px;
}

.timeline {
  display: grid;
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.timeline-item {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 2rem;
  padding: 1.5rem;
  background: var(--light-gray);
  border-radius: var(--border-radius);
  border-left: 4px solid var(--primary-pink);
  transition: transform 0.3s ease;
}

.timeline-item:hover {
  transform: translateX(5px);
}

.timeline-time {
  font-weight: 600;
  color: var(--primary-pink);
  font-size: 1.1rem;
}

.timeline-content h3 {
  color: var(--dark-text);
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.timeline-content p {
  color: var(--dark-text);
  opacity: 0.8;
}

/* ===== SIGNIFICANCE SECTION ===== */
.significance-section {
  padding: var(--section-padding);
  background: linear-gradient(135deg, #FFF8F0 0%, var(--cream-bg) 100%);
}

.significance-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 3rem;
  align-items: center;
}

.significance-text h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  color: var(--primary-pink);
  margin-bottom: 1.5rem;
}

.significance-text p {
  margin-bottom: 1.5rem;
  font-size: 1.05rem;
  line-height: 1.7;
}

.dress-code {
  background: var(--white);
  padding: 1.5rem;
  border-radius: var(--border-radius);
  border-left: 4px solid var(--accent-green);
  margin-top: 2rem;
}

.dress-code h3 {
  color: var(--accent-green);
  margin-bottom: 0.5rem;
}

.significance-visual {
  text-align: center;
}

.kalash-visual {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  background: var(--white);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(233, 30, 99, 0.1);
}

.kalash {
  font-size: 4rem;
  animation: float 3s ease-in-out infinite;
}

.kalash-leaves {
  font-size: 2rem;
  animation: sway 4s ease-in-out infinite;
}

.diya-pair {
  display: flex;
  gap: 2rem;
}

.diya {
  font-size: 2rem;
  animation: flicker 2s ease-in-out infinite alternate;
}

.diya:nth-child(2) {
  animation-delay: 0.5s;
}

/* ===== RSVP SECTION ===== */
.rsvp-section {
  padding: var(--section-padding);
  background: var(--white);
}

.rsvp-header {
  text-align: center;
  margin-bottom: 3rem;
}

.rsvp-header h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  color: var(--primary-pink);
  margin-bottom: 1rem;
}

.rsvp-header p {
  font-size: 1.1rem;
  color: var(--dark-text);
  opacity: 0.8;
}

.rsvp-form {
  max-width: 600px;
  margin: 0 auto;
  background: var(--light-gray);
  padding: 2.5rem;
  border-radius: var(--border-radius);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 1.5rem;
}

.form-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
  color: var(--dark-text);
  margin-bottom: 0.5rem;
}

.form-group label i {
  color: var(--primary-pink);
  font-size: 1rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 12px 15px;
  border: 2px solid #E0E0E0;
  border-radius: 8px;
  font-size: 1rem;
  font-family: inherit;
  transition: border-color 0.3s ease;
  background: var(--white);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-pink);
  box-shadow: 0 0 0 3px rgba(233, 30, 99, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.submit-btn {
  width: 100%;
  background: var(--arch-gradient);
  color: var(--white);
  border: none;
  padding: 15px;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--pink-shadow);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

/* ===== FORM MESSAGES ===== */
.form-message {
  text-align: center;
  padding: 2rem;
  border-radius: var(--border-radius);
  margin-top: 2rem;
}

.success-message {
  background: linear-gradient(135deg, #E8F5E8 0%, #F1F8E9 100%);
  color: var(--dark-green);
  border: 1px solid var(--accent-green);
}

.error-message {
  background: linear-gradient(135deg, #FFEBEE 0%, #FCE4EC 100%);
  color: #C62828;
  border: 1px solid #E57373;
}

.form-message i {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.form-message h3 {
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
}

/* ===== SHARE SECTION ===== */
.share-section {
  padding: var(--section-padding);
  background: linear-gradient(135deg, var(--cream-bg) 0%, #FFF0E6 100%);
  text-align: center;
}

.share-section h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  color: var(--primary-pink);
  margin-bottom: 1rem;
}

.share-section p {
  margin-bottom: 2rem;
  opacity: 0.8;
  font-size: 1.1rem;
}

.share-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.share-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 12px 20px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
  text-decoration: none;
  color: var(--white);
}

.share-btn:hover {
  transform: translateY(-2px);
}

.share-btn.whatsapp {
  background: #25D366;
  box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
}

.share-btn.whatsapp:hover {
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
}

.share-btn.email {
  background: #FF6B35;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
}

.share-btn.email:hover {
  box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
}

.share-btn.copy {
  background: var(--primary-pink);
  box-shadow: 0 4px 12px var(--pink-shadow);
}

.share-btn.copy:hover {
  box-shadow: 0 6px 20px var(--pink-shadow);
}

.share-btn.facebook {
  background: #4267B2;
  box-shadow: 0 4px 12px rgba(66, 103, 178, 0.3);
}

.share-btn.facebook:hover {
  box-shadow: 0 6px 20px rgba(66, 103, 178, 0.4);
}

/* ===== FOOTER ===== */
.footer {
  background: var(--dark-text);
  color: var(--white);
  padding: 3rem 0 1rem;
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 2rem;
}

.footer-blessing {
  text-align: center;
}

.om-small {
  font-family: 'Noto Sans Devanagari', serif;
  font-size: 2rem;
  color: var(--gold);
  margin-bottom: 1rem;
}

.footer-blessing p {
  margin-bottom: 0.5rem;
}

.footer-blessing em {
  opacity: 0.8;
  font-style: italic;
}

.footer-contact {
  text-align: center;
}

.footer-contact p {
  margin-bottom: 0.5rem;
}

.footer-contact a {
  color: var(--gold);
  text-decoration: none;
}

.footer-contact a:hover {
  text-decoration: underline;
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  opacity: 0.7;
}

/* ===== ANIMATIONS ===== */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}

@keyframes glow {
  from {
    filter: drop-shadow(0 0 5px rgba(233, 30, 99, 0.5));
  }
  to {
    filter: drop-shadow(0 0 20px rgba(233, 30, 99, 0.8));
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

@keyframes sway {
  0%, 100% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(5deg);
  }
}

@keyframes leafRustle {
  0%, 100% {
    transform: rotate(0deg) scale(1);
  }
  25% {
    transform: rotate(-2deg) scale(1.05);
  }
  75% {
    transform: rotate(2deg) scale(0.95);
  }
}

@keyframes hangingMotion {
  0%, 100% {
    transform: translateX(0px);
  }
  50% {
    transform: translateX(3px);
  }
}

@keyframes omGlow {
  from {
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  to {
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 255, 255, 0.5);
  }
}

@keyframes titleGlow {
  from {
    text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
  }
  to {
    text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3), 0 0 30px rgba(255, 215, 0, 0.3);
  }
}

@keyframes flicker {
  0%, 100% {
    filter: brightness(1) drop-shadow(0 0 5px rgba(255, 193, 7, 0.5));
  }
  50% {
    filter: brightness(1.2) drop-shadow(0 0 15px rgba(255, 193, 7, 0.8));
  }
}

/* ===== RESPONSIVE DESIGN ===== */
@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
  
  .floating-controls {
    top: 1rem;
    right: 1rem;
    gap: 0.5rem;
  }
  
  .control-btn {
    width: 45px;
    height: 45px;
    font-size: 1rem;
  }
  
  .arch-container {
    max-width: 350px;
    min-height: 600px;
    padding: 2rem 1.5rem;
  }
  
  .lotus-petals {
    font-size: 3rem;
  }
  
  .left-lotus {
    left: 5%;
  }
  
  .right-lotus {
    right: 5%;
  }
  
  .vine-decoration {
    display: none;
  }
  
  .om-symbol {
    font-size: 2.5rem;
  }
  
  .invitation-text {
    font-size: 1rem;
  }
  
  .ceremony-title {
    font-size: 2.8rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .timeline-item {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .significance-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .form-row {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .share-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .share-btn {
    width: 200px;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .arch-container {
    max-width: 320px;
    min-height: 550px;
    padding: 1.5rem 1rem;
  }
  
  .lotus-petals {
    font-size: 3rem;
  }
  
  .ceremony-title {
    font-size: 2.5rem;
  }
  
  .kalash {
    font-size: 3rem;
  }
  
  .rsvp-form {
    padding: 1.5rem;
  }
}

/* ===== ACCESSIBILITY ===== */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* High contrast mode */
@media (prefers-contrast: high) {
  .arch-container {
    border: 2px solid var(--white);
  }
  
  .detail-text,
  .invitation-text {
    text-shadow: none;
    font-weight: 600;
  }
}

/* Focus indicators for keyboard navigation */
.control-btn:focus,
.map-link:focus,
.submit-btn:focus,
.share-btn:focus {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  box-shadow: 0 0 0 3px rgba(233, 30, 99, 0.2);
}'''

# Save the CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Created style.css")
print(f"File size: {len(css_content)} characters")