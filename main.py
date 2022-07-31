from ui.main_ui import main
from threading import Thread
from scripts import trigger_record

th = Thread(target=trigger_record).start()
ui = Thread(target=main).start()