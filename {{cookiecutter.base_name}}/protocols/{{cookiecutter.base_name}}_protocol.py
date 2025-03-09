from typing import Protocol

from .{{cookiecutter.presenter_base_name}}_protocol import {{cookiecutter.__presenter_protocol_name}}


class {{cookiecutter.__protocol_name}}(Protocol):
	def create_ui(self, presenter: {{cookiecutter.presenter_name}}Protocol): ...
	
	def destroy(self): ...
