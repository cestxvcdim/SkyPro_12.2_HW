from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import get_posts_by_word
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    logging.info('OK')
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    search_query = request.args.get('s')
    logging.info('Выполняется поиск...')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        logging.error('Некорректный файл')
        return 'Некорректный файл'
    logging.info('OK')
    return render_template('post_list.html', posts=posts, query=search_query)
