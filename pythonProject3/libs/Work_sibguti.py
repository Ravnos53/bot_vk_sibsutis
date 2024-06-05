import json

# Кнопки клавиатуры для сотрудника СибГУТИ
sibguti_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Ищу сотрудника среди студентов СибГУТИ"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Приглашаю представителя компании на мероприятие"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Задача для практики студентам СибГУТИ"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Предлагаю компанию для практики студентам"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Мероприятия Центра карьеры"
            },
            "color": "primary"
        }],
        [{
            "action":{
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Я руководитель практики"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"back\"}",
                "label": "Назад"
            },
            "color": "default"
        }]
    ]
}

# Преобразование клавиатуры в JSON-формат
sibguti_keyboard = json.dumps(sibguti_keyboard, ensure_ascii=False).encode('utf-8')
sibguti_keyboard = str(sibguti_keyboard.decode('utf-8'))