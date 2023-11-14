import datetime
from dataclasses import dataclass
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)

    collections = sa.orm.relationship('Collection', back_populates='user')


class Game(Base):
    __tablename__ = 'games'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    release_date = sa.Column(sa.Date, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    developer_id = sa.Column(sa.Integer, sa.ForeignKey('developers.id'))
    processor_id = sa.Column(sa.Integer, sa.ForeignKey('processors.id'))
    graphics_card_id = sa.Column(sa.Integer, sa.ForeignKey('graphics_cards.id'))
    operating_system_id = sa.Column(sa.Integer, sa.ForeignKey('operating_'
                                                              'systems.id'))

    developer = sa.orm.relationship('Developer', back_populates='games')
    processor = sa.orm.relationship('Processor', back_populates='games')
    graphics_card = sa.orm.relationship('GraphicsCard', back_populates='games')
    operating_system = sa.orm.relationship('OperatingSystem',
                                           back_populates='games')


class Developer(Base):
    __tablename__ = 'developers'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    games = sa.orm.relationship('Game', back_populates='developer')


class Processor(Base):
    __tablename__ = 'processors'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    rating = sa.Column(sa.Float, nullable=False)
    games = sa.orm.relationship('Game', back_populates='processor')


class GraphicsCard(Base):
    __tablename__ = 'graphics_cards'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    rating = sa.Column(sa.Float, nullable=False)
    games = sa.orm.relationship('Game', back_populates='graphics_card')


class OperatingSystem(Base):
    __tablename__ = 'operating_systems'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    rating = sa.Column(sa.Float, nullable=False)
    games = sa.orm.relationship('Game', back_populates='operating_system')


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    date = sa.Column(sa.DateTime, default=datetime.datetime.now(), nullable=False)
    comments = sa.orm.relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String, nullable=False)
    date = sa.Column(sa.DateTime, default=datetime.datetime.now, nullable=False)
    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id'))
    post = sa.orm.relationship('Post', back_populates='comments')


class Collection(Base):
    __tablename__ = 'collections'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    game_id = sa.Column(sa.Integer, sa.ForeignKey('games.id'))

    user = sa.orm.relationship('User', back_populates='collections')
    game = sa.orm.relationship('Game')

    def add_game(self, game):
        self.game = game


class GameSearch:
    def __init__(self):
        self.genre_model = Genre
        self.graphic_model = GraphicsCard
        self.os_model = OperatingSystem
        self.processor_model = Processor


engine = sa.create_engine("postgresql+psycopg2://postgres:51346@localhost"
                          ":5432/L5", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
