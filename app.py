from flask import Flask ,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///D:/sqlite/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
    
        with app.app_context():
            upload = Upload(filename=file.filename, data=file.read())
            db.session.add(upload)
            db.session.commit()
        
        return f'Uploaded: {file.filename}'
    return "upload the file"



if __name__ == '__main__':
    app.run(debug=True)
