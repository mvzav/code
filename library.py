import pickle

class Book:
    book = {}
    def __init__(self, author, name, publ, rubric, avail, score):
        self.author = author
        self.name = name
        self.publ = publ
        self.rubtic = rubric
        self.avail = avail
        self.score = score

    def add():
        author = input('Ведите И.О.Фамилию автора')
        name = input('Введите название книги')
        publ = input('Введите название издательства')
        k_rubric = input('Введите цифру 1, если специальная литература, или цифру 2, если беллетристика')
        if k_rubric == '1':
            rubric = 'Специальная литература'
        if k_rubric == '2':
            rubric = 'Беллетристика'
        avail = True
        score = input('Введите оценку от 1 до 5')
        print('Книга добавлена')

    def delete():
        name = input('Введите название книги для удаления')
        del Book.book[name]

    def input_author():
        author_t = input('Введите И.О Фамилию автора')
        for b in Book.book.items():
            if b.author == author_t:
                print(b)

    def input_rubric():
        rubric_t = input('Введите рубрику')
        for b in Book.book.items():
            if b.rubric == rubric_t:
                print(b)

    def input_avail():
        for b in Book.book.items():
            if b.avail == True:
                print(b)

    def change():
        name = input('Введите название книги для изменения')
        book_t = Book.book[name]
        t = input('Введите 1, если изменить наличие. Введите 2, чтобы изменить оценку')
        if t == '1':
            if book_t.avail == True:
                book_t.avail = False
            else:
                book_t.avail = True
        if t == '2':
            book_t.score = int('Введите новую оценку')


    def save_books():
        file = 'library.txt'
        library = Book.book.items()
        f = open(file, 'wb')
        pickle.dump(library, f)
        f.close()
        del library
        return ('Библиотека сохранена в файл')


    def menu():
        x = 0
        while x != '6':
            print( '''1. Вывод по автору - 1\n2. Вывод по разделу - 2 \n3. Вывод по наличию - 3 \n4. Изменение - 4 \n5. Добавление- 5 \n6. Удаление - 6\n7. Загрузка в файл- 7 \n8. Выход - 8 ''')
            x = input('Введите значение : ')
            if x == '1':
               Book.input_author()
            elif x == '2':
                Book.input_avail()
            elif x == '3':
                Book.input_rubric()
            elif x == '4':
                Book.change()
            elif x == '5':
                Book.add()
            elif x == '6':
                Book.delete()
            elif x == '7':
                Book.save_books()
            elif x == '6':
                break

a = Book('А.С.Пушкин','Капитанская дочка', 'Лань', 'Беллетристика', True,'5')
Book.menu()