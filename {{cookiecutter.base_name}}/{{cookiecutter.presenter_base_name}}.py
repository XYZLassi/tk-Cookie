{%- if cookiecutter.type == "Toplevel" -%}
from typing import Callable
{%- endif %}

from .protocols import {{cookiecutter.__protocol_name}}, {{cookiecutter.__presenter_protocol_name}}


class {{cookiecutter.presenter_name}}({{cookiecutter.__presenter_protocol_name}}):
	{%- if cookiecutter.type == "Toplevel" %}
	def __init__(self, view_factory: Callable[[], {{cookiecutter.__protocol_name}}]):
		self.__view_factory: Callable[[], {{cookiecutter.__protocol_name}}] = view_factory
		self.__view: {{cookiecutter.__protocol_name}} | None = None
	{%- else %}
	def __init__(self, view: {{cookiecutter.__protocol_name}}):
		self.__view: {{cookiecutter.__protocol_name}} | None = view
		
		self.view.create_ui(self)
	{%- endif %}
	
	@property
	def view(self) -> {{cookiecutter.__protocol_name}}:
		if self.__view is None:
			raise RuntimeError('View is not initialized')
		return self.__view

	{% if cookiecutter.type == "Toplevel" -%}
	def show(self):
		self.__view = self.__view_factory()
		self.view.create_ui(self)
	{%- endif %}
	
	def close(self):
		if self.__view:
			self.__view.destroy()
			self.__view = None
	
	def on_close(self):
		self.close()
