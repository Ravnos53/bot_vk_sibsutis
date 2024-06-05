import json

courses_and_training_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Курсы на платформе Факультетус"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Где можно поискать курсы?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "дополнительное проф. образование СибГУТИ"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
courses_and_training_keyboard = json.dumps(courses_and_training_keyboard, ensure_ascii=False).encode('utf-8')
courses_and_training_keyboard = str(courses_and_training_keyboard.decode('utf-8'))