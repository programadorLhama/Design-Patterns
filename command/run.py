from button import Button
from receptor import Receptor
from commands import ButtonCommand

recep = Receptor()
butt = Button()

butt.set_command(ButtonCommand(recep, { "ola": "mundo" }))
butt.action()
