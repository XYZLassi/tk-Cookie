import tkinter as tk

from .protocols import {{cookiecutter.name}}Protocol, {{cookiecutter.presenter_name}}Protocol


class {{cookiecutter.name}}({{cookiecutter.type}}, {{cookiecutter.name}}Protocol):
	def __init__(self, parent):
		super().__init__(parent)
	
	def create_ui(self, presenter: {{cookiecutter.presenter_name}}Protocol):
		# General
		self.protocol("WM_DELETE_WINDOW", presenter.close)
		
		# UI
		main_frame = tk.Frame(self)
		main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
