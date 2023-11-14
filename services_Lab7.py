from uow import *


def create_user(
    uow: AbstractUnitOfWork,
    name: str,
    email: str,
    password: str,
):
    with uow:
        user = User(name, email, password)
        uow.user_repository.add(user)
        uow.commit()
        return user.id

def create_collection(uow: AbstractUnitOfWork, name: str, user: User, games: List[Game]):
    with uow:
        collections = Collection(name, user, games)
        uow.collection_repository.add(collections)
        uow.commit()
        return collections.id


def create_post(
    uow: AbstractUnitOfWork,
    title: str,
    author: str,
    description: str,
    category: Category,
    recipe: Recipe
):
    with uow:
        post = Post(title, author, description, category)
        post.recipe = recipe
        uow.post_repository.add(post)
        uow.commit()
        return post.id

def create_comment(
    uow: AbstractUnitOfWork,
    username: str,
    message: str,
    date_creating: datetime.date,
    post: Post
):
    with uow:
        comment = Comment(username, message, date_creating, post)
        uow.comment_repository.add(comment)
        uow.commit()
        return comment.id

def create_game(
    uow: AbstractUnitOfWork,
    title: str,
    release_date: datetime.date,
    description: str,
    developer: Developer,
    processor: Processor,
    graphics_card: GraphicsCard,
    operating_system: OperatingSystem
):
    with uow:
        game = Game(title, release_date, description, developer, processor, graphics_card, operating_system)
        uow.game_repository.add(game)
        uow.commit()
        return game.id

def create_developer(uow: AbstractUnitOfWork, name: str):
    with uow:
        developer = Developer(name)
        uow.developer_repository.add(developer)
        uow.commit()
        return developer.id

def create_graphics_card(uow: AbstractUnitOfWork, name: str, rating: int):
    with uow:
        graphics_card = GraphicsCard(name, rating)
        uow.graphics_card_repository.add(graphics_card)
        uow.commit()
        return graphics_card.id

def create_os(uow: AbstractUnitOfWork, name: str, rating: int):
    with uow:
        os = OperatingSystem(name, rating)
        uow.os_repository.add(os)
        uow.commit()
        return os.id

def create_processor(uow: AbstractUnitOfWork, name: str, rating: int):
    with uow:
        processor = Processor(name, rating)
        uow.processor_repository.add(processor)
        uow.commit()
        return processor.id
