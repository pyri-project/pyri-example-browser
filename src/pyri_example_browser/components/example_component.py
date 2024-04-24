from typing import List, Dict, Callable, Any
import importlib_resources
from RobotRaconteur.Client import *
from pyri.webui_browser.pyri_vue import PyriVue, VueComponent, vue_register_component, vue_data, \
    vue_method, vue_prop, vue_computed, vue_watch
import asyncio

import numpy as np


@VueComponent
class ExampleComponent(PyriVue):

    vue_template = importlib_resources.read_text(__package__,"example_component.html")

    current_value = vue_data(0)

    def __init__(self):
        super().__init__()

    def core_ready(self):
        # Called when the WebUI core class is ready
        pass

    @vue_method
    def increment(self, *args):
        self.current_value = self.current_value + 1

    @vue_method
    def decrement(self, *args):
        self.current_value = self.current_value - 1

    # @vue_method can also be async for use with Robot Raconteur calls


def register_vue_components():
    vue_register_component("pyri-example-component", ExampleComponent)

