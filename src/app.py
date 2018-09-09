from flask import Flask, redirect, url_for, render_template, request
 
app = Flask(__name__)
 
 




@app.route('/')
def home():
    createLink = "<a href='" + url_for('create') + "'>Create a question</a>"
    return "<html><head><title>Hello, World!</title></head><body> " + createLink + "</body></html>"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createquestion.html')
    elif request.method == 'POST':
        title = request.form['title'],
        question = request.form['question'],
        answer = request.form['answer'],
         
        

        
        return redirect(url_for('made.html', question=question))
        
    else:
        return "<h2>Invalid request</h2>"
     

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':

        question = "ask me"


        return render_template("answerquestion.html", question=question)
    elif request.method == 'POST':
        submittedanswer = request.form['submittedAnswer']


        answer = "answer me"
        if submittedanswer == answer:
            return render_template('correct.html')
        else:
            return render_template('incorrect.html', submittedanswer = submittedanswer, answer = answer)
    else:
        return '<h1>Invalid request</h1>'
 

if __name__ == '__main__':
    app.run(debug=True)