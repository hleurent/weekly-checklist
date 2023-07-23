import json
import os

class DataManager:

    def __init__(self) -> None:
        self.WEEK_DAYS = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]

        __location__ = os.path.realpath(
                            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.file_path = os.path.join(__location__, '../checklists/NewTestFile.json')
        self.data = self.load()

        if self.data == {}:
            self.init_data()
            self.data = self.load()
            print(self.data)
    
    def load(self):
        data = {}
        try:
            with open(self.file_path, 'r') as json_file:
                try:
                    data = json.load(json_file)
                except json.decoder.JSONDecodeError:
                    data = {}

        except FileNotFoundError:
            data = {}
        
        return data

    def save(self, data : any) -> bool:
        if (not self.file_path.endswith(".json")):
            return False
        
        with open(self.file_path, 'w') as outfile:
            json.dump(data, outfile, indent = 4)

        return True

    def init_data(self):
        data = {"tasks" : [], "weeks" : []}
        self.save(data)

    def get_all_tasks(self):
        try:
            return self.data["tasks"]
        except KeyError:
            return []
        
    def add_task_name(self, name : str):
        try:
            if (name != "" and name not in self.data["tasks"]) :
                self.data["tasks"].append(name)
                self.save(self.data)
                return True
            return False
        
        except KeyError:
            self.data["tasks"] = [name]
            self.save(self.data)
            return True
    
    def delete_task(self, task_name: str):
        self.data["tasks"].remove(task_name)

        for day in self.data["days"]:
            if task_name in self.data["days"][day]:
                self.data["days"][day].remove(task_name)

        self.save(self.data)

    def task_exists(self, day:str, task:str):
        try:
            return task in self.data["days"][day]
        except KeyError:
            return False

    def toggle_task_state(self, day: str, task_name: str) -> None:
        try:
            if (self.task_exists(day, task_name)):
                self.data["days"][day].remove(task_name)
            else :
                self.data["days"][day].append(task_name)
        except KeyError:
            self.data["days"][day] = [task_name]
            
        self.save(self.data)


    def set_task_undone(self, day: str, task_name: str) -> None:
        try:
            if (self.task_exists(day, task_name)):
                self.data["days"][day].remove(task_name)
        except KeyError:
            self.data["days"][day] = [task_name]
            
        self.save(self.data)

    def get_last_week(self):
        return self.data["weeks"][-1] if len(self.data["weeks"]) > 0 else None

    def get_all_week_names(self):
        return [week["name"] for week in self.data["weeks"]]
    
    def get_week(self, week_name):
        print("week name : " + week_name)
        return next((week for week in self.data["weeks"] if week["name"] == week_name), None)
    
    def add_week(self, week_name) -> bool:
        if week_name != "" and week_name not in self.get_all_week_names():
            self.data["weeks"].append(
                {
                    "name" : week_name,
                    "days" : {}
                }
            )

            for day in self.WEEK_DAYS:
                self.data["weeks"][-1]["days"][day] = []

            self.save(self.data)
            return True
        
        return False

