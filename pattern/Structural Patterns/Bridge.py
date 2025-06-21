class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_state(self, state):
        pass

class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.state = None
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            print(f"{self.brand} TV включен.")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print(f"{self.brand} TV выключен.")
            self.is_on = False

    def set_state(self, state):
        if self.is_on:
            self.state = state
            print(f"{self.brand} TV: канал изменён на {self.state}")

class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.state = None
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            print(f"{self.brand} лампа включена.")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print(f"{self.brand} лампа выключена.")
            self.is_on = False

    def set_state(self, state):
        if self.is_on:
            self.state = state
            print(f"{self.brand} лампа: яркость установлена на {self.state}")

class SonyTV(TV):
    def __init__(self):
        super().__init__("Sony")


class SamsungTV(TV):
    def __init__(self):
        super().__init__("Samsung")


class PhilipsLight(Light):
    def __init__(self):
        super().__init__("Philips")


class IKEALight(Light):
    def __init__(self):
        super().__init__("IKEA")

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state):
        self.device.set_state(state)

def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    print("-" * 40)

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    print("-" * 40)

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    print("-" * 40)

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()


if __name__ == "__main__":
    main()