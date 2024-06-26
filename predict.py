import random

class Positive: 
    def __init__(self):
        self.predictions = [
            "Скоро звёзды укажут путь к неожиданному счастью",
            "Ветер перемен приносит благословение в скрытой форме",
            "Солнце восходит над горизонтом твоих надежд",
            "Ключ к успеху уже в твоих руках; ты просто еще не узнал его форму",
            "Твоё будущее сверкает ярче, чем самая светлая звезда",
            "Жди знака, который откроет двери к долгожданной радости",
            "Ты скоро обнаружишь сокровище, скрытое в твоём сердце",
            "Великое путешествие начинается с одного шага, который ты сделаешь сегодня",
            "Ты как феникс, восстанешь из пепла своих сомнений и полетишь к мечте",
            "Тайный союзник появится, чтобы помочь тебе на пути к успеху",
            "В свете веры узреешь свою дорогу, и благословение станет твоим спутником.",
            "Молитва - ключ к откровениям, и ты обретешь ответы на свои вопросы.",
            "Сердце, наполненное добротой, привлечет благословение, как магнит.",
            "Пусть мудрость ведет тебя, а милосердие освещает твой путь.",
            "Твоя преданность ведет к миру, а твои добрые дела будут вознаграждены.",
            "Как светило, ты можешь озарить тьму своими добрыми делами, раскрывая путь для других.",
            "Время подобно ткачу, а ты можешь быть нитью, вплетенной в прекрасный узор судьбы.",
            "Как драгоценный камень, ты можешь блеснуть в своей уникальности, привлекая восхищенные взгляды.",
            "Твоя жизнь - это песня, наполненная мелодией надежды, которая звучит в сердцах других.",
            "Каждый шаг, который ты делаешь вперед, может быть каплей дождя, которая наполняет бассейн твоего успеха."
        ]

    def get_prediction(self):
        return random.choice(self.predictions)

class N_Positive:
    def __init__(self):
        self.predictions = [
            "Маленький шаг в неизвестность может привести к большой радости",
            "Тени сомнений понемногу рассеиваются, открывая путь к свету",
            "Терпение будет вознаграждено, хотя и не так быстро, как ты надеешься",
            "Небольшие трудности уступят место внезапным радостям",
            "Возможно, ответ на твой вопрос уже ближе, чем ты думаешь",
            "Твои усилия скоро будут замечены теми, кто может их вознаградить",
            "Сердце подскажет правильный выбор в скором времени",
            "Под поверхностью обыденности скрывается нечто ценное",
            "Звезды медленно, но верно движутся в твою пользу",
            "Скрытые таланты обретут признание в неожиданной форме",
            "Время как течение реки несет с собой неожиданные сюрпризы, вдохновляющие к новым начинаниям.",
            "Тени сомнений медленно рассеиваются, оставляя место для вдохновения и творчества.",
            "Мир вокруг нас полон возможностей, и ты только начинаешь разгадывать их.",
            "Случайности сменяются моментами счастья, и ты можешь обнаружить его даже в самых обыденных моментах.",
            "Твоя уверенность в себе откроет двери к новым горизонтам, наполняя жизнь радостью и удовлетворением.",
            "Мгновения тишины могут быть зеркалом, отражающим внутреннюю гармонию, которая поднимает дух.",
            "Ветер перемен может развеять пыль прошлого, оставляя перед тобой свежие возможности.",
            "Твоя сила стойкости может быть тем светом, который освещает твой путь, когда темно вокруг.",
            "Каждый шепот тишины может содержать ответы на вопросы, которые ты даже не задавал.",
            "Корни древа твоей жизни проникают глубоко в землю реальности, даря тебе прочность в любую бурю."
        ]

    def get_prediction(self):
        return random.choice(self.predictions)


class Neutral:
    def __init__(self):
        self.predictions = [

            "Время идет своим чередом, несущее изменения и постоянство одновременно",
            "День за днем пишет книгу твоей судьбы, страница за страницей",
            "Как лист на ветру, так и ты подвластен переменам жизни",
            "Всё течёт, всё изменяется; ни один день не похож на другой",
            "Ты стоишь на перекрестке путей; каждый выбор ведёт к своей судьбе",
            "Времена года меняются, как и этапы твоей жизни",
            "Звёзды говорят многое, но не всё; твой путь – твой выбор",
            "Как река течёт к морю, так и время несёт тебя вперёд",
            "Жизнь – это путешествие с неизвестным назначением",
            "Твоё прошлое, настоящее и будущее переплетены в единый узор судьбы"
            "Как вода в реке, твоя судьба течет своими водами, иногда спокойно, иногда бурно, но всегда ведущая к своему устью.",
            "Словно старейшина леса, ты стоишь твердо в корнях своих убеждений, наблюдая за миром вокруг.",
            "Вокруг нас мир полон тайн, и лишь терпеливый путник может разгадать их все.",
            "Сквозь сон судьбы проблескивают образы, и только сердце способно их правильно толковать.",
            "Судьба подобна книге, каждая страница — новый поворот, новый сюжет, новая загадка.",
            "Подобно тени в полдень, тайны судьбы раскрывают свои образы лишь на мгновение, чтобы снова скрыться.",
            "Пусть свет звезд осветит твой путь, и ты сможешь открыть тайны, скрытые в глубинах времени.",
            "Как растущее дерево, ты стремишься к высотам, но не забывай о корнях, которые тебя кормят.",
            "Время — это лишь инструмент в руках судьбы, и твоя задача использовать его мудро.",
            "Судьба подобна звездному небу: полна блеска, но лишь самый искусный наблюдатель способен прочитать ее знаки."
        ]

    def get_prediction(self):
        return random.choice(self.predictions)


class N_Neutral:
    def __init__(self):
        self.predictions = [

            "Туман неопределенности ещё не рассеялся, но скоро прояснится.",
            "Маленькие заботы сегодняшнего дня не предвещают великих изменений.",
            "Твой путь может быть извилист, но он ведет тебя вперед.",
            "Сомнения и уверенность чередуются, как день и ночь.",
            "Твои поиски ответов могут занять больше времени, чем ожидалось.",
            "Ветер перемен касается тебя, но не приносит сразу заметных изменений.",
            "Пока ты стоишь на распутье, пути твоей судьбы остаются неопределенными.",
            "Маленькие волны жизни не всегда предвещают бурю.",
            "Твоя судьба таит в себе множество путей, но не все они ясны сейчас.",
            "Небольшие знаки судьбы окружают тебя, но их значение ещё не ясно.",
            "Твой путь расплетается, как клубок нитей, ожидая, когда же наконец-то образуется узор.",
            "Судьба таинственна, как лабиринт, в котором каждый поворот приносит новое открытие.",
            "Твои мысли, как облака на небе, иногда ясные, иногда покрытые пеленой таинственности.",
            "Время — это река, несущая нас по своему течению, иногда тихо и плавно, иногда быстро и неуклонно.",
            "Судьба подобна загадке, чье решение находится где-то между строчек жизни.",
            "Твой путь как картина, разворачивающаяся перед тобой, и лишь время скажет, какой образ она примет в итоге.",
            "Волшебство судьбы затаилось в каждом мгновении, подобно маленьким драгоценным камням, ожидающим своего обнаружения.",
            "Судьба подобна песке в руках, непостоянна и изменчива, но при этом полна возможностей.",
            "Твой путь подобен звездному небу, усыпанному тысячами звезд, каждая из которых приносит свою историю.",
            "Судьба — это загадка, которую нужно разгадать, смотря на мир через призму мудрости и опыта."
        ]

    def get_prediction(self):
        return random.choice(self.predictions)


class Negative:
    def __init__(self):
        self.predictions = [
            "Твоё терпение будет испытано, прежде чем придёт облегчение.",
            "Тучи на горизонте предвещают бурю, но после неё придет ясность.",
            "Скоро ты столкнешься с трудным выбором, который потребует мужества.",
            "Тёмные воды заблуждений могут затянуть тебя, будь осторожен.",
            "Будь начеку: не всё то золото, что блестит.",
            "Скрытые препятствия могут замедлить твой путь вперёд.",
            "Время раскрыть тайны, но не все из них принесут радость.",
            "Остерегайся ложных друзей, которые могут повести тебя по ложному пути.",
            "Тени прошлого могут настигнуть тебя, если не будешь осторожен.",
            "Будь готов к потерям, которые приведут к важным урокам.",
            "Твои надежды могут оказаться лишь иллюзией, и разочарование станет неизбежным.",
            "Темные облака над твоей судьбой готовы пролить дождь несчастий на твои плечи.",
            "Предательство может прийти в обличье лояльности, так что будь бдителен перед тем, кто протягивает руку помощи.",
            "Время от времени судьба испытывает нас чередой тяжких испытаний, чтобы мы смогли узнать силу нашего духа.",
            "Ты можешь ощутить потери, подобно листьям, упавшим с деревьев осенью, но помни, что зима всегда уступает весне.",
            "Судьба иногда подбрасывает нам горечь поражений, чтобы мы могли научиться ценить сладость победы.",
            "Темные дороги прошлого могут привести к болезненным воспоминаниям, которые не желают оставить свои следы.",
            "Остерегайся ловушек внутри себя, где даже самые глубокие желания могут привести к разочарованию.",
            "Твоя судьба подобна путанице в лабиринте, где каждый поворот может привести к тупику.",
            "Негативные мысли могут стать цепями, сковывающими твой дух и тянущими вниз."
        ]
        

    def get_prediction(self):
        return random.choice(self.predictions)


class N_Negative:
    def __init__(self):
        self.predictions = [
            "Маленькие трудности на пути могут заставить тебя остановиться и задуматься.",
            "Твоя уверенность может быть пошатнута, но это временно.",
            "Слабый ветер перемен может принести небольшие препятствия.",
            "Твой путь освещен неясно; будь внимателен к каждому шагу.",
            "Некоторые ответы могут оставить больше вопросов, чем разрешений.",
            "Мелкие недоразумения могут привести к кратковременному разочарованию.",
            "Твои намерения хороши, но результаты могут быть не такими, как ожидалось.",
            "Будь готов к неожиданным задержкам в достижении целей.",
            "Важное решение может оказаться сложнее, чем кажется на первый взгляд.",
            "Трещины в стене неопределенности могут сделать твой путь менее прочным, но именно они могут открыть новые горизонты.",
            "Тени неопределенности могут заставить тебя замедлить шаги, но именно в этом медленном танце может заключаться ответ.",
            "Каждый шаг на темном пути может вызвать волну сомнений, но именно эти волны могут развеять дым иллюзий.",
            "Неопределенность может быть путеводной звездой, которая ведет тебя через бурю, хотя и не всегда прямо к порту.",
            "Кажется, что ответы на вопросы могут ускользнуть, как вода сквозь пальцы, но это лишь временная природа знаний.",
            "Разочарование, как дождевые капли, может оставить следы на твоем сердце, но именно в этих следах может скрыться мудрость.",
            "Идеалы могут оказаться ветром перемен, который несет их вдали от твоих пальцев, но именно так можно обнаружить новые истины.",
            "Туманный ландшафт неопределенности может сделать твой путь менее ясным, но это может быть причудой судьбы, чтобы ты мог увидеть новые горизонты.",
            "Дорога к цели может быть длинной и извилистой, но в каждом повороте может крыться новая возможность.",
            "Тени прошлого могут стать тяжелым бременем на твоем пути, но в них также можно обнаружить следы уроков.",
            "Путеводная звезда твоей судьбы может мерцать слабее в ночном небе, но даже в темноте есть место для открытий."
        ]

    def get_prediction(self):
        return random.choice(self.predictions)
