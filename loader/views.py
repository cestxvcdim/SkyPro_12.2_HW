from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import save_picture, add_post
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    logging.info('OK')
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')
    logging.info('Выполняется проверка...')
    if not picture or not content:
        logging.info('Нет картинки или текста')
        return 'Нет картинки или текста'
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Неверное расширение файла')
        return 'Неверное расширение файла'
    try:
        path = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        logging.error('Некорректный файл')
        return 'Некорректный файл'
    post = add_post({"pic": path, "content": content})
    logging.info('OK')
    return render_template('post_uploaded.html', post=post)
