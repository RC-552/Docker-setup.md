from flask import Flask
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="db",  # This matches the 'db' service name in docker-compose.yml
            port="5432"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Failed: {conn}"
    return "Hello from Flask App with PostgreSQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
