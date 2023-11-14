from flask import Flask, request, redirect, render_template, jsonify
from services import *

app = Flask(__name__)

@app.route('/create_user', methods=['GET', 'POST'])
def cr_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        uow = SqlAlchemyUnitOfWork()
        user_id = create_user(uow, username, email, password)

        return redirect('/create_collection', code=301, Response=None)
    else:
        return render_template('create_user.html')

@app.route('/create_collection', methods=['GET', 'POST'])
def cr_collection():
    if request.method == 'POST':
        name = request.form['name']


        uow = SqlAlchemyUnitOfWork()
        user = uow.user_repository.get_by_id(1)
        games = uow.game_repository.get_all()

        collection_id = create_collection(uow, name, user, games)

        return redirect('/create_post', code=301, Response=None)
    else:
        return render_template('create_collection.html')

@app.route('/create_post', methods=['GET', 'POST'])
def cr_post():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        description = request.form['description']

        uow = SqlAlchemyUnitOfWork()
        category = uow.category_repository.get_by_id(1)
        recipe = uow.recipe_repository.get_by_id(1)

        post_id = create_post(uow, name, author, description, category, recipe)

        return redirect(f'/posts/{post_id}', code=301, Response=None)
    else:
        return render_template('create_post.html')

@app.route('/create_comment', methods=['GET', 'POST'])
def cr_comment():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        date_creating = datetime.date.today()

        uow = SqlAlchemyUnitOfWork()
        post = uow.post_repository.get_by_id(1)

        comment_id = create_comment(uow, username, message, date_creating, post)

        return redirect(f'/posts/{post.id}', code=301, Response=None)
    else:
        return render_template('create_comment.html')

@app.route('/create_game', methods=['GET', 'POST'])
def cr_game():
    if request.method == 'POST':
        title = request.form['title']
        release_date = request.form['release_date']
        description = request.form['description']

        uow = SqlAlchemyUnitOfWork()
        developer = uow.developer_repository.get_by_id(1)
        processor = uow.processor_repository.get_by_id(1)
        graphics_card = uow.graphics_card_repository.get_by_id(1)
        os = uow.os_repository.get_by_id(1)

        game_id = create_game(uow, title, release_date, description, developer, processor, graphics_card, os)

        return redirect(f'/games/{game_id}', code=301, Response=None)
    else:
        return render_template('create_game.html')

@app.route('/create_developer', methods=['GET', 'POST'])
def cr_developer():
    if request.method == 'POST':
        name = request.form['name']

        uow = SqlAlchemyUnitOfWork()
        developer_id = create_developer(uow, name)

        return redirect('/create_game', code=301, Response=None)
    else:
        return render_template('create_developer.html')

@app.route('/create_graphics_card', methods=['GET', 'POST'])
def cr_graphics_card():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']

        uow = SqlAlchemyUnitOfWork()
        graphics_card_id = create_graphics_card(uow, name, rating)

        return redirect('/create_game', code=301, Response=None)
    else:
        return render_template('create_graphics_card.html')

@app.route('/create_os', methods=['GET', 'POST'])
def cr_os():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']

        uow = SqlAlchemyUnitOfWork()
        os_id = create_os(uow, name, rating)

        return redirect('/create_game', code=301, Response=None)
    else:
        return render_template('create_os.html')

@app.route('/create_processor', methods=['GET', 'POST'])
def cr_processor():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']

        uow = SqlAlchemyUnitOfWork()
        processor_id = create_processor(uow, name, rating)

        return redirect('/create_game', code=301, Response=None)
    else:
        return render_template('create_processor.html')

if __name__ == '__main__':
    app.run(debug=True)
