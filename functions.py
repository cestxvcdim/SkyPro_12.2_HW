import json


def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict[str, str]]:
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def add_post(post: dict[str, str]) -> dict[str, str]:
    posts: list[dict[str, str]] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
