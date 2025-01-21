from pydantic import BaseModel


class NotificationModel(BaseModel):
    user_email: str
    message: str
