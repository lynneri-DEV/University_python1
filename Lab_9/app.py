from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Временное хранилище задач
tasks = [
    {"id": 1, "title": "Сдать лабораторную №9", "done": False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get('title')
    if task_title:
        new_id = len(tasks) + 1 if tasks else 1
        tasks.append({"id": new_id, "title": task_title, "done": False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)