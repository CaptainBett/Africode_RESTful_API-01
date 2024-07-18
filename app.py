from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse,fields,abort,marshal_with


# Start your Flask application here
app = Flask(__name__)
api = Api(app)

# Set up SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Define your models here
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'User: {self.username} {self.email}'
    
app.app_context().push()
db.create_all()

user_args = reqparse.RequestParser() 
user_args.add_argument('username', type=str, required=True, help='Username is required')
user_args.add_argument('email', type=str, required=True, help='Email is required')

userFields = {"id":fields.Integer,"username":fields.String,"email":fields.String}



# Define your API resources here
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users, 200

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(username=args['username'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        return user, 201
    
api.add_resource(Users,'/api/users/')

class User(Resource):
    @marshal_with(userFields)
    def get(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message='User not found!')
        return user
    
    @marshal_with(userFields)
    def patch(self,id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message='User not found!')
        user.username = args['username'] 
        user.email = args['email'] 
        db.session.commit()
        return user
    @marshal_with(userFields)
    def delete(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message='User not found!')
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users

api.add_resource(User,'/api/users/<int:id>')

@app.route('/')
def home():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)
 