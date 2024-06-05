class Radiant:
    def get_message(self):
        return "Випромінювання"

class Radio(Radiant):
    def get_message(self):
        return "Радіохвилі"

class Sound(Radiant):
    def get_message(self):
        return "Звукові хвилі"

class Visible(Radiant):
    def get_message(self):
        return "Видиме світло"

class Infrared(Radiant):
    def get_message(self):
        return "Інфрачервоні промені"

class Ultraviolet(Radiant):
    def get_message(self):
        return "Ультрафіолетове випромінювання"

class Gamma(Radiant):
    def get_message(self):
        return "Гамма-випромінювання"

class Xray(Radiant):
    def get_message(self):
        return "Рентгенівське випромінювання"

class Device:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def get_messages(self):
        messages = [handler.get_message() for handler in self.handlers]
        return messages

class RadioDevice(Device):
    def __init__(self):
        super().__init__()
        self.add_handler(Radio())
        self.add_handler(Sound())

class Lamp(Device):
    def __init__(self):
        super().__init__()
        self.add_handler(Visible())
        self.add_handler(Infrared())
        self.add_handler(Ultraviolet())
        
radio_device = RadioDevice()
lamp = Lamp()

radio_messages = radio_device.get_messages()
lamp_messages = lamp.get_messages()

print("Повідомлення для класу 'Рація':")
for message in radio_messages:
    print(message)

print("\nПовідомлення для класу 'Лампочка':")
for message in lamp_messages:
    print(message)
