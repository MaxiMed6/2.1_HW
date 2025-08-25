class Romb:
    def __init__(self, storona_a, angle_a, angle_b):
        self.storona_a = storona_a
        self.angle_a = angle_a
        self.angle_b = angle_b

        if angle_a + angle_b != 180:
            raise ValueError("Сума кутів повинна бути 180°")

    def __setattr__(self, name, value):
        if name == "storona_a":
            if value <= 0:
                raise ValueError("Сторона повинна бути більше 0")
            self.__dict__[name] = value
        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError(" Кут повинен бути від 1 - 179")
            self.__dict__[name] = value

            self.__dict__["angle_b"] = 180 - value
        elif name == "angle_b":
            if value <= 0 or value >= 180:
                raise ValueError("Кут повинен бути від 1 - 179")
            self.__dict__[name] = value
            self.__dict__["angle_a"] = 180 - value
        else:
            self.__dict__[name] = value


    def __str__(self):
        return f"Ромб: сторона = {self.storona_a}, кут_a = {self.angle_a}°, кут_б = {self.angle_b}°"


if __name__ == "__main__":
    try:
        rombik = Romb(5, 60, 120)
        print(rombik)

        rombik.storona_a = 10
        rombik.angle_a = 30
        print(rombik)

        # rombik.angle_b = 0
        rombik.storona_a = 0


    except ValueError as e:
        print(f"Помилка: {e}")

