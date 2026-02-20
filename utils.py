from enum import Enum
from pydantic import BaseModel

class Language(str, Enum):
    ro = "ro"
    ru = "ru"

class Pagination(BaseModel):
    skip: int
    limit: int

class UserRole(str, Enum):
    user = "user"
    admin = "admin"

def get_translation(translations, lang: Language):
    translation = next(
        (t for t in translations if t.language == lang),
        None
    )
    if not translation:
        translation = next(
            (t for t in translations if t.language == Language.ro),
            None
        )
    return translation