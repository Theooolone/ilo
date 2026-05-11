from typing import Required, Optional, TypedDict
from ilo import data

class _etymology_word(TypedDict):
    word: Required[str]
    alt: Optional[str]

class _audio_instance(TypedDict):
    author: Required[str]
    link: Required[str]

class Word:
    def __init__(self, json: dict):
        self.ID: str = json["id"]
        self.author_verbatim: str = json["author_verbatim"]
        self.author_source: str = json["author_source"]
        self.book: str = json["book"]
        self.coined_era: str = json["coined_era"]
        self.creation_date: str = json["creation_date"]
        self.author: list[str] = json["author"]
        self.ku_data: Optional[dict[str, int]] = json.get("ku_data")
        self.see_also: list[str] = json["see_also"]
        self.resources: dict[str, str] = json["resources"]
        self.representations: dict[str, str] = json["representations"]
        self.source_language: str = json["source_language"]
        self.usage_category: str = json["usage_category"]
        self.string: str = json["word"]
        self.deprecated: bool = json["deprecated"]
        self.audio: list[_audio_instance] = json["audio"]
        self.pu_verbatim: Optional[dict[str, str]] = json.get("pu_verbatim")
        self.usage: dict[str, int] = json["usage"]
        self.glyph_ids: list[str] = json["glyph_ids"]
        self.primary_glyph_id: Optional[str] = json.get("primary_glyph_id")
        self.image: Optional[str] = json.get("image")
        self.svg: Optional[str] = json.get("svg")
        self._commentary: dict[str, str] = {}
        self._definition: dict[str, str] = {}
        self._etymology: dict[str, str] = {}

    def add_lang(self, lang: str, json: dict):
        self._commentary[lang] = json["translations"]["commentary"]
        self._definition[lang] = json["translations"]["definition"]
        self._etymology[lang] = json["translations"]["etymology"]

    def get_usage(self) -> int:
        return next(reversed(self.usage.values())) if self.usage else 0

    def get_commentary(self, lang: str = "en") -> str:
        data.fetch_lang(lang)
        return self._commentary[lang]

    def get_definition(self, lang: str = "en") -> str:
        data.fetch_lang(lang)
        return self._definition[lang]

    def get_etymology(self, lang: str = "en") -> str:
        data.fetch_lang(lang)
        return self._etymology[lang]
