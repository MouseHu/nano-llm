import functools
from typing import NamedTuple


class SpecialToken(NamedTuple):
    def __init__(self, token: str, id: int):
        self._token = token
        self._id = id

    def get_token(self):
        return self._token

    def get_id(self):
        return self._id


class SpecialTokens:
    eos = SpecialToken(None, "[EOS]")
    bos = SpecialToken(None, "[BOS]")
    pad = SpecialToken(None, "[PAD]")
    unk = SpecialToken(None, "[UNK]")


@functools.cache
def _name_to_special_token_map() -> dict[str, SpecialToken]:
    return {
        "eos": SpecialTokens.eos,
        "bos": SpecialTokens.bos,
        "pad": SpecialTokens.pad,
        "unk": SpecialTokens.unk,
    }
