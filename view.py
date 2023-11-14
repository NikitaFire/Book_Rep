from uow import *

def get_collection_by_id(id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        collection = uow.collection_repository.get_by_id(id)
        return collection.to_dict()

def get_collection_games_by_post_id(id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        collection = uow.collection_repository.get_by_id(id)
        games = uow.game_repository.get_all()
        games = [game for game in games if game.collection == collection]
        return [game.to_dict() for game in games]

def get_all_collections(uow: SqlAlchemyUnitOfWork):
    with uow:
        collections = uow.collection_repository.get_all()
        return [collection.to_dict() for collection in collections]
