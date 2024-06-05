from libs import *
from imports import *

# Устанавливаем ключ доступа к API ВКонтакте
TOKEN = "vk1.a._BGV2UAGeKRwlIpbJmuDmG_RWBV8TZtBKDe3ZejDeGxBS-eL5q_p-Lrhkh3g8Y3-Ieiho36admLvH3OECldW25_f9veX_P8BcNfxRszHYOk0oZ2xtBOxYHXJzaBa2TaCtaGFRHzgC6PsdVsWXCA1tA0TEtrzVapgV848yaQHoQ5IDL6Yrh3jHsTs0E-fAKkLTlkzXFMGU0xN7jxA6xG6dw"

# Создаем объект сессии
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

user_states = {}

# Функция для отправки сообщения
def send_message(user_id, message):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=random.randint(1, 999999)
    )

# Функция для отправки сообщения с клавиатурой
def send_message_with_keyboard(user_id, message, keyboard):
    vk.messages.send(
        user_id=user_id,
        message=message,
        keyboard=keyboard,
        random_id=random.randint(1, 999999)
    )


# Основной цикл обработки сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id

        if message == "студент":
            send_message_with_keyboard(user_id, "Вы находитесь в Разделе для студентов. Выберите интересующий вас подраздел:", student_keyboard)



        elif message == "практика":
            user_states[user_id] = 1
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_1_keyboard)

        # studentpractica_page_1_keyboard
        elif message == "к кому обращаться по практике?":
            send_message(user_id, "С вопросами по организации практики обращайтесь в центр карьеры - к. 1-506, эл. почта praktika@sibguti.ru. Подробнее о праткике здесь https://sibsutis.ru/work-univer/talent-pool/practice.php")
        elif message == "где могу пройти практику?":
            send_message(user_id, "Практику можно пройти на предприятии, у индивидуальных предпринимателей (ИП) (при этом обязательно заключается договор между вузом и организацией) или в СибГУТИ (на кафедре или в профильном структурном подразделении университета).")
        elif message == "могу пройти практику по месту работы?":
            send_message(user_id, "Можете, если работаете по профилю получаемого образования. Обязательно заключается договор между вузом и организацией.")
        elif message == "когда практика?":
            send_message(user_id, "Смотрите свой календарный учебный график или спросите, написав письмо на praktika@sibguti.ru, указав свою группу.")

        #studentpractica_page_2_keyboard
        elif message == "могу ли пройти практику раньше?":
            send_message(user_id, "Нет.")
        elif message == "какие документы необходимы до практики?":
            send_message(user_id, "Договор между вузом и предприятием, письмо от предприятия о назначении руководителя, дневник практики.")
        elif message == "кому сдавать отчет?":
            send_message(user_id, "Руководителю по практике от СибГУТИ.")
        elif message == "можно ли пройти практику дистанционно?":
            send_message(user_id, "Можно, если это согласовано руководителем практики от СибГУТИ и указано в договоре между вузом и предприятием.")

        #studentpractica_page_3_keyboard
        elif message == "будут ли мне платить на практике?":
            send_message(user_id, "Обычно практика не оплачивается. Но при наличии в организации вакантной должности, работа на которой соответствует требованиям к практической подготовке, заключить с обучающимся СибГУТИ срочный трудовой договор о замещении такой должности.")
        elif message == "могу ли пройти практику вне Новосибирска?":
            send_message(user_id, "Можете по месту постоянного места жительства по согласованию с директором института/деканом факультета.")
        elif message == "где взять направление на практику?":
            send_message(user_id, "Направлением на практику является оформленный дневник практики и письмо от предприятия о назначении руководителя практики")
        elif message == "когда будет собрание по практике?":
            send_message(user_id, "Узнавайте в дирекции и центре карьеры (к. 1-506, эл. почта praktika@sibguti.ru).")

        #studentpractica_page_4_keyboard
        elif message == "где взять дневник и отчет?":
            send_message(user_id, "Ссылка, где можно скачать шаблоны отчётов и дневников доводится до студентов на собрании по практике")
        elif message == "кто руководитель по практике?":
            send_message(user_id, "Узнавайте в дирекции и центре карьеры -центр карьеры - к. 1-506, эл. почта praktika@sibguti.ru")
        elif message == "как узнать номер договора?":
            send_message(user_id, "Если номер не указан в таблице Распределение студентов на практику, напишите на адрес эл. почты praktika@sibguti.ru")
        elif message == "как составить резюме чтобы пройти отбор?":
            send_message(user_id, "В сообществе ВКонтакте https://vk.com/career_sibguti перейдите в раздел «Услуги» и выберите «Консультация» https://vk.com/career_sibguti?w=wall-213323941_896")

        #Переходы в студент-парктика
        elif message == "далее" and user_states.get(user_id) == 4:
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_1_keyboard)
            user_states[user_id] = 1
        elif message == "далее" and user_states.get(user_id) == 1:
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_2_keyboard)
            user_states[user_id] = 2
        elif message == "далее" and user_states.get(user_id) == 2:
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_3_keyboard)
            user_states[user_id] = 3
        elif message == "далее" and user_states.get(user_id) == 3:
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_4_keyboard)
            user_states[user_id] = 4
        elif message == "назад" and user_states.get(user_id) == 1:
            user_states[user_id] = 4
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_4_keyboard)
        elif message == "назад" and user_states.get(user_id) == 3:
            user_states[user_id] = 2
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_2_keyboard)
        elif message == "назад" and user_states.get(user_id) == 2:
            user_states[user_id] = 1
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_1_keyboard)
        elif message == "назад" and user_states.get(user_id) == 4:
            user_states[user_id] = 3
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", studentpractica_page_3_keyboard)

        #Курсы и образование
        elif message == "курсы и обучение":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", courses_and_training_keyboard)

        elif message == "курсы на платформе факультетус":
            send_message(user_id, "Перейдите по ссылке на главную страницу. Прокрутите вниз и выберите курс, который вам понравится.  https://facultetus.ru/university/487")
        elif message == "где можно поискать курсы?":
            send_message(user_id, "Образовательные курсы вы можете найти в свободном доступе в Интернете, на платформе Факультетус https://facultetus.ru или обратиться в Центр карьеры (каб. 1-506 или напишите в личные сообщения в сообщество ВКонтакте https://vk.com/career_sibguti")
        elif message == "дополнительное проф. образование сибгути":
            send_message(user_id, "В СибГУТИ реализуется более 100 программ дополнительного образования. Найти и выбрать подходящую можно на официальном сайте СибГУТИ https://sibsutis.ru/education/addo/")


        #Работа
        elif message == "работа":
            send_message_with_keyboard(user_id, "Определите интересующий вас вопрос для поиска работы:", student_or_graduate_keyboard)

        elif message == "я студент, который ищет работу":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", workstudent_keyboard)
        elif message == "я выпускник, который ищет работу":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", workgraduate_keyboard)

        elif message == "ресурсы для поиска работы":
            send_message(user_id, "Для поиска работы вы можете воспользоваться: Платформой «Факультетус» https://facultetus.ru Нашей группой Вконтакте https://vk.com/career_sibguti Телеграм-каналом https://t.me/career_sibguti")
        elif message == "центр карьеры помогает в поиске работы":
            send_message(user_id, "Мы предлагаем индивидуальную карьерную консультацию, помощь с резюме, встречу с работодателями и экскурсии в компании.Подай заявку на карьерную консультацию: группа Вконтакте https://vk.com/career_sibguti в разделе «Услуги» выбери «Консультация» https://vk.com/career_sibguti?w=wall-213323941_896")
        elif message == "вакансии":
            send_message(user_id, "Каждый четверг мы делаем подборку вакансий в нашей группе Вконтакте: https://vk.com/career_sibguti   Также все вакансии кадровых партнеров СибГУТИ нахдятся в цифровой карьерной среде на платформе Факультетус https://facultetus.ru")
        elif message == "мероприятия центра карьеры":
            send_message(user_id, "Мы весь год проводим карьерные мероприятия, мастер-классы, встречи с работодателями и многое другое! Следи за анонсами в нашей группе ВКонтакте: https://vk.com/career_sibguti и телеграм-канале https://t.me/career_sibguti")

        elif message == "работодатели для выпускников сибгути":
            send_message(user_id, "У нас достаточно много кадровых партнёров, информацию о которых вы можете найти на Факультетусе в разделе «Организации» https://facultetus.ru/unimanager/487?openup=main")
        elif message == "что говорить на собеседовании?":
            send_message(user_id, "Получи профессиональную помощь и рекомендации на индивидуальной карьерной консультации https://vk.com/career_sibguti?w=wall-213323941_896. Мы ответим на все интересующие тебя вопросы, запись идёт в разделе «Услуги» в группе ВКонтакте Центра карьеры https://vk.com/career_sibguti")
        elif message == "предлагаю проект с центром карьеры":
            send_message(user_id, "Мы всегда открыты к новым предложениям и идеям для создания проекта! Ценим креативность, инновации и стремление к развитию. Поэтому мы готовы рассмотреть любые интересные идеи, которые могут принести пользу и улучшить нашу работу. Смело пишите нам в ВКонтакте https://vk.com/career_sibguti")



        #Стажировка
        elif message == "стажировка":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", internship_keyboard)

        elif message == "где можно поискать стажировку?":
            send_message(user_id, "Мы публикуем и делаем подборки стажировок в нашей группе ВКонтакте https://vk.com/career_sibguti  и телеграм-канале https://t.me/career_sibguti")
        elif message == "что такое стажировка?":
            send_message(user_id, "Стажировка - это временная работа, которая предлагает практическое обучение и получение опыта работы в выбранной области.")
        elif message == "работа гарантирована после стажировки?":
            send_message(user_id, "Всё зависит от результата вашей работы, старайтесь успешно завершить стажировку чтобы получить оффер для дальнейшего трудоустройства.")



        elif message == "выпускник":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", graduate_keyboard)

        elif message == "когда встреча выпускников?":
            send_message(user_id, "Традиционная встреча выпускников проходит ежегодно в апреле, объявление о встрече размещается на официальном сайте СибГУТИ, пишите на адрес эл. почты rabota@sibguti.ru")
        elif message == "готов поделиться своей карьерной историе":
            send_message(user_id, "Пишите на адрес эл. почты rabota@sibguti.ru")
        elif message == "опрос выпускников":
            send_message(user_id, "Заполните анкету по ссылке: https://facultetus.ru/poll/3774/AIpl9cC4")
        elif message == "есть предложение для сотрудниче с вузом":
            send_message(user_id, "Пишите на адрес эл. почты rabota@sibguti.ru")



        elif message == "назад":
            send_message_with_keyboard(user_id, "Выберите вашу роль:", role_keyboard)



        elif message == "сотрудник сибгути":
            send_message_with_keyboard(user_id, "Выберите интересующий вас вопрос:", sibguti_keyboard)

        elif message == "ищу сотрудника среди студентов сибгути":
            send_message(user_id, "Станьте кадровым партнером СибГУТИ на платформе Факультетус. Направьте нам ссылку на вакансию, которая размещена в нашей цифровой карьерной среде на Факультетусе. Мы каждый четверг публикуем подборки вакансий в карьерных социальных сетях вуза. Если не удается самостятельно стать кадровым партнером, напишите на rabota@sibguti.ru.")
        elif message == "приглашаю представителя компании на мероприятие":
            send_message(user_id, "Здорово! Это действительно может повысить интерес студентов к дисциплине и улучшить качество образования СибГУТИ. Напишите на rabota@sibguti.ru желаемые даты, время, варианты компаний (сфера деятельности) и тему для выступления. Мы найдем спикеров.")
        elif message == "задача для практики студентам сибгути":
            send_message(user_id, "Напишите об этом на praktika@sibguti.ru. Подробно опишите задачу и требования к практикантам. В случае, если эта задача соответсвует компетенциям РПД, мы передадим ее руководителю по практике и студентам. В случае заинтересованности с их стороны, мы с Вами свяжемся. ")
        elif message == "предлагаю компанию для практики студентам":
            send_message(user_id, "Если Вы предлагаете компанию, предварительно обсудив этот вопрос с их представителями, то сообщите нам контакты и на кого можно сослаться при диалоге с ними. Если нет, то укажите наименование и ссылку на их сайт. Кроме того, укажите для каких направлений подготовки, на Ваш взгляд, она могла бы быть профильной.")
        elif message == "мероприятия центра карьеры":
            send_message(user_id, "Мы приглашаем Вас принять участие в наших карьерных событиях. Вы сможете быть ближе к рынку труда и понимать актуальные требования. Все события мы публикуем в ЦКС на Платформе Факультетус https://facultetus.ruв разделе События https://facultetus.ru, а также дублируем в карьерных каналах в телеграмм https://t.me/career_sibguti и ВКонтакте https://vk.com/career_sibguti")
        elif message == "Я руководитель практики":
            send_message(user_id, "Руководитель по практике должен ознакомиться с Положением о практической подготовке, получить консультацию от Центра карьеры по организационным вопросам (собрание/посетить лично центр карьеры/написать на praktika@sibguti.ru). Важно донести до студента сроки практики и место практики (кафедра или предприятие). ")

        else:
            send_message_with_keyboard(user_id, "Выберите вашу роль:", role_keyboard)
