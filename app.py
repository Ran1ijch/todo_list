from flask import Flask, render_template, request, redirect

todos = ['Спать', 'поесть', 'поспать', 'поиграть']



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', todos=todos)

@app.route("/add", methods=['POST'])
def add_todo():
    todos.append(request.form['todo'])
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index <= len(todos):
        todos.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)