from flask import Flask, render_template, send_from_directory, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'

# Store form submissions (in production, use a database)
form_submissions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/apartments')
def apartments():
    return render_template('apartments.html')

@app.route('/completed')
def completed():
    return render_template('completed.html')

@app.route('/ongoing')
def ongoing():
    return render_template('ongoing.html')

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')

@app.route('/joint-venture')
def joint_venture():
    return render_template('joint-venture.html')

@app.route('/real-estate-news')
def real_estate_news():
    return render_template('real-estate-news.html')

# Handle contact form submission
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        data = {
            'firstName': request.form.get('firstName'),
            'lastName': request.form.get('lastName'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'subject': request.form.get('subject'),
            'budget': request.form.get('budget'),
            'message': request.form.get('message'),
            'timestamp': datetime.now().isoformat()
        }
        form_submissions.append(data)
        return jsonify({'status': 'success', 'message': 'Form submitted successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Handle newsletter subscription
@app.route('/subscribe-newsletter', methods=['POST'])
def subscribe_newsletter():
    try:
        email = request.form.get('email')
        # In production, save to database or send to email service
        return jsonify({'status': 'success', 'message': 'Subscribed successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Admin route to view submissions (basic)
@app.route('/admin/submissions')
def admin_submissions():
    return jsonify(form_submissions)

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/<path:filename>')
def serve_root_files(filename):
    if os.path.exists(os.path.join(app.static_folder, filename)):
        return send_from_directory(app.static_folder, filename)
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1907)