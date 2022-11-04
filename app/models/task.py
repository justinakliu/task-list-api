from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {"id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": bool(self.completed_at)
                }

    @classmethod
    def from_dict(cls, data):
        return Task(title=data["title"],
                    description=data["description"]
                    )