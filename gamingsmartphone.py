# Part 1: Designing the gaming smartphone with smartphone as class

# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        """Constructor to initialize smartphone attributes"""
        self.brand = brand # e.g., Samsung
        self.model = model # e.g., Galaxy S23
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
        self.battery_remaining = battery_life  # start with full battery

    def make_call(self, number):
        """Simulates making a phone call"""
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def browse_internet(self, hours):
        """Simulates browsing the internet and reducing battery"""
        if hours <= self.battery_remaining:
            self.battery_remaining -= hours
            print(f"{self.brand} {self.model} browsed the internet for {hours}h. "
                  f"Battery left: {self.battery_remaining}h")
        else:
            print(f"Not enough battery to browse for {hours}h. Please recharge!")

    def charge(self):
        """Recharge the phone back to full battery"""
        self.battery_remaining = self.battery_life
        print(f"{self.brand} {self.model} has been fully charged 🔋")


# Subclass: GamingSmartphone (inherits Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system=True, bigger_RAM=True, rotate_screen=True):
        """Constructor adds a gaming-specific feature"""
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system
        self.bigger_RAM = bigger_RAM
        self.rotate_screen = rotate_screen

    def play_game(self, game, hours):
        """Simulates playing a game, drains more battery"""
        drain = hours * 2  # gaming drains 2x faster
        if drain <= self.battery_remaining:
            self.battery_remaining -= drain
            print(f"{self.brand} {self.model} played {game} for {hours}h 🎮. "
                  f"Battery left: {self.battery_remaining}h")
        else:
            print(f"Not enough battery to play {game} for {hours}h.")


# Objects in smartphone class and subsequent subclass
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 24)
phone1.make_call("+254712345678")
phone1.browse_internet(5)
phone1.charge()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 20)
gaming_phone.play_game("PUBG", 3)
gaming_phone.browse_internet(2)
