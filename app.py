from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('todo.db')
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, content TEXT)')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    conn = sqlite3.connect('todo.db')
    conn.execute('INSERT INTO tasks (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return redirect('/')
#port
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
