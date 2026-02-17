from enum import Enum

class Language(str, Enum):
    ro = "ro"
    ru = "ru"

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