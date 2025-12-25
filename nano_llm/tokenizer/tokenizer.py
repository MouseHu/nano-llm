import abc


class TokenizerImpl(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def encode(self, text):
        pass

    @abc.abstractmethod
    def decode(self, tokens):
        pass

    @abc.abstractmethod
    def get_vocab(self):
        pass

    @abc.abstractmethod
    def get_special_tokens(self):
        pass

    @abc.abstractmethod
    def get_special_token_id(self, special_token):
        pass


class Tokenizer:
    def __init__(self, tokenizer_impl: TokenizerImpl):
        self._tokenizer_impl = tokenizer_impl

    def encode(self, text):
        return self._tokenizer_impl.encode(text)

    def decode(self, tokens):
        return self._tokenizer_impl.decode(tokens)
