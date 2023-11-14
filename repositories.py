from abc import ABC, abstractmethod
from models import *
from sqlalchemy.orm import Session
from typing import List, Optional
import xml.etree.ElementTree as Et


class abstract_repository(ABC):
    @abstractmethod
    def add_user(self, obj):
        pass

    @abstractmethod
    def get_user_by_username(self, obj):
        pass

    @abstractmethod
    def get_user_by_email(self, obj):
        pass

    @abstractmethod
    def get_all_users(self, obj):
        pass

    @abstractmethod
    def create_collection(self, obj):
        pass

    @abstractmethod
    def add_collection(self, obj):
        pass

    @abstractmethod
    def get_collection_by_user(self, obj):
        pass

    @abstractmethod
    def get_collection_by_id(self, id):
        pass

    @abstractmethod
    def delete_collection(self, obj):
        pass

    @abstractmethod
    def add_post(self, obj):
        pass

    @abstractmethod
    def get_posts_by_user(self, obj):
        pass

    @abstractmethod
    def get_post_by_id(self, id):
        pass

    @abstractmethod
    def delete_post(self, obj):
        pass

    @abstractmethod
    def get_all_posts(self, obj):
        pass

    @abstractmethod
    def add_comment(self, obj):
        pass

    @abstractmethod
    def get_comments_by_post(self, obj):
        pass

    @abstractmethod
    def get_comment_by_id(self, id):
        pass

    @abstractmethod
    def delete_comment(self, obj):
        pass

    @abstractmethod
    def get_all_comments(self, obj):
        pass

    @abstractmethod
    def add_game(self, obj):
        pass

    @abstractmethod
    def get_game_by_title(self, obj):
        pass

    @abstractmethod
    def search_games_by_developer(self, obj):
        pass

    @abstractmethod
    def search_games_by_processor(self, obj):
        pass

    @abstractmethod
    def delete_game(self, obj):
        pass

    @abstractmethod
    def get_all_games(self, obj):
        pass

    @abstractmethod
    def add_developer(self, obj):
        pass

    @abstractmethod
    def get_developer_by_name(self, obj):
        pass

    @abstractmethod
    def delete_developer(self, obj):
        pass

    @abstractmethod
    def get_all_developers(self, obj):
        pass

    @abstractmethod
    def add_graphics_card(self, obj):
        pass

    @abstractmethod
    def get_graphics_card_by_name(self, obj):
        pass

    @abstractmethod
    def delete_graphics_card(self, obj):
        pass

    @abstractmethod
    def get_all_graphics_cards(self, obj):
        pass

    @abstractmethod
    def add_processor(self, obj):
        pass

    @abstractmethod
    def get_processor_by_name(self, obj):
        pass

    @abstractmethod
    def delete_processor(self, obj):
        pass

    @abstractmethod
    def get_all_processors(self, obj):
        pass

    @abstractmethod
    def add_operating_system(self, obj):
        pass

    @abstractmethod
    def get_operating_system_by_name(self, obj):
        pass

    @abstractmethod
    def delete_operating_system(self, obj):
        pass

    @abstractmethod
    def get_all_operating_systems(self, obj):
        pass


# XML
class UserXMLRepository:
    def __init__(self, tree):
        self.root = tree.getroot()

    def add_user(self, user: User):
        users_node = self.root.find('./users')
        users_node.append(user.to_xml())

    def delete_user_by_id(self, id: int):
        xpath_expr = f".//user[@id='{id}']"
        users_node = self.root.findall(xpath_expr)
        if users_node is not None:
            for user_node in users_node:
                self.root.remove(user_node)

    def get_user_by_id(self, id: int) -> Optional[User]:
        xpath_expr = f".//user[@id='{id}']"
        user_node = self.root.find(xpath_expr)
        if user_node is None:
            return None
        return User.from_xml(user_node)

    def get_all_users(self) -> List[User]:
        users = []
        for user_node in self.root.findall('./users/user'):
            users.append(User.from_xml(user_node))
        return users


class CollectionXMLRepository:
    def __init__(self, tree, game_repository = GameXMLRepository):
        self.root = tree.getroot()
        self.game_repository = game_repository

    def add_collection(self, collection: Collection):
        collections_node = self.root.find('./collections')
        collections_node.append(collection.to_xml())

    def delete_collection_by_id(self, id: int):
        xpath_expr = f".//collection[@id='{id}']"
        collections_node = self.root.findall(xpath_expr)
        if collections_node is not None:
            for collection_node in collections_node:
                self.root.remove(collection_node)

    def get_collection_by_id(self, id: int) -> Optional[Collection]:
        xpath_expr = f".//collection[@id='{id}']"
        collection_node = self.root.find(xpath_expr)
        if collection_node is None:
            return None
        return Collection.from_xml(collection_node)

    def get_all_collections(self) -> List[Collection]:
        collections = []
        for collection_node in self.root.findall('./collections/collection'):
            collections.append(Collection.from_xml(collection_node))
        return collections


class PostXMLRepository:
    def __init__(self, tree, user_repository = UserXMLRepository):
        self.root = tree.getroot()
        self.user_repository = user_repository

    def add_post(self, post: Post):
        posts_node = self.root.find('./posts')
        posts_node.append(post.to_xml())

    def delete_post_by_id(self, id: int):
        xpath_expr = f".//post[@id='{id}']"
        posts_node = self.root.findall(xpath_expr)
        if posts_node is not None:
            for post_node in posts_node:
                self.root.remove(post_node)

    def get_post_by_id(self, id: int) -> Optional[Post]:
        xpath_expr = f".//post[@id='{id}']"
        post_node = self.root.find(xpath_expr)
        if post_node is None:
            return None
        return Post.from_xml(post_node)

    def get_all_posts(self) -> List[Post]:
        posts = []
        for post_node in self.root.findall('./posts/post'):
            posts.append(Post.from_xml(post_node))
        return posts


class CommentXMLRepository:
    def __init__(self, tree, user_repository = UserXMLRepository,
                 post_repository = PostXMLRepository):
        self.root = tree.getroot()
        self.user_repository = user_repository
        self.post_repository = post_repository

    def add_comment(self, comment: Comment):
        comments_node = self.root.find('./comments')
        comments_node.append(comment.to_xml())

    def delete_comment_by_id(self, id: int):
        xpath_expr = f".//comment[@id='{id}']"
        comments_node = self.root.findall(xpath_expr)
        if comments_node is not None:
            for comment_node in comments_node:
                self.root.remove(comment_node)

    def get_comment_by_id(self, id: int) -> Optional[Comment]:
        xpath_expr = f".//comment[@id='{id}']"
        comment_node = self.root.find(xpath_expr)
        if comment_node is None:
            return None
        return Comment.from_xml(comment_node)

    def get_all_comments(self) -> List[Comment]:
        comments = []
        for comment_node in self.root.findall('./comments/comment'):
            comments.append(Comment.from_xml(comment_node))
        return comments


class GameXMLRepository:
    def __init__(self, tree, developer_repository = DeveloperXMLRepository,
                 os_repository = OperatingSystemXMLRepository,
                 processor_repository = ProcessorXMLRepository,
                 graphics_card_repository = GraphicsCardXMLRepository):
        self.root = tree.getroot()
        self.developer_repository =developer_repository
        self.os_repository =os_repository
        self.processor_repository =processor_repository
        self.graphics_card_repository = graphics_card_repository

    def add_game(self, game: Game):
        games_node = self.root.find('./games')
        games_node.append(game.to_xml())

    def delete_game_by_id(self, id: int):
        xpath_expr = f".//game[@id='{id}']"
        games_node = self.root.findall(xpath_expr)
        if games_node is not None:
            for game_node in games_node:
                self.root.remove(game_node)

    def get_game_by_id(self, id: int) -> Optional[Game]:
        xpath_expr = f".//game[@id='{id}']"
        game_node = self.root.find(xpath_expr)
        if game_node is None:
            return None
        return Game.from_xml(game_node)

    def get_all_games(self) -> List[Game]:
        games = []
        for game_node in self.root.findall('./games/game'):
            games.append(Game.from_xml(game_node))
        return games


class DeveloperXMLRepository:
    def __init__(self, tree):
        self.root = tree.getroot()

    def add_developer(self, developer: Developer):
        developers_node = self.root.find('./developers')
        developers_node.append(developer.to_xml())

    def delete_developer_by_id(self, id: int):
        xpath_expr = f".//developer[@id='{id}']"
        developers_node = self.root.findall(xpath_expr)
        if developers_node is not None:
            for developer_node in developers_node:
                self.root.remove(developer_node)

    def get_developer_by_id(self, id: int) -> Optional[Developer]:
        xpath_expr = f".//developer[@id='{id}']"
        developer_node = self.root.find(xpath_expr)
        if developer_node is None:
            return None
        return Developer.from_xml(developer_node)

    def get_all_developers(self) -> List[Developer]:
        developers = []
        for developer_node in self.root.findall('./developers/developer'):
            developers.append(Developer.from_xml(developer_node))
        return developers


class GraphicsCardXMLRepository:
    def __init__(self, tree):
        self.root = tree.getroot()

    def add_graphics_card(self, graphics_card: GraphicsCard):
        graphics_cards_node = self.root.find('./graphics_cards')
        graphics_cards_node.append(graphics_card.to_xml())

    def delete_graphics_card_by_id(self, id: int):
        xpath_expr = f".//graphics_card[@id='{id}']"
        graphics_cards_node = self.root.findall(xpath_expr)
        if graphics_cards_node is not None:
            for graphics_card_node in graphics_cards_node:
                self.root.remove(graphics_card_node)

    def get_graphics_card_by_id(self, id: int) -> Optional[GraphicsCard]:
        xpath_expr = f".//graphics_card[@id='{id}']"
        graphics_card_node = self.root.find(xpath_expr)
        if graphics_card_node is None:
            return None
        return GraphicsCard.from_xml(graphics_card_node)

    def get_all_graphics_cards(self) -> List[GraphicsCard]:
        graphics_cards = []
        for graphics_card_node in self.root.findall(
                './graphics_cards/graphics_card'):
            graphics_cards.append(GraphicsCard.from_xml(graphics_card_node))
        return graphics_cards


class ProcessorXMLRepository:
    def __init__(self, tree):
        self.root = tree.getroot()

    def add_processor(self, processor: Processor):
        processors_node = self.root.find('./processors')
        processors_node.append(processor.to_xml())

    def delete_processor_by_id(self, id: int):
        xpath_expr = f".//processor[@id='{id}']"
        processors_node = self.root.findall(xpath_expr)
        if processors_node is not None:
            for processor_node in processors_node:
                self.root.remove(processor_node)

    def get_processor_by_id(self, id: int) -> Optional[Processor]:
        xpath_expr = f".//processor[@id='{id}']"
        processor_node = self.root.find(xpath_expr)
        if processor_node is None:
            return None
        return Processor.from_xml(processor_node)

    def get_all_processors(self) -> List[Processor]:
        processors = []
        for processor_node in self.root.findall('./processors/processor'):
            processors.append(Processor.from_xml(processor_node))
        return processors


class OperatingSystemXMLRepository:
    def __init__(self, tree):
        self.root = tree.getroot()

    def add_operating_system(self, operating_system: OperatingSystem):
        operating_systems_node = self.root.find('./operating_systems')
        operating_systems_node.append(operating_system.to_xml())

    def delete_operating_system_by_id(self, id: int):
        xpath_expr = f".//operating_system[@id='{id}']"
        operating_systems_node = self.root.findall(xpath_expr)
        if operating_systems_node is not None:
            for operating_system_node in operating_systems_node:
                self.root.remove(operating_system_node)

    def get_operating_system_by_id(self, id: int) -> Optional[OperatingSystem]:
        xpath_expr = f".//operating_system[@id='{id}']"
        operating_system_node = self.root.find(xpath_expr)
        if operating_system_node is None:
            return None
        return OperatingSystem.from_xml(operating_system_node)

    def get_all_operating_systems(self) -> List[OperatingSystem]:
        operating_systems = []
        for operating_system_node in self.root.findall(
                './operating_systems/operating_system'):
            operating_systems.append(
                OperatingSystem.from_xml(operating_system_node))
        return operating_systems


# SQLAlchemy
class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.session.query(User).filter_by(username=username).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter_by(email=email).first()

    def get_all_users(self) -> List[User]:
        return self.session.query(User).all()

    def create_collection(self, game: Game, user: User):
        collection = Collection(user_id=user.id, game_id=game.id)
        self.session.add(collection)
        self.session.commit()

    @staticmethod
    def write_post(title: str, description: str) -> Post:
        post = Post(title=title, description=description)
        return post

    @staticmethod
    def write_comment(post: Post, text: str) -> Comment:
        comment = Comment(text=text)
        post.comments.append(comment)
        self.session.commit()


class CollectionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_collection(self, collection: Collection):
        self.session.add(collection)
        self.session.commit()

    def get_collection_by_user(self, user: User) -> List[Collection]:
        return self.session.query(Collection).filter_by(user=user).all()

    def get_collection_by_id(self, collection_id: int) -> Optional[Collection]:
        return self.session.query(Collection).filter_by(
            id=collection_id).first()

    def delete_collection(self, collection: Collection):
        self.session.delete(collection)
        self.session.commit()


class PostRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_post(self, post: Post):
        self.session.add(post)
        self.session.commit()

    def get_posts_by_user(self, user_id: int) -> List[Post]:
        return self.session.query(Post).filter_by(user_id=user_id).all()

    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        return self.session.query(Post).filter_by(id=post_id).first()

    def delete_post(self, post: Post):
        self.session.delete(post)
        self.session.commit()

    def get_all_posts(self) -> List[Post]:
        return self.session.query(Post).all()


class CommentRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_comment(self, comment: Comment):
        self.session.add(comment)
        self.session.commit()

    def get_comments_by_post(self, post_id: int) -> List[Comment]:
        return self.session.query(Comment).filter_by(post_id=post_id).all()

    def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        return self.session.query(Comment).filter_by(id=comment_id).first()

    def delete_comment(self, comment: Comment):
        self.session.delete(comment)
        self.session.commit()

    def get_all_comments(self) -> List[Comment]:
        return self.session.query(Comment).all()


class GameRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_game(self, game: Game):
        self.session.add(game)
        self.session.commit()

    def get_game_by_title(self, title: str) -> Optional[Game]:
        return self.session.query(Game).filter_by(title=title).first()

    def search_games_by_developer(self, developer_name: str) -> List[Game]:
        return self.session.query(Game).join(Developer). \
            filter(Developer.name == developer_name).all()

    def search_games_by_processor(self, processor_name: str,
                                  min_rating: Optional[float] = None) -> List[
        Game]:
        if min_rating is None:
            return self.session.query(Game).join(Processor). \
                filter(Processor.name == processor_name).all()
        else:
            return self.session.query(Game).join(Processor). \
                filter(Processor.name == processor_name, Processor.rating
                       >= min_rating).all()

    def delete_game(self, game: Game):
        self.session.delete(game)
        self.session.commit()

    def get_all_games(self) -> List[Game]:
        return self.session.query(Game).all()


class DeveloperRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_developer(self, developer: Developer):
        self.session.add(developer)
        self.session.commit()

    def get_developer_by_name(self, name: str) -> Optional[Developer]:
        return self.session.query(Developer).filter_by(name=name).first()

    def delete_developer(self, developer: Developer):
        self.session.delete(developer)
        self.session.commit()

    def get_all_developers(self) -> List[Developer]:
        return self.session.query(Developer).all()


class GraphicsCardRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_graphics_card(self, graphics_card: GraphicsCard):
        self.session.add(graphics_card)
        self.session.commit()

    def get_graphics_card_by_name(self, name: str) -> Optional[GraphicsCard]:
        return self.session.query(GraphicsCard).filter_by(name=name).first()

    def delete_graphics_card(self, graphics_card: GraphicsCard):
        self.session.delete(graphics_card)
        self.session.commit()

    def get_all_graphics_cards(self) -> List[GraphicsCard]:
        return self.session.query(GraphicsCard).all()


class ProcessorRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_processor(self, processor: Processor):
        self.session.add(processor)
        self.session.commit()

    def get_processor_by_name(self, name: str) -> Optional[Processor]:
        return self.session.query(Processor).filter_by(name=name).first()

    def delete_processor(self, processor: Processor):
        self.session.delete(processor)
        self.session.commit()

    def get_all_processors(self) -> List[Processor]:
        return self.session.query(Processor).all()


class OperatingSystemRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_operating_system(self, operating_system: OperatingSystem):
        self.session.add(operating_system)
        self.session.commit()

    def get_operating_system_by_name(self, name: str) -> Optional[
        OperatingSystem]:
        return self.session.query(OperatingSystem).filter_by(name=name).first()

    def delete_operating_system(self, operating_system: OperatingSystem):
        self.session.delete(operating_system)
        self.session.commit()

    def get_all_operating_systems(self) -> List[OperatingSystem]:
        return self.session.query(OperatingSystem).all()
