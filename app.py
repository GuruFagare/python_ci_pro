from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def invitation():
    host_name = "Sushant & Family"
    event_date = "15 August 2025"
    event_time = "5:00 PM"
    venue = "Shree Ganesh Mandir, Pune"
    message = """
    We cordially invite you and your family to join us for the auspicious
    occasion of Satyanarayan Pooja, followed by Prasad and dinner.
    """

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Satyanarayan Pooja Invitation</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #fff8e7;
                text-align: center;
                padding: 20px;
            }}
            .card {{
                border: 2px solid #d4af37;
                border-radius: 15px;
                background-color: #fffaf0;
                padding: 20px;
                width: 60%;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #a0522d;
            }}
            h2 {{
                color: #8b0000;
            }}
            p {{
                font-size: 18px;
                color: #333;
            }}
            .footer {{
                margin-top: 20px;
                font-style: italic;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🙏 Satyanarayan Pooja Invitation 🙏</h1>
            <h2>Hosted by {host_name}</h2>
            <p>{message}</p>
            <p><b>Date:</b> {event_date}</p>
            <p><b>Time:</b> {event_time}</p>
            <p><b>Venue:</b> {venue}</p>
            <div class="footer">
                <p>We look forward to your presence and blessings.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
