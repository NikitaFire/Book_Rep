# import sqlalchemy as sa
# import datetime
# from sqlalchemy.orm import sessionmaker
# from my_sqlalchemy_script import *
# from repositories import *
#
# engine = sa.create_engine("postgresql+psycopg2://postgres:51346@localhost"
#                           ":5432/L5", echo=True)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# user_repository = UserRepository()
# collection_repository = CollectionRepository()
# post_repository = PostRepository()
# comment_repository = CommentRepository()
# game_repository = GameRepository()
# developer_repository = DeveloperRepository()
# graphics_card_repository = GraphicsCardRepository()
# processor_repository = ProcessorRepository()
# os_repository = OperatingSystemRepository()
#
# user1 = User(username='user1', email='user1@example.com', password='password1')
# user2 = User(username='user2', email='user2@example.com', password='password2')
#
# user_repository.add_user(user1)
# user_repository.add_user(user2)
#
# developer1 = Developer(name='Ubisoft')
# developer2 = Developer(name='Electronic Arts')
#
# developer_repository.add_developer(developer1)
# developer_repository.add_developer(developer2)
#
# processor1 = Processor(name='Processor 1', rating=4.5)
# processor2 = Processor(name='Processor 2', rating=4.0)
#
# processor_repository.add_processor(processor1)
# processor_repository.add_processor(processor2)
#
# os1 = OperatingSystem(name='OS 1', rating=4.6)
# os2 = OperatingSystem(name='OS 2', rating=4.3)
#
# os_repository.add_operating_system(os1)
# os_repository.add_operating_system(os2)
#
# graphics_card1 = GraphicsCard(name='Graphics Card 1', rating=4.7)
# graphics_card2 = GraphicsCard(name='Graphics Card 2', rating=4.2)
#
# graphics_card_repository.add_graphics_card(graphics_card1)
# graphics_card_repository.add_graphics_card(graphics_card2)
#
# game1 = Game(title='Game 1', release_date=datetime.date(2023, 1, 1),
#              description='Description 1')
# game2 = Game(title='Game 2', release_date=datetime.date(2023, 2, 1),
#              description='Description 2')
#
# developer1.games.append(game1)
# developer2.games.append(game2)
#
# processor1.games.append(game1)
# processor2.games.append(game2)
#
# graphics_card1.games.append(game1)
# graphics_card2.games.append(game2)
#
# os1.games.append(game1)
# os2.games.append(game2)
#
# game_repository.add_game(game1)
# game_repository.add_game(game2)
#
# collection1 = Collection(user=user1, game=game1)
# collection2 = Collection(user=user2, game=game2)
#
# collection_repository.add_collection(collection1)
# collection_repository.add_collection(collection2)
#
# post1 = Post(title='Post 1', description='Description of Post 1',
#              date=datetime.datetime.now())
# post2 = Post(title='Post 2', description='Description of Post 2',
#              date=datetime.datetime.now())
#
# user1.collections.append(collection1)
# user2.collections.append(collection2)
#
# post_repository.add_post(post1)
# post_repository.add_post(post2)
#
# comment1 = Comment(text='Comment 1 for Post 1', date=datetime.datetime.now(),
#                    post=post1)
# comment2 = Comment(text='Comment 2 for Post 2', date=datetime.datetime.now(),
#                    post=post2)
#
# comment_repository.add_comment(comment1)
# comment_repository.add_comment(comment2)
#
# for user in user_repository.users:
#     session.add(user)
#
# for collection in collection_repository.collections:
#     session.add(collection)
#
# for developer in developer_repository.developers:
#     session.add(developer)
#
# for processor in processor_repository.processors:
#     session.add(processor)
#
# for graphics_card in graphics_card_repository.graphics_cards:
#     session.add(graphics_card)
#
# for post in post_repository.posts:
#     session.add(post)
#
# for comment in comment_repository.comments:
#     session.add(comment)
#
# session.commit()
# session.close()
