from .protocols import {{cookiecutter.__protocol_name}}, {{cookiecutter.__presenter_protocol_name}}


class {{cookiecutter.presenter_name}}({{cookiecutter.__presenter_protocol_name}}):
	def __init__(self, view: {{cookiecutter.__protocol_name}}):
		self.__view : {{cookiecutter.__protocol_name}} | None = view
		
		self.view.create_ui(self)
	
	@property
	def view(self) -> {{cookiecutter.__protocol_name}}:
		if self.__view is None:
			raise RuntimeError('View is not initialized')
		return self.__view

	def on_close(self):
		self.close()
	
	def close(self):
		self.view.destroy()
