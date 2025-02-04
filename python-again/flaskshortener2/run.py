from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🔹 Uruchamiam aplikację Flask!")  # Debugging
    app.run(debug=True)