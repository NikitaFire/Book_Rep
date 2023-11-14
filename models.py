import datetime
import xml.etree.ElementTree as ET
from dataclasses import dataclass
import sqlalchemy as sa


class User:
    """User."""
    def __init__(self, username, email, password):
        self.id = 0
        self.username = username
        self.email = email
        self.password = password
        self.friends = []

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.email == other.email
        return False

    def create_collection(self, game):
        self.collections.append(game)

    @staticmethod
    def write_post(title, description):
        return Post(title, description)

    @staticmethod
    def write_comment(post, text):
        comment = Comment(text)
        post.add_comment(comment)
        return comment

    def to_xml(self):
        user_node = ET.Element('user')
        user_node.set('user_id', str(self.id))
        username_node = ET.SubElement(user_node, 'username')
        username_node.text = self.username
        email_node = ET.SubElement(user_node, 'email')
        email_node.text = self.email
        password_node = ET.SubElement(user_node, 'password')
        password_node.text = self.password
        return user_node


class Game:
    """Game."""

    def __init__(self, title, release_date, description, developer, processor,
                 graphics_card, operating_system):
        self.id = 0
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developer = developer
        self.processor = processor
        self.graphics_card = graphics_card
        self.operating_system = operating_system

    def __eq__(self, other):
        if isinstance(other, Game):
            return (
                self.title == other.title and
                self.release_date == other.release_date and
                self.description == other.description and
                self.developer == other.developer and
                self.processor == other.processor and
                self.graphics_card == other.graphics_card and
                self.operating_system == other.operating_system
            )
        return False

    def to_xml(self):
        game_node = ET.Element('game')
        game_node.set('game_id', str(self.id))
        title_node = ET.SubElement(game_node, 'title')
        title_node.text = self.title
        release_date_node = ET.SubElement(game_node, 'release_date')
        release_date_node.text = self.release_date
        description_node = ET.SubElement(game_node, 'description')
        description_node.text = self.description
        processor_node = ET.SubElement(game_node, 'processor')
        processor_node.text = self.processor
        graphics_card_node = ET.SubElement(game_node, 'graphics_card')
        graphics_card_node.text = self.graphics_card
        operating_system_node = ET.SubElement(game_node, 'operating_system')
        operating_system_node.text = self.operating_system
        return game_node


class Developer:
    """Developer."""

    def __init__(self, name):
        self.id = 0
        self.name = name

    def to_xml(self):
        developer_node = ET.Element('developer')
        developer_node.set('developer_id', str(self.id))
        name_node = ET.SubElement(developer_node, 'name')
        name_node.text = self.name
        return developer_node


class Processor:
    """Processor."""

    def __init__(self, name, rating):
        self.id = 0
        self.name = name
        self.rating = rating

    def to_xml(self):
        processor_node = ET.Element('processor')
        processor_node.set('processor_id', str(self.id))
        name_node = ET.SubElement(processor_node, 'name')
        name_node.text = self.name
        rating_node = ET.SubElement(processor_node, 'rating')
        rating_node.text = str(self.rating)
        return processor_node


class GraphicsCard:
    """Graphics Card."""

    def __init__(self, name, rating):
        self.id = 0
        self.name = name
        self.rating = rating

    def to_xml(self):
        graphics_card_node = ET.Element('graphics_card')
        graphics_card_node.set('graphics_card_id', str(self.id))
        name_node = ET.SubElement(graphics_card_node, 'name')
        name_node.text = self.name
        rating_node = ET.SubElement(graphics_card_node, 'rating')
        rating_node.text = str(self.rating)
        return graphics_card_node


class OperatingSystem:
    """Operating System."""

    def __init__(self, name, rating):
        self.id = 0
        self.name = name
        self.rating = rating

    def to_xml(self):
        os_node = ET.Element('os')
        os_node.set('os_id', str(self.id))
        name_node = ET.SubElement(os_node, 'name')
        name_node.text = self.name
        rating_node = ET.SubElement(os_node, 'rating')
        rating_node.text = str(self.rating)
        return os_node


class Post:
    """Post."""

    def __init__(self, title, description, date):
        self.id = 0
        self.title = title
        self.description = description
        self.date = datetime.datetime.now()
        self.comments = List[Comment] = []

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.title == other.title and \
                   self.description == other.description
        return False

    def add_comment(self, comment):
        self.comments.append(comment)

    def to_xml(self):
        post_node = ET.Element('post')
        post_node.set('post_id', str(self.id))
        title_node = ET.SubElement(post_node, 'title')
        title_node.text = self.title
        description_node = ET.SubElement(post_node, 'description')
        description_node.text = self.description
        date_node = ET.SubElement(post_node, 'date')
        date_node.text = str(self.date)
        comments_node = ET.SubElement(post_node, 'comments')
        for comment in self.comments:
            comments_node.append(comment.to_xml())
        return post_node


class Comment:
    """Post Comment."""

    def __init__(self, text, user):
        self.id = 0
        self.text = text
        self.user = user
        self.creation_date = datetime.datetime.now()

    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.text == other.text
        return False

    def to_xml(self):
        comment_node = ET.Element('comment')
        comment_node.set('id', str(self.id))
        text_node = ET.SubElement(comment_node, 'text')
        text_node.text = self.text
        date_node = ET.SubElement(comment_node, 'date')
        date_node.text = str(self.creation_date)
        return comment_node


class Collection:
    """Collection."""

    def __init__(self, name, user: User, games: Game):
        self.id = 0
        self.name = name
        self.user = user
        self.games = games

    def __eq__(self, other):
        if isinstance(other, Collection):
            return (
                    self.name == other.name and
                    self.games == other.games
            )
        return False

    def to_xml(self):
        collection_node = ET.Element('collection')
        collection_node.set('id', str(self.id))
        user_node = ET.SubElement(collection_node, 'user')
        user_node.text = str(self.user.id)
        game_node = ET.SubElement(collection_node, 'game')
        game_node.text = str(self.games.id)
        return collection_node


class GameSearch:
    def __init__(self):
        self.graphic_model = GraphicsCard
        self.os_model = OperatingSystem
        self.processor_model = Processor

    def __eq__(self, other):
        if isinstance(other, GameSearch):
            return (
                    self.graphic_model == other.graphic_model and
                    self.os_model == other.os_model and
                    self.processor_model == other.processor_model
            )
        return False
