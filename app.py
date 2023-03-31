from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Usuario\\Documents\\Python Scripts\\Blog con python\\archivo.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

