SIDE_BAR_ELEMENTS_TEXT = [
    'Налаштування застосунку',
    'Допомога',
    'Повідомити про проблему',
    'Відеоспостереження',
    'Додати хаб',
    'Умови використання',
]


def test_side_bar(main_fixture):
    main_page = main_fixture
    result = main_page.check_side_bar_elements()
    assert all([result['clickable'], result['show_img'], result['show_text'], result['text'] == SIDE_BAR_ELEMENTS_TEXT])
