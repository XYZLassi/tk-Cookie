from .protocols import {{cookiecutter.name}}Protocol, {{cookiecutter.presenter_name}}Protocol


class {{cookiecutter.presenter_name}}({{cookiecutter.presenter_name}}Protocol):
	def __init__(self, view: {{cookiecutter.name}}Protocol):
		self.view = view
		
		self.view.create_ui(self)
		
	def close(self):
		self.view.destroy()
