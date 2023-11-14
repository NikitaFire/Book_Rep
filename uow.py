from repositories import *
from models import *

class AbstractUnitOfWork(ABC):
    user_repository: AbstractRepository
    collection_repository: AbstractRepository
    post_repository: AbstractRepository
    comment_repository: AbstractRepository
    game_repository: AbstractRepository
    developer_repository: AbstractRepository
    graphics_card_repository: AbstractRepository
    processor_repository: AbstractRepository
    os_repository: AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.user_repository = UserRepository(self.session)
        self.collection_repository = CollectionRepository(self.session)
        self.post_repository = PostRepository(self.session)
        self.comment_repository = CommentRepository(self.session)
        self.game_repository = GameRepository(self.session)
        self.developer_repository = DeveloperRepository(self.session)
        self.graphics_card_repository = GraphicsCardRepository(self.session)
        self.processor_repository = ProcessorRepository(self.session)
        self.os_repository = OperatingSystemRepository(self.session)

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

class XMLUnitOfWork(AbstractUnitOfWork):
    def __init__(self, xml_file='mrpo.xml'):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file, ET.XMLParser(encoding='UTF-8'))

    def __enter__(self):
        self.developer_repository = DeveloperXMLRepository(self.tree)
        self.graphics_card_repository = GraphicsCardXMLRepository(self.tree)
        self.processor_repository = ProcessorXMLRepository(self.tree)
        self.os_repository = OperatingSystemXMLRepository(self.tree)
        self.user_repository = UserXMLRepository(self.tree)
        self.collection_repository = CollectionXMLRepository(self.tree, self.game_repository)
        self.post_repository = PostXMLRepository(self.tree, self.user_repository)
        self.comment_repository = CommentXMLRepository(self.tree, self.user_repository,
                                                       self.post_repository)
        self.game_repository = GameXMLRepository(
            self.tree, self.developer_repository, self.os_repository, self.processor_repository,
            self.graphics_card_repository)
        return super().__enter__()

    def commit(self):
        self.tree.write(self.xml_file, encoding='UTF-8')

    def rollback(self):
        pass

class JSONUnitOfWork(AbstractUnitOfWork):
    def __init__(self, json_file='mrpo.json'):
        self.json_file = json_file
        if os.stat(self.json_file).st_size == 0:
            self.data = {"user": [],
                         "collection": [],
                         "posts": [],
                         "comments": [],
                         "game": [],
                         "developer": [],
                         "graphics_card": [],
                         "processor": [],
                         "os": []}
        else:
            with open(self.json_file, "r", encoding='utf-8') as file:
                self.data = json.load(file)

    def __enter__(self):
        self.user_repository = UserXMLRepository(self.data, self.json_file)
        self.collection_repository = CollectionXMLRepository(self.data, self.json_file)
        self.post_repository = PostXMLRepository(self.data, self.json_file)
        self.comment_repository = CommentXMLRepository(self.data, self.json_file)
        self.developer_repository = DeveloperXMLRepository(self.data, self.json_file)
        self.graphics_card_repository = GraphicsCardXMLRepository(self.data, self.json_file)
        self.processor_repository = ProcessorXMLRepository(self.data, self.json_file)
        self.os_repository = OperatingSystemXMLRepository(self.data, self.json_file)
        self.game_repository = GameXMLRepository(self.data, self.json_file)
        return super().__enter__()

    def commit(self):
        with open(self.json_file, "w", encoding='UTF-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def rollback(self):
        pass
