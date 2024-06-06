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

class RadioDevice(Sound, Radio):
    pass

class Lamp(Infrared, Visible, Ultraviolet):
    pass

class TNT(Sound, Visible, Infrared, Radio):
    pass

class Sun(Infrared, Visible, Ultraviolet, Xray, Gamma):
    pass

radio_device = RadioDevice()
lamp = Lamp()

radio_message = radio_device.get_message()
lamp_message = lamp.get_message()

print(radio_message)
print(lamp_message)
