from .protocols import {{cookiecutter.__protocol_name}}, {{cookiecutter.__presenter_protocol_name}}


class {{cookiecutter.presenter_name}}({{cookiecutter.__presenter_protocol_name}}):
	def __init__(self, view: {{cookiecutter.__protocol_name}}):
		self.view = view
		
		self.view.create_ui(self)
	
	def on_close(self):
		self.close()
	
	def close(self):
		self.view.destroy()
