from flaskr import create_app

app = create_app()

@app.route('/health')
def health_check():
    return "Healthy", 200

