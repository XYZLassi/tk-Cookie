from typing import Protocol

from .{{cookiecutter.presenter_base_name}}_protocol import {{cookiecutter.presenter_name}}Protocol


class {{cookiecutter.name}}Protocol(Protocol):
	def create_ui(self, presenter: {{cookiecutter.presenter_name}}Protocol): ...
	
	def destroy(self): ...
