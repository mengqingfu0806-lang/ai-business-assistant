from config import settings
from core.assistant import Assistant

print(settings.PROJECT_NAME)
print(settings.VERSION)
print(settings.ENVIRONMENT)
assistant = Assistant()

print(assistant.initialize())
