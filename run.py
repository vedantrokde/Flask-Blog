from blog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# ============================================
# runing app in debug mode using flask command
# $env:FLASK_APP = "app"
# $env:FLASK_ENV = "development"
# flask run
# -by default app remains in production mode
# ============================================