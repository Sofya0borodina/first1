from pymorphy2 import MorphAnalyzer


def get_normal_form(word1):                          ### Определяем функцию, которая возвращает нормальную (нулевую) форму слова
        morph = MorphAnalyzer()
        return morph.parse(word1)[0].normal_form


def get_lines(file_name):                              ### Определяем функцию, которая собирает текст в один абзац, выводит его на экран и возвращает получившийся текст
        with open(file_name, encoding="utf-8") as f:
                lines = f.read().strip().split("\n")
                lines = " ".join(lines)
                print(lines)
        return lines


def clear_text(text):                                   ### Определяем функцию, которая возвращает очищенную версию текста
        text = text.lower()
        cleaned_text = ""
        for symbol in text:
                if symbol.isalpha() or symbol == " " or symbol == "\n":
                        cleaned_text += symbol
        tokens = cleaned_text.split()
        return tokens


def define_theme(text_):                        ### Определяем функцию, которая возвращает тематику (рубрику) статьи
        score = {"экономика": 0, "политика": 0, "наука": 0, "культура": 0, "спорт": 0}    ### Создаём словарь, который считает очки, набранные статьёй по каждой тематике 
        article = set(clear_text(text_))             ### Обращаемся к третьей функции и превращаем очищенный текст в множество (текст разбивается на слова)
        for word in article:
                for theme in dictionary:
                        word  = get_normal_form(word)          ### Обращаемся к первой функции
                        if word in dictionary[theme]:
                                score[theme] = score[theme] + 1   ### Прибавляем очки к тематике, к которой относится слово
        return max(score, key=score.get)       ### Ищем ключ (тематику) с наибольшим значением (количеством набранных очков)

                        

file_name = input("Введите название файла: ")
dictionary = {"экономика": ["экономика", "деньги", "средства", "бизнесмен", "банк"], "политика": ["политика", "государство", "президент", "страна"], "наука": ["наука", "открытие", "инновация", "технология"], "культура": ["культура", "театр", "кино"], "спорт": ["футбол", "баскетбол", "команда", "спорт", "мяч", "выиграть", "проиграть", "игра"]}
text2 = get_lines(file_name)
print(define_theme(text2))
