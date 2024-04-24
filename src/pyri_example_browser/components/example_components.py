from pyri.webui_browser.plugins.component import PyriWebUIBrowserComponentPluginFactory
from .example_component import register_vue_components as example_register_vue_components

class PyriExampleComponentsWebUIBrowserComponentPluginFactory(PyriWebUIBrowserComponentPluginFactory):
    def get_plugin_name(self) -> str:
        return "pyri-example-browser"

    def register_components(self) -> None:
        example_register_vue_components()
        

def get_webui_browser_component_factory():
    return PyriExampleComponentsWebUIBrowserComponentPluginFactory()