import unittest
from datetime import datetime, timedelta
from models import User, Collection, Comment, Post, Game, Developer, \
    GraphicsCard, Processor, OperatingSystem, GameSearch, PostService, \
    CollectionService, GameSearchService, FriendshipService


class TestPostServiceMethods(unittest.TestCase):
    def setUp(self):
        self.post_service = PostService()

    def test_add_comment_to_post(self):
        post = Post("Title", "Content")
        user = User("user1", "user1@example.com", "password1")

        self.post_service.add_comment_to_post(post, "Comment text", user)

        self.assertEqual(len(post.comments), 1)
        self.assertEqual(post.comments[0].text, "Comment text")
        self.assertEqual(post.comments[0].user, user)

    def test_get_comments_for_post(self):
        post = Post("Title", "Content")
        user = User("user1", "user1@example.com", "password1")
        self.post_service.add_comment_to_post(post, "Comment 1", user)
        self.post_service.add_comment_to_post(post, "Comment 2", user)

        comments = self.post_service.get_comments_for_post(post)

        self.assertEqual(len(comments), 2)

    def test_get_comments_by_user(self):
        post = Post("Title", "Content")
        user1 = User("user1", "user1@example.com", "password1")
        user2 = User("user2", "user2@example.com", "password2")
        self.post_service.add_comment_to_post(post, "Comment 1", user1)
        self.post_service.add_comment_to_post(post, "Comment 2", user2)

        comments_by_user = self.post_service.get_comments_by_user(post, user1)

        self.assertEqual(len(comments_by_user), 1)
        self.assertEqual(comments_by_user[0].user, user1)

    def test_get_comments_since_date(self):
        post = Post("Title", "Content")
        user = User("user1", "user1@example.com", "password1")
        comment1 = Comment("Comment 1", user)
        comment2 = Comment("Comment 2", user)

        comment1.creation_date = datetime.now() - timedelta(days=2)
        comment1.creation_date = datetime.now() - timedelta(days=1)
        post.comments = [comment1, comment2]

        comments_since_today = self.post_service.get_comments_since_date(post,
                                                                         datetime.now())
        self.assertEqual(len(comments_since_today), 1)
        self.assertEqual(comments_since_today[0].text, "Comment 2")

        comments_since_yesterday = self.post_service.get_comments_since_date(
            post, datetime.now() - timedelta(days=2))
        self.assertEqual(len(comments_since_yesterday), 2)


class TestCollectionServiceMethods(unittest.TestCase):
    def setUp(self):
        self.collection_service = CollectionService()

    def test_create_collection(self):
        collection_name = "My Collection"
        collection = self.collection_service.create_collection(collection_name)
        self.assertEqual(collection.name, collection_name)

    def test_add_and_remove_game_from_collection(self):
        collection_name = "My Collection"
        collection = self.collection_service.create_collection(collection_name)

        developer = Developer("Developer 1")
        graphics_card = GraphicsCard("Nvidia GTX 3080", 4.8)
        processor = Processor("Intel i9-10900K", 4.5)
        os = OperatingSystem("Windows 10", 4.5)
        game = Game("Game 1", "2023-08-01", "Description 1", developer,
                    processor, graphics_card, os)

        self.collection_service.add_game_to_collection(collection, game)
        self.assertEqual(len(collection.games), 1)

        self.collection_service.remove_game_from_collection(collection, game)
        self.assertEqual(len(collection.games), 0)


class TestGameSearchServiceMethods(unittest.TestCase):
    def setUp(self):
        self.game1 = Game("Game 1", "2023-08-01", "Description 1",
                          Developer("Developer 1"),
                          Processor("Intel i9-10900K", 4.5),
                          GraphicsCard("Nvidia GTX 3080", 4.8),
                          OperatingSystem("Windows 10", 4.5))
        self.game2 = Game("Game 2", "2023-08-02", "Description 2",
                          Developer("Developer 2"),
                          Processor("AMD Ryzen 7 5800X", 4.6),
                          GraphicsCard("AMD Radeon RX 6900 XT", 4.7),
                          OperatingSystem("Linux", 4.2))
        self.game3 = Game("Game 3", "2023-08-03", "Description 3",
                          Developer("Developer 1"),
                          Processor("Intel i9-10900K", 4.5),
                          GraphicsCard("Nvidia RTX 3090", 4.9),
                          OperatingSystem("Windows 11", 4.6))
        self.games_list = [self.game1, self.game2, self.game3]

        self.search_service = GameSearchService(self.games_list)

    def test_search_games_by_developer(self):
        filtered_games = self.search_service.search_games(
            developer_name="Developer 1")
        self.assertEqual(len(filtered_games), 2)

    def test_search_games_by_graphics_card(self):
        graphics_card = GraphicsCard("Nvidia GTX 3080", 4.8)
        self.game1.graphics_card = graphics_card
        self.game2.graphics_card = graphics_card

        filtered_games = self.search_service.search_games(
            graphic_model=graphics_card)
        self.assertEqual(len(filtered_games), 2)

    def test_search_games_by_os(self):
        os = OperatingSystem("Windows 10", 4.5)
        self.game1.operating_system = os
        self.game3.operating_system = os

        filtered_games = self.search_service.search_games(os_model=os)
        self.assertEqual(len(filtered_games), 2)

    def test_search_games_by_processor(self):
        processor = Processor("Intel i9-10900K", 4.5)
        self.game1.processor = processor
        self.game3.processor = processor

        filtered_games = self.search_service.search_games(
            processor_model=processor)
        self.assertEqual(len(filtered_games), 2)


class TestFriendshipServiceMethods(unittest.TestCase):
    def setUp(self):
        self.friendship_service = FriendshipService()

    def test_add_friend(self):
        user1 = User("user1", "user1@example.com", "password1")
        user2 = User("user2", "user2@example.com", "password2")

        self.friendship_service.add_friend(user1, user2)

        self.assertIn(user2, user1.friends)

    def test_remove_friend(self):
        user1 = User("user1", "user1@example.com", "password1")
        user2 = User("user2", "user2@example.com", "password2")

        user1.friends.append(user2)
        self.friendship_service.remove_friend(user1, user2)

        self.assertNotIn(user2, user1.friends)


if __name__ == '__main__':
    unittest.main()
