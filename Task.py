import datetime

class Task:
    def __init__(self, id, description, status="todo", createdAt=None, updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        current_time = datetime.datetime.now()
        self.createdAt = createdAt if createdAt is not None else current_time
        self.updatedAt = updatedAt if updatedAt is not None else current_time