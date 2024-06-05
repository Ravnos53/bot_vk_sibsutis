import json

# Кнопки клавиатуры для выбора роли
role_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Студент"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Сотрудник СибГУТИ"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Работодатель"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Выпускник"
            },
            "color": "primary"
        }]
    ]
}

role_keyboard = json.dumps(role_keyboard, ensure_ascii=False).encode('utf-8')
role_keyboard = str(role_keyboard.decode('utf-8'))