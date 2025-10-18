# Структура данных об организациях.
from idlelib.debugger_r import restart_subprocess_debugger

organizations = {
    1: {
        'name': 'Организация',
        'reviews': []
    },
    2: {
        'name': 'Другая организация',
        'reviews': [
            {'12':'good dog'},
            {'671':'blast'}
        ]
    }
}


# Необходимо напиcать функцию, которая добавляет отзыв об организации в структуру данных (выше).
# Функция должна возвращать добавленный отзыв.
# У организации может быть только один отзыв от каждого пользователя.



def add_rev(rev:str, user_id:str, org_id:int) -> str:

    if org_id not in organizations:
        raise KeyError('organization not found')

    reviews = organizations[org_id]['reviews']

    for review_dict in reviews:
        if user_id in review_dict:
            review_dict[user_id] = rev
            return rev
    reviews.append({user_id:rev})
    return rev



def test_camel_maker():
    text = '4of Fo1r pe6ople g3ood th5e the2'
    data_arr = text.split()
    sorted_data = {}
    positions = [str(ind) for ind in range(1,10)]
    for el in data_arr:
        for symbol in el:
            if symbol in positions:
                sorted_data[symbol] = el
    result = ''
    for el in range(1,10):
        if str(el) in sorted_data:
            result += sorted_data[f'{el}']+' '
    print(result[:-1])


# КАК ТАК?!
# def order(sentence):
#   return " ".join(sorted(sentence.split(), key=min))