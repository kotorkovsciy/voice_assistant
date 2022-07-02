# import speech_recognition as sr
from speech_recognition import Recognizer, Microphone
from json import load, loads, dumps
from plugins.mainCMD import say_hello, say_time


def record_volume():
    r = Recognizer()

    with Microphone(device_index=2) as source:
        print('Слушаю...')
        audio = r.listen(source)

    query = r.recognize_google(audio, language='ru-RU')
    for x in query.split(' '):
        for y in list(out_dir('command.json').items()):
            if x.lower() in y[1]["examples"]:
                commands(y[1]["commands"])

    print(f'Вы сказали: {query.lower()}')


def out_dir(filename):
    with open(filename, encoding='utf 8') as f:
        directs = load(f)
    return loads(dumps(directs, indent=4, sort_keys=True, ensure_ascii=False).replace("'", '"'))


def commands(cmd):
    match cmd:
        case "say_hello":
            say_hello()
        case "say_time":
            say_time()
