# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('Алексей', color="#c8ffc8")
define M = Character('', what_italic=True)
define b = Character('Белка', color="#ffbf00")
define s = Character('Санёк', color="#8DB600")
define n = Character('Настя', color="#f66508")
define m = Character('Миша', color="#4a76a8")
define c = Character('Семён', color="#61af34")
define er = Character('L*p#|rx', color="#ffffff")
define g = Character('Голос', color="#5084c5")

# Вместо использования оператора image, можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
    
image movie = Movie(size=(1920, 1080),  xpos=0, ypos=0, xanchor=0, yanchor=100)
 
label start:
    scene bg black
    python:
        name = renpy.input(_("Как тебя зовут?"))

        name = name.strip()              
    play music "Memories.mp3"
    M "И снится мне сон..."
    
    M "Чудесные воспоминания, которые заставляют пустить скупую слезу."
    
    M "Кажется, что я вот-вот вернусь в те прекрасные дни."
    stop music fadeout 1
    play sound "vibro_tlf.mp3"
    
    a "Ну хорош, зачем меня будить?"
    
    M "На экране мобильного высветилось знакомое имя \"Белка\""
    
    stop sound fadeout 1
    
    b "Люсиль вставай! Нам через 20 минут надо быть возле Санька!"
    
    a "Ладно, скоро буду. До встречи."
    
    b "Пока."
    
    M "Люся - это Люцифер..."
    
    M "Сначала Настя начала так называть, теперь Белка..."
    
    M "Ладно, надо собираться."
    
    scene bg1 snow
    with Dissolve(.5)
    pause .5
    scene bg1 snow
    play music "snow.mp3" fadeout 1
    M "На часах 21:53. Я немного опаздываю."
    
    M "Но как тут не опоздать, когда вокруг такая красота?"
    M "Всегда любил ночь."
    play sound "xpystsnow.mp3"
    M "Снег крупными хлопьями ложится прямо мне под ноги."
    
    M "В этот холодный декабрьский день было как-то особенно грустно..."
    
    M "Сегодня последний день уходящего года..."
    stop sound fadeout 1
    scene bg2 snowlight
    with Dissolve(.5)
    pause .5
    scene bg2 snowlight
        
    M "Незаметно для себя я оказался возле дома Санька."
    
    M "Я остановился возле одинокого фонаря, который освещал лавочку и решил ждать Белку именно здесь."
    
    M "Свет фонаря завораживал. Снег продолжал сыпать крупными хлопьями..."
    
    M "Тут так спокойно. Лишь шум машин тревожил это тихое местечко."
    
    a "Эх. Как же тут красиво. Остался бы здесь..."
    
    b "И что тогда?"
    
    M "Не успел я воспроизвести свои мысли вслух, как вмешалась Белка."
    
    M "Видимо я просто её не заметил."
    
    b "Так ты мне ответишь?"
    menu:

        "{b}Ответить.{/b}":
            jump choice1_yes

        "{b}Не отвечать.{/b}":
            jump choice1_no

    label choice1_yes:

        $ menu_flag1 = True

        a "Я хотел сказать, что было бы прекрасно остаться здесь еще."
        
        b "Возможно..."
        
        b "Нам пора..."
        
        M "Странно, никогда не видел Белку такой \"Ушедшей в себя\""

        jump choice1_done

    label choice1_no:

        $ menu_flag1 = False

        a "Это секрет, который умрет вместе со мной!"
        b "Шутник, блин. Пошли."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
    scene bg1 snow
    with Dissolve(.5)
    pause .5
    scene bg1 snow
    
M "Мы стали подходить к подъезду Санька."
    
if menu_flag1:
    b "Подожди..."
    a "Что-то не так?"
    b "Нет. Просто..."
    b "Давай побудем тут еще немного."
    a "Хорошо."
    M "Мы стояли возле подъезда около 10 минут..."
    M "Неожиданно для нас дверь открылась, и оттуда выбежал Санёк..."
    stop music fadeout 1
    play sound "SanyaRun.mp3"
    M "О нет..."
    b "Лёха беги!!!"
    M "У Санька есть очень  плохая привычка, которая меня немного раздражает"
    M "Он начинает обниматься... Сильно обниматься."
    M "Очень сильно!"
    s "Привет Лёха!"
    M "Он всё же смог догнать меня и повалить."
    a "Привет... Саня... Слезь... С... Меня... ПОЖАЛУЙСТА!!!"
    stop sound fadeout 1
    s "Прости..."
    play music "snow.mp3" fadeout 1
    b "Успокоились?"
    s "Я да, он не знаю."
else:
    b "Ого! Мы почти не опоздали!"
    a "Значит пора подниматься. Звони в домофон."
    s "Да?"
    b "Открывай давай. Свои."
stop music fadeout 1     
        
 
    
M "Вскоре мы всё-таки попали в квартиру Санька."
scene bg3 windowsanya
with Dissolve(.5)
pause .5
scene bg3 windowsanya
play sound "window.mp3"
M "Я встал возле окна и начал осматривать окрестности Саниного дома."
M "Одинокая тишина присоединилась к моим раздумьям..."
if menu_flag1:
    M "Через какое-то время ко мне подошла Белка."
    scene bg4 belka #под вопросом
    with Dissolve(.5)
    pause .5
    scene bg4 belka
    M "В её руках был чай..."
    a "Довольно необычно для тебя, Катюх."
    M "Сказал я ей, указывая на кружку."
    b "Что?"
    M "Она сказала это так испуганно..."
    M "Будто не видела что я здесь нахожусь."
    a "О чем ты думаешь?"
    b "Ни о чем. Просто интересно..."
    a "Что интересно?"
    b "..."
    M "Эта тишина меня начинала угнетать..."
    b "Что бы было, останься мы здесь навсегда?"
    a "Ты о чём?"
    b "Ты представь, весь мир существует только для тебя."
    a "Это как-то эгоистично."
    b "Эх..."
    b "Ладно, я пошла накладывать на стол. Скоро же Новый Год."
    M "Еле заметная улыбка промелькнула на её лице."
    scene bg6 homes
    with Dissolve(.5)
    pause .5
    scene bg6 homes
    stop sound fadeout 1
    M "Пока Саша и Катя были заняты своими делами, я решил немного вздремнуть."
    M "Я надел наушники и включил музыку."
    play music "dream.mp3"
    M "Лучшее лекарство - Это расслабляющая музыка."
    M "Глаза начали закрываться..."
    scene bg black
    with Dissolve(.5)
    pause .5
    scene bg black
    
    a "..."
    a "..."
    a "..."
    stop music fadeout 1
    
else:
    M "Вокруг лишь тишина."
    
    scene bg black
    with Dissolve(.5)
    pause .5
    scene bg black
    M "Закрыв глаза я начинаю вспоминать..."
    M "Я полностью погрузился в тишину."
    stop sound fadeout 1
    M "Кто-то приоткрыл окно. Ветер подул в комнату."
    play sound "Wind.mp3"
    M "Это помогло уйти мне ещё глубже в воспоминания."
    M "Ничего лишнего, только я и музыка в моей голове..."
    M "Неужели опять предпраздничная депрессия?"
    a "Как всегда."
    M "Сказал я вполголоса, чтобы меня никто не услышал."
    M "Ко мне незаметно подошел Санёк."
    s "Ну что Лёх, пошли помогать Кате."
    M "На часах 22:32."
    menu:
        "{b}Пошли.{/b}":
            jump choice2_yes

        "{b}Скоро приду.{/b}":
            jump choice2_no

    label choice2_yes:

        $ menu_flag2 = True
        
        M "Пора идти помогать."
        jump choice2_done

    label choice2_no:

        $ menu_flag2 = False
        a "Я скоро подойду, помоги пока один."
        s "Как скажешь."
        M "Я остался ещё на несколько минут в полном одиночестве."
        M "Вскоре я все-таки решил покинуть этот уютный уголок тишины."
        
        jump choice2_done

    label choice2_done:
        if menu_flag2:
            scene bg6 homes
            with Dissolve(.5)
            pause .5
            scene bg6 homes
            play sound "podgotovka.mp3" 
            M "Мы с Саньком пошли на кухню."
            M "Из этого места, где царствовала еда, доносился приятный запах."
            a "А вот и мы!"
            b "Наконец-то! Иди салат делай."
            a "Хорошо."
            M "Я лениво подошел к столу и начал резать..."
            M "Еду на салат, к сожалению."
            M "Закончив подготовку я вновь посмотрел на часы."
            M "23:03."
            M "Пока Саша и Катя были заняты своими делами, я решил немного вздремнуть."
            M "Я надел наушники и включил музыку."
            M "Лучшее лекарство - Это расслабляющая музыка."
            M "Глаза начали закрываться..."
            stop sound fadeout 1
            play music "dream.mp3"
            scene bg black
            with Dissolve(.5)
            pause .5
            scene bg black
            a "..."
            a "..."
            stop music fadeout 1
    
        else:
            scene bg6 homes
            with Dissolve(.5)
            pause .5
            scene bg6 homes
            play sound "podgotovka.mp3" 
            M "Прямо передо мной стояла большая ёлка. Её мягкие иголки  слегка осыпались."
            M "Запах ели такой приятный..."
            a "Маленькой ёлочке холодно зимой..."
            b "...Из лесу ёлочку взяли мы домой."
            a "Ой."
            b "Пошли уже. Певец недоделанный."
            a "Ещё как доделанный."
            M "Пробухтел я себе под нос."
            b "Ну что Соловей, иди салат готовь."
            a "Хорошо, а Саня что будет делать?"
            a "Я что, должен один отдуваться?"
            b "Ну ты и бестолочь. Сань готовь тогда второй салат."
            s "А может я лучше мандарины почищу?"
            b "Ты дурачок? Они уже на столе."
            M "И правда, стол был уже почти полностью готов."
            M "Еда так и манила."
            M "Закончив подготовку я вновь посмотрел на часы."
            M "23:20."
            M "Пока Саша и Катя были заняты своими делами, я решил сесть возле ёлки."
            M "Я надел наушники и включил музыку."
            M "Мягкое кресло будто поглощало меня."
            M "Глаза сами начали закрываться..."
            stop sound fadeout 1
            scene bg black
            with Dissolve(.5)
            pause .5
            scene bg black
            play music "dream.mp3"
            a "..."
            a "..."
            a "..."
            stop music fadeout 1

play sound "zvonok.mp3"
M "Мой короткий сон потревожил звонок в дверь.."
M "Я снял наушники. Кресло не хотело меня отпускать..."
b "Кого там принесло?"
s "Сейчас узнаем."
stop sound fadeout 1
M "В прихожую вошла Настя, Миша и Семён."
M "Забавно... Семён... Почему я вспомнил БЛ?"
M "Распознал я их по голосам."
play music "podgotovka.mp3"
scene bg6 homes
with Dissolve(.5)
pause .5
scene bg6 homes
s "Привет ребят. Какими судьбами?"
n "Привет, да вот решили с вами отпраздновать."
m "Ага, уже совсем скоро не сможем так встречаться..."
c "Поэтому и решили отметить этот \"{i}Последний Новый Год{i}\" вместе с вами."
M "\"{i}Последний Новый Год{i}\", звучит не очень..."
M "Я встал с кресла, и направился встречать гостей."
M "Миша отдал мне большой пакет."
M "Внутри что-то звенело."
M "Кажется я знаю что они принесли."
a "Как я понимаю это на кухню?"
m "Ну да."
M "Настя пошла помогать Белке."
M "Саня начал разговаривать с Мишей и Семёном."
M "Все нашли себе какое-то дело.."
M "Кроме меня."
M "Я вновь подошёл к окну."
scene bg3 windowsanya
with Dissolve(.5)
pause .5
scene bg3 windowsanya
M "На часах 23:49."
a "Вот и осталось 10 минут до Нового Года."
n "Люсьен, иди за стол! Тебя только ждём."
M "Опа! Уже Люсьен..."
M "Кем я ещё буду?"
scene bg6 homes
with Dissolve(.5)
pause .5
scene bg6 homes
M "Я сел за стол вместе со всеми."
M "И вот 23:59."
M "Отсчет пошёл."
play sound "clock.mp3"
s "Пять!"
n "Четыре!"
c "Три!"
m "Два!"
a "Один..."
play sound "salyt.mp3"
M "..."
M "А вот и послышался салют."
s "Ура!"
n "С Новым Годом!"
c "С новым счастьем."
m "С праздником ребят."
stop sound fadeout 1
if menu_flag1:
    M "Я посмотрел на Белку."
    M "Что-то с ней не то..."
    M "Она закрыла глаза и выпила своё шампанское."
    M "Странно..."
    M "Всё странно..."
    M "Может подойти?"
    M "Поговорить с ней?"
    M "Но что я ей скажу?"
    M "~Эй Белка! Что с тобой творится? Ты какая-то не такая?~"
    M "Тупо."
    M "Все веселились, пили, ели."
    M "Все... Кроме Белки."
    M "К сожалению это заметил только я."
    
else:
    M "Неужели этот Новый Год будет счастливым?"
    M "Будет ли он таким, Как говорят нам с телеэкранов?"
    M "Сможем ли мы изменить свою жизнь?"
    



b "Сань, а тут крыша открыта?"
M "Неожиданно сказала Белка спустя тридцать минут молчания."
s "Да, а тебе зачем?"
b "Хочу посмотреть на салют."
s "И всё?"
b "Ну и покурить."#под вопросом
s "Иди, но давай не долго."
b "Хорошо."
a "Я пойду с тобой."
b "Хах. Почему я не удивлена."
a "Как всегда."
scene bg8 krisha
with Dissolve(.5)
pause .5
scene bg8 krisha
M "Вскоре мы очутились на крыше."
b "Прекрасный пейзаж."
a "Да, тут очень красиво."
if menu_flag1:

    b "Помнишь наш небольшой разговор по поводу этого Нового Года?"
    stop music fadeout 1
    play sound "zlo.mp3"
    a "Про то, что как было бы хорошо, останься мы здесь?"
    b "Да."
    b "Мне порой кажется, что я - это не я."
    a "В каком смысле?"
    M "Она переменилась в лице."
    M "Ехидная улыбка, неожиданно появившаяся на её лице, меня немного напугала."
    b "Ни в каком, я что-то бред начала говорить."
    M "Мы подошли к краю крыши."
    scene bg9 vid
    with Dissolve(.5)
    pause .5
    scene bg9 vid
    b "Вся наша жизнь идёт наперекосяк."
    M "Как-то странно сказала Белка."
    a "Ты о чём?"
    b "О том, что вся наша жизнь - лишь глупая игра."
    b "Я могу всё изменить, но не знаю хочу ли."
    a "Это ты должна решить сама."
    a "Есть такое забавное выражение:"
    a "{i}~Если судьба подкинула тебе кислый лимон - подумай, где достать текилу и офигенно повеселиться.~{i}"
    b "Да, пожалуй ты прав."
    b "Сегодня изменится всё..."
    a "И что ты сделаешь в первую очередь?"
    b "Вот сейчас и узнаем..."
    stop sound fadeout 1
    play sound "knife.mp3"
    scene bg14 blood1
    with Dissolve(.5)
    pause .5
    scene bg14 blood1
    play sound "num.mp3"
    a "Ка.. тя.."
    M "Сильный удар ножом в живот..."
    b "Скоро увидимся..."
    b "[name]..."
    M "Не понимаю, за что?"
    scene bg black
    with Dissolve(.5)
    pause .5
    scene bg black
    M "Вот и всё?"
    M "Всё закончилось?"
    M "Вот он?"
    M "..."
    M "\"{i}Последний Новый Год?{i}\""
    M "..."
    stop sound
    play sound "glitch.mp3"
    scene bg black
    with pixellate
    pause .5
    M "..."
    stop sound
    play music "Memories.mp3"
    M "И снится мне сон..."
    
    M "Чудесные воспоминания, которые заставляют пустить скупую слезу."
    
    M "Кажется, что я вот-вот вернусь в те прекрасные дни."
    stop music fadeout 1
    play sound "vibro_tlf.mp3"
    
    a "Ну хорош, зачем меня будить?"
    
    M "На экране мобильного высветилось знакомое имя \"SWudgfdrwlvhfb\""
    
    stop sound fadeout 1
    
    er "Л_си_ь в_т_в_й! Н_м ч_ре_ 20 м_н_т н_до б_ть в_з_е С_н_к_!"
    
    a "Алло? Тебя плохо слышно."
    
    er "П_ка."
    
    M "Странно..."
    
    M "Это же была Она?"
    
    M "Эх, ладно. Надо дойти до Санька."
    
    scene bg1 snow
    with Dissolve(.5)
    pause .5
    scene bg1 snow
    scene bg1 snow1 with Dissolve(.05)
    #scene bg13 helpme with Dissolve Для Android!!!!!!!!!
    python in mystore:

        def pro():
            import webbrowser
            webbrowser.open('https://pp.userapi.com/c840026/v840026594/5116b/ve3AecQJTMA.jpg')
            
        pro()
    play music "snow.mp3" fadeout 1
    M "На часах 21:53. Я немного опаздываю."
    
    M "Но как тут не опоздать, когда вокруг такая красота?"
    M "Всегда любил ночь."
    play sound "xpystsnow.mp3"
    M "Снег крупными хлопьями ложится прямо мне под ноги."
    
    M "В этот холодный декабрьский день было как-то особенно грустно..."
    
    M "Сегодня последний день уходящего года..."
    scene bg1 snow1 with Dissolve(.05)
    stop sound fadeout 1
    scene bg2 snowlight
    with Dissolve(.5)
    pause .5
    scene bg2 snowlight
        
    M "Незаметно для себя я оказался возле дома Санька."
    
    M "Я остановился возле одинокого фонаря, который освещал лавочку."
    
    M "Свет фонаря завораживал. Снег продолжал сыпать крупными хлопьями..."
    
    M "Тут так спокойно. Лишь шум машин тревожил это тихое местечко."
    
    a "Эх. Как же тут красиво. Остался бы здесь..."
    stop music fadeout 1
    g "Ты глуп."
    
    show er
    
    a "Ты... Кто..."
    play sound "gli.mp3"
    play movie "glitch.webm"
    show movie
    g "\rx#zhuh#qrw#eurxjkw#khuh#e|#fkdqfh, [name]"
    hide movie with fade
    stop movie
    play sound "gli.mp3"
    show er2 with pixellate
    
    g "Pl_y w_th m_"
    
    M "Странно, страха нет, но всё тело будто скованно."
    
    M "Я ничего не могу."
    
    M "Как-всегда беспомощен."
    
    g "Давай сыграем? Это простой пин-понг."
    
    
    stop music fadeout 1
    
    
    
    scene bg2 snowlight
    
else:
    M "Так странно..."
    M "Кажется, что всё и должно быть именно так."
    M "Но меня не покидает мысль о том, что нашу жизнь можно изменить к лучшему."
    b "Лёш..."
    a "Что?"
    stop music fadeout 1
    play sound "zlo.mp3"
    b "Как думаешь, можно ли вернуться назад?"
    a "Куда?"
    b "Да брось [name]. Хватит претворяться!"
    a "Почему она назвала меня '[name]'?"
    b "Знаешь, иногда нужно просто освободиться."
    b "Я помогу тебе."
    M "Она взяла камень и направилась на меня."
    a "Что ты..."
    play sound "pad.mp3"
    scene bg14 blood1
    with Dissolve(.5)
    pause .5
    play sound "num.mp3"
    M "Удар по голове..."
    b "Скоро увидимся..."
    b "[name]..."
    M "Не понимаю, за что?"
    scene bg black
    with Dissolve(.5)
    pause .5
    scene bg black
    M "Вот и всё?"
    M "Всё закончилось?"
    M "Вот он?"
    M "..."
    M "\"{i}Последний Новый Год?{i}\""
    
    stop sound
    play sound "glitch.mp3"
    scene bg black
    with pixellate
    pause .5
    M "..."
    stop sound
    play music "Memories.mp3"
    M "И снится мне сон..."
    
    M "Чудесные воспоминания, которые заставляют пустить скупую слезу."
    
    M "Кажется, что я вот-вот вернусь в те прекрасные дни."
    stop music fadeout 1
    play sound "vibro_tlf.mp3"
    
    a "Ну хорош, зачем меня будить?"
    
    M "На экране мобильного высветилось знакомое имя \"SWudgfdrwlvhfb\""
    
    stop sound fadeout 1
    
    er "Л_си_ь в_т_в_й! Н_м ч_ре_ 20 м_н_т н_до б_ть в_з_е С_н_к_!"
    
    a "Алло? Тебя плохо слышно."
    
    er "П_ка."
    
    M "Странно..."
    
    M "Это же была Она?"
    
    M "Эх, ладно. Надо дойти до Санька."
    
    
    scene bg1 snow
    with Dissolve(.5)
    pause .5
    scene bg1 snow
    scene bg1 snow1 with Dissolve(.02)
    scene bg1 snow
    play music "snow.mp3" fadeout 1
    M "На часах 21:53. Я немного опаздываю."
    
    M "Но как тут не опоздать, когда вокруг такая красота?"
    M "Всегда любил ночь."
    play sound "xpystsnow.mp3"
    M "Снег крупными хлопьями ложится прямо мне под ноги."
    
    M "В этот холодный декабрьский день было как-то особенно грустно..."
    
    M "Сегодня последний день уходящего года..."
    stop sound fadeout 1
    scene bg2 snowlight
    with Dissolve(.5)
    pause .5
    scene bg2 snowlight
        
    M "Незаметно для себя я оказался возле дома Санька."
    
    M "Я остановился возле одинокого фонаря, который освещал лавочку."
    
    M "Свет фонаря завораживал. Снег продолжал сыпать крупными хлопьями..."
    
    M "Тут так спокойно. Лишь шум машин тревожил это тихое местечко."
    stop music fadeout 1
    a "Эх. Как же тут красиво. Остался бы здесь..."
    
    
    
    g "\rx#zhuh#qrw#eurxjkw#khuh#e|#fkdqfh, [name]"
    
    
    
    g "Может Она была права?"
    
    a "Ты... Кто..."
    play movie "glitch.webm"
    show movie
    g "Давай сыграем в игру. Обычный пин-понг."# Под вопросом
    hide movie with fade
    stop movie
    play sound "gli.mp3"
    show er2 with pixellate
    
    
    
    stop music fadeout 1
init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, dental-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "Голос"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "[name]"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "bg pong field"

    add pong

    text _("[name]"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text _("Голос"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text _("Нажми, чтобы начать"):
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

if _return == "Голос":
    show er2
    g "Ты такой жалкий, [name]!"
    scene bg1 black1 with Dissolve(.5)
    play music "krik.mp3"
    g "Ты скоро проснёшься..."
    stop music
    jump start2

else:
      
    livE "Ты победил! Мои поздравлния... Но мы не закончили... Ты скоро вернёшся"
    
label start2:
    play music "lobot.mp3"
    scene bg15 lobot with Dissolve(.5)
    M "Что...Где... Где я?"
    M "Что произошло?"
    g "Я написала для тебя стихотворение."
    g "Оно на полу. Прочти его."
    M "Действительно, на полу оказался листок бумаги."
    scene bg17 lobotpap with Dissolve(.5)
    M "Что это значит?"
    
    python in mystore:

        def serial():
            import sys
            import os
            filename = 'QQQQQQQQQQQQQQQ.txt'
            filename = os.path.join(sys.path[0], filename)
            text_file = open(filename, "w")
            text_file.write("""Ой.
Привет.
А ты зачем сюда зашёл?
А, наверное стало интересно что это за файл.
Знаешь, а ведь тут нет ничего особенного.
Ну ладно, для тебя всё-таки будет подарок.
Держи кораблик.
_______ |\__ _. |\ 
_______ |)\__ _|)\ 
_______ |)_\_.. |)_\ 
_______ |)__\.. |)__\ 
___ (\’/ )_|)___\|)___\ 
__(№(/o\)№)|)____\____\ 
__(№)(№)_|)_____\____\_____, 
\____________________ _/ 
_\____________________/ """)
            text_file.close()
        serial()
           
    scene bg15 lobot with Dissolve(.5)
    g "Знаешь, мне было так скучно одной."
    g "Наконец-то она тебя убила. Теперь ты со мной."
    g "Тебе нечего бояться, я просто хочу помочь."
    M "Я... Умер..?"
    a "ЧТО???"
    M "Закричал я во всю силу."
    a "Кто ты?"
    a "Где ты?"
    a "Что ты такое?"
    g "Не волнуйся, все хорошо."
    M "Всё хорошо - самая лживая фраза."
    g "Пока ты лежал в снегу произошло ещё кое-что."
    a "В снегу?"
    g "Ой, а ты не помнишь?"
    stop music fadeout 1
    g "Сейчас покажу..."
    g "Да где же этот файл.."
    g "Нашла."
    $  renpy . movie_cutscene ( "memories.webm" )
    
    g "Вспомнил?"
    play music "slowdie.mp3"
    M "Что за? Я действительно умер?"
    g "Не бойся со мной ты в безопасности."
    
    
    
    
    scene bg11 nastya with Dissolve(.02)
    
    scene bg2 snowlight
 
scene bg11 nastya with Dissolve(.01)   

    
init:
    transform txt_up:
        yalign 1.5
        linear 15.0 yalign -1.5

label titri:
    scene black with dissolve
    show text "Идея:{p}Алексей 'ЭпиL' Михайлюк{p} {p}Код:{p}Алексей 'ЭпиL' Михайлюк{p} {p}Арты:{p} Алексей 'ЭпиL' Михайлюк{p} Интернет{p} {p}Спасибо за прохождение моей новеллы!{p}{p}{p}{p}Это только начало!" at txt_up
    pause 45
    stop sound fadeout 1
    return

return
