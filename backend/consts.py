class Constants:
    HELLO_MSG = """Hello!"""
    COMMAND_PROMPT_MSG = """-> """
    UNKNOWN_COMMAND_MSG = """Введена неизвестная команда"""
    SETTINGS_HELP_MSG = """
Отобразить настройки.
Использование:
    settings"""
    SET_HELP_MSG = """Изменить определенную настройку/опцию.
Использование:
    set [option] [value]
Пример:
    set Language en"""
    HELP_MSG = """Доступные команды:
%s
Использование:
    help [command]
Пример:
    help set"""
    QUIT_HELP_MSG = """Выход из программы.
Использование:
    q"""
    ADDRESS_SEARCH_HELP_MSG = """Предоставляет подсказки для введенного адреса"""
    CHOOSE_ADDRESS_HELP_MSG = """Позволяет выбрать подходящую подсказку для адреса"""
    FIND_ADDRESS_COORDINATES_HELP_MSG = """Получение точки геолокации для запрошенного адреса"""
    SEARCH_PICK_ADDRESS_COORDS_HELP_MSG = """Получение и выбор подходящей подсказки для адреса, а так же получение точки геолокации запрошенного адреса.
Использование:
    /s [address]
Пример:
    /s москва хабар"""
    SUGGESTED_ADDRESSES_MSG = """Предлагаемые адреса:"""
    ENTERING_INDEX_REQUIRED_ADDRESS_MSG = """Введите номер подходящего адреса -> """
    SELECTED_ADDRESS_MSG = """Выбранный адрес: %s"""
    ADDRESS_COORDINATES_MSG = """Широта: %s
Долгота: %s"""
    INPUT_ERROR_MSG = """Ошибка ввода. 
Используйте help"""
    HTTP_403_ERROR_MSG = """В запросе указан несуществующий API-ключ
Или не подтверждена почта
Или исчерпан дневной лимит по количеству запросов"""
    NOT_FOUND_ADDRESSES = """Для введенного адреса не нашлось подсказок. Попробуйте другой адрес."""
