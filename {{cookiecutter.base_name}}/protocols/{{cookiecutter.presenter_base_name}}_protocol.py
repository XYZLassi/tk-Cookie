from typing import Protocol


class {{cookiecutter.__presenter_protocol_name}}(Protocol):
	def on_close(self): ...
