class BMW:
    def __init__(self, model, year, color, horsepower, fuel_type, mileage):
        self.model = model
        self.year = year
        self.color = color
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.status = "stopped"  # car status: running or stopped

    def start_engine(self):
        if self.status == "running":
            print("Engine is already running.")
        else:
            self.status = "running"
            print("Engine started.")

    def stop_engine(self):
        if self.status == "stopped":
            print("Engine is already stopped.")
        else:
            self.status = "stopped"
            print("Engine stopped.")

    def accelerate(self):
        if self.status == "running":
            print(f"The {self.model} is accelerating.")
        else:
            print("Start the engine first to accelerate.")

    def brake(self):
        if self.status == "running":
            print(f"The {self.model} is braking.")
        else:
            print("Start the engine first to brake.")

    def display_details(self):
        return (f"BMW Model: {self.model}, Year: {self.year}, "
                f"Color: {self.color}, Horsepower: {self.horsepower} HP, "
                f"Fuel Type: {self.fuel_type}, Mileage: {self.mileage} km, "
                f"Status: {self.status}")
