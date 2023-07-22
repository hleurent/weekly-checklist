import json
import os

class DataManager:

    def __init__(self) -> None:
        __location__ = os.path.realpath(
                            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.file_path = os.path.join(__location__, '../checklists/WeeklyCheckList.json')
        self.data = self.load()
    
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


