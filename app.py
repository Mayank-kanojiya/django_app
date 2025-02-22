from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        # Get system information
        name = "Mayank Kanojia"  # Replace with your full name
        username = os.environ.get('USER') or os.environ.get('USERNAME') or "unknown"
        ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
        top_output = subprocess.getoutput('ps aux')  # Use ps if top is not available

        # Format the HTML response
        response = f"""
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
        """
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)