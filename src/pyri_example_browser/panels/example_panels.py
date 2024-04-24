from typing import List, Dict, Callable, Any, Tuple
from pyri.webui_browser.plugins.panel import PyriWebUIBrowserPanelInfo, PyriWebUIBrowserPanelPluginFactory
from pyri.webui_browser import PyriWebUIBrowser
from pyri.webui_browser.golden_layout import PyriGoldenLayoutPanelConfig

_panel_infos = {
    "example": PyriWebUIBrowserPanelInfo(
        title="Example",
        description = "Example WebUI panel",
        panel_type = "example",
        panel_category = "example",
        component_type="pyri-example-component",
        priority=10000
    )
}

_panel_default_configs = {
    "example": PyriGoldenLayoutPanelConfig(
        component_type=_panel_infos["example"].component_type,
        panel_id = "example",
        panel_title = "Example",
        closeable= False
    )
}

class PyriExamplePanelsWebUIBrowserPanelPluginFactory(PyriWebUIBrowserPanelPluginFactory):
    def __init__(self):
        super().__init__()

    def get_plugin_name(self) -> str:
        return "pyri-example-browser"

    def get_panels_infos(self) -> Dict[str,PyriWebUIBrowserPanelInfo]:
        return _panel_infos

    def get_default_panels(self, layout_config: str = "default") -> List[Tuple[PyriWebUIBrowserPanelInfo, "PyriGoldenLayoutPanelConfig"]]:
        if layout_config.lower() == "default":
            return [
                (_panel_infos["example"], _panel_default_configs["example"])
            ]
        else:
            return []

def get_webui_browser_panel_factory():
    return PyriExamplePanelsWebUIBrowserPanelPluginFactory()