import tkinter as tk

from .protocols import {{cookiecutter.__protocol_name}}, {{cookiecutter.__presenter_protocol_name}}


class {{cookiecutter.name}}({{cookiecutter.__type}}, {{cookiecutter.__protocol_name}}):
	def __init__(self, parent):
		super().__init__(parent)

	# noinspection PyAttributeOutsideInit, DuplicatedCode
	def create_ui(self, presenter: {{cookiecutter.__presenter_protocol_name}}):
		# General
		{%- if cookiecutter.type == "Toplevel"%}
		self.protocol("WM_DELETE_WINDOW", presenter.on_close)
		{%- endif %}
		
		# UI
		main_frame = tk.Frame(self)
		main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
