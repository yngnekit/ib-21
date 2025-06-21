class LightingSystem:
    def turn_on(self):
        return "Освещение включено"

    def turn_off(self):
        return "Освещение выключено"

    def set_dim_level(self, level):
        return f"Уровень яркости установлен на {level}%"

class ClimateControlSystem:
    def set_temperature(self, temp):
        return f"Температура установлена на {temp}°C"

    def turn_off(self):
        return "Климат-контроль выключен"

class SecuritySystem:
    def arm(self):
        return "Сигнализация включена"

    def disarm(self):
        return "Сигнализация отключена"

class MultimediaSystem:
    def turn_on(self):
        return "Мультимедиа система включена"

    def play_music(self):
        return "Музыка воспроизводится"

    def turn_off(self):
        return "Мультимедиа система выключена"

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def home_mode(self):
        results = [
            self.lighting.turn_on(),
            self.climate.set_temperature(22),
            self.security.disarm()
        ]
        return results

    def away_mode(self):
        results = [
            self.lighting.turn_off(),
            self.multimedia.turn_off(),
            self.security.arm()
        ]
        return results

    def party_mode(self):
        results = [
            self.lighting.set_dim_level(40),
            self.multimedia.turn_on(),
            self.multimedia.play_music(),
            self.climate.set_temperature(20)
        ]
        return results

    def night_mode(self):
        results = [
            self.lighting.turn_off(),
            self.climate.set_temperature(18),
            self.security.arm()
        ]
        return results

    def get_all_systems_status(self):
        return (
            "Освещение: включено/выключено\n"
            "Климат: температура установлена\n"
            "Сигнализация: включена/выключена\n"
            "Мультимедиа: включена/выключена"
        )

# Клиентский код
def main():
    print("=== Тестирование паттерна Фасад для умного дома ===")

    # Создаем экземпляр фасада
    smart_home = SmartHomeFacade()

    # Проверяем начальное состояние
    print("\n1. Начальное состояние всех систем:")
    print(smart_home.get_all_systems_status())

    # Проверяем режим "Я дома"
    print("\n2. Активация режима 'Я дома':")
    home_results = smart_home.home_mode()
    for result in home_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я дома':")
    print(smart_home.get_all_systems_status())

    # Проверяем режим "Вечеринка"
    print("\n3. Активация режима 'Вечеринка':")
    party_results = smart_home.party_mode()
    for result in party_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Вечеринка':")
    print(smart_home.get_all_systems_status())

    # Проверяем режим "Ночь"
    print("\n4. Активация режима 'Ночь':")
    night_results = smart_home.night_mode()
    for result in night_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Ночь':")
    print(smart_home.get_all_systems_status())

    # Проверяем режим "Я ухожу"
    print("\n5. Активация режима 'Я ухожу':")
    away_results = smart_home.away_mode()
    for result in away_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я ухожу':")
    print(smart_home.get_all_systems_status())

    print("\n=== Тестирование завершено ===")

if __name__ == "__main__":
    main()