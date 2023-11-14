from models import *
from serializer import ObjectSerializer

serializer = ObjectSerializer()

developer = Developer(name = 'EA')
developer.id = 2

processor = Processor(name = "Intel i5", rating = 8)
processor.id = 5

graphics_card = GraphicsCard(name = "Nvidia", rating = 9)
graphics_card.id = 7

os = OperatingSystem(name = "Windows 11", rating = 9)
os.id = 1

game = Game(title = "Apex", release_date = 10.05, description = "The Best game"
            , developer = developer, processor = processor, graphics_card =
            graphics_card, operating_system = os)

game.operating_system = os

transform = 'JSON'
output = serializer.serialize(game, transform)
print(output)

print(next(game.status('Delete Game')))

