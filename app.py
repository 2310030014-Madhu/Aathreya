from flask import Flask, render_template, request, flash, redirect, url_for
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this in production

# Configuration
app.config['DEBUG'] = True  # Set to False in production

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


# Optional: Add a simple contact form handler if needed in the future
@app.route('/contact', methods=['POST'])
def contact_form():
    """Handle contact form submissions (if you add a form later)"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, just flash a message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Optional: Add a simple newsletter signup
@app.route('/newsletter', methods=['POST'])
def newsletter_signup():
    """Handle newsletter signups"""
    email = request.form.get('email')
    if email:
        # Here you would save the email to your newsletter list
        flash('Thank you for subscribing to our newsletter!', 'success')
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)