class DVD:

    months = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    def __init__(self, name: str, id_dvd: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_dvd
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_dvd: int, name: str, date: str, age_restriction: int):
        month, year = map(int, date.split(".")[1:])
        return cls(name, id_dvd, year, cls.months[month], age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status: {status}")
