import json
#Здесь расположены клавиатуры Студенты и клавиатуры практики
# Кнопки клавиатуры для студента
student_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Практика"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Курсы и обучение"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Работа"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Стажировка"
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
student_keyboard = json.dumps(student_keyboard, ensure_ascii=False).encode('utf-8')
student_keyboard = str(student_keyboard.decode('utf-8'))

studentpractica_page_1_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "К кому обращаться по практике?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Где могу пройти практику?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Могу пройти практику по месту работы?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Когда практика?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Назад"
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"6\"}",
                    "label": "Далее"
                },
                "color": "default"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
studentpractica_page_1_keyboard = json.dumps(studentpractica_page_1_keyboard, ensure_ascii=False).encode('utf-8')
studentpractica_page_1_keyboard = str(studentpractica_page_1_keyboard.decode('utf-8'))

studentpractica_page_2_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Могу ли пройти практику раньше?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Какие документы необходимы до практики?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Кому сдавать отчет?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Можно ли пройти практику дистанционно?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Назад"
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"6\"}",
                    "label": "Далее"
                },
                "color": "default"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
studentpractica_page_2_keyboard = json.dumps(studentpractica_page_2_keyboard, ensure_ascii=False).encode('utf-8')
studentpractica_page_2_keyboard = str(studentpractica_page_2_keyboard.decode('utf-8'))

studentpractica_page_3_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Будут ли мне платить на практике?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Можно пройти практику вне Новосибирска?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Где взять направление на практику?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Когда будет собрание по практике?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Назад"
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Далее"
            },
            "color": "default"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
studentpractica_page_3_keyboard = json.dumps(studentpractica_page_3_keyboard, ensure_ascii=False).encode('utf-8')
studentpractica_page_3_keyboard = str(studentpractica_page_3_keyboard.decode('utf-8'))

studentpractica_page_4_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Где взять дневник и отчет?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Кто руководитель по практике?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Как узнать номер договора?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Как составить резюме чтобы пройти отбор?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Назад"
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"6\"}",
                    "label": "Далее"
                },
                "color": "default"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
studentpractica_page_4_keyboard = json.dumps(studentpractica_page_4_keyboard, ensure_ascii=False).encode('utf-8')
studentpractica_page_4_keyboard = str(studentpractica_page_4_keyboard.decode('utf-8'))