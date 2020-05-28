from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    about_me = db.Column(db.String(240))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
        
    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def team_posts(self):
        created = Post.query.filter_by(team_id=self.team_id)
        return created.order_by(Post.timestamp.desc())

class Post(db.Model):  
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)  


class Team(db.Model):
    __tablename__='teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    members = db.relationship('User', backref='team_members')
    team_posts = db.relationship('Post', backref='team_posts')
    

    @staticmethod
    def insert_teams():
        """Populates teams
            Upon first time implementation run Team.insert_teams() to populate the user teams
            To change the team name just alter the teams variable
        """

        teams = ['team1', 'team2', 'team3']
        for t in teams:
            team = Team.query.filter_by(name=t).first()
            if team is None:
                team = Team(name=t)
            db.session.add(team)
        db.session.commit()


class Position(db.Model):
    __tablename__='position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    members = db.relationship('User', backref='position_members')

    @staticmethod
    def insert_position():
        """Populates positions
            Upon first time implementation run Position.insert_position() to populate the user positions
            To change the position name just alter the positions variable
        """

        positions = ['Front-end', 'Back-end', 'Full-stack', 'Product Manager']
        for p in positions:
            position = Position.query.filter_by(name=p).first()
            if position is None:
                position = Position(name=p)
            db.session.add(position)
        db.session.commit()



@login.user_loader
def load_user(id):
    return User.query.get(int(id))