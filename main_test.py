import pytest

from main import MoviesLibrary


@pytest.fixture
def movies_library():
    return MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])


def test_add_movie_to_genre(movies_library):
    movies_library.add_movie('Комедия', 'Весёлый питонист')
    if movies_library.recommend('Комедия') == ["Весёлый питонист"]:
        pass
    else:
        pytest.fail("Неверные фильмы в библиотеке Комедия")
    if not movies_library.recommend('Ужасы'):
        pass
    else:
        pytest.fail("Возвращена не пустая библиотека")
    if not movies_library.recommend('Романтика'):
        pass
    else:
        pytest.fail("Возвращена не пустая библиотека")


def test_add_movie_to_multiple_genres(movies_library):
    movies_library.add_movie('Комедия', 'Весёлый питонист')
    movies_library.add_movie('Романтика', 'Три разраба и тестировщик')
    if movies_library.recommend('Комедия') == ["Весёлый питонист"]:
        pass
    else:
        pytest.fail("Неверные фильмы в библиотеке Комедия")
    if not movies_library.recommend('Ужасы'):
        pass
    else:
        pytest.fail("Возвращена не пустая библиотека")
    if movies_library.recommend('Романтика') == ['Три разраба и тестировщик']:
        pass
    else:
        pytest.fail("Неверные фильмы в библиотеке Романтика")


def test_recommended_library_empty(movies_library):
    assert movies_library.recommend('Комедия') == []
    assert movies_library.recommend('Романтика') == []
    assert movies_library.recommend('Ужасы') == []


def test_add_movies_to_genre(movies_library):
    movies_library.add_movie('Комедия', 'Весёлый питонист')
    movies_library.add_movie('Комедия', 'Три разраба и тестировщик')
    print(movies_library.recommend('Комедия'))
    if sorted(movies_library.recommend('Комедия')) == sorted(["Три разраба и тестировщик", 'Весёлый питонист']):
        pass
    else:
        pytest.fail("Неверные фильмы в библиотеке Комедия")