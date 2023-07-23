class WeeklyDataManager:

    def __init__(self, data, week_name) -> None:
        self.data = data
        self.week_name = week_name

    @property
    def week_data(self):
        return self.data[self.week_name]

    @week_data.setter
    def week_data(self, value):
        self.data[self.week_name] = value