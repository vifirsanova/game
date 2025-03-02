# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Alice = Character('Алиса', color="#c8ffc8")
define Violinist = Character('Скрипач', color="#c8ffc8")
define Hatter = Character('Шляпник', color="#c8ffc8")
define CheshireCat = Character('Чеширский кот', color="#c8ffc8")
define Duchess = Character('Герцогиня', color="#c8ffc8")
define Turtle = Character('Черепаха', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    Alice "Вы создали новую игру Ren'Py."

    Alice "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
