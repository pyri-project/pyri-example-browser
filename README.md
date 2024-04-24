# PyRI WebUI Browser Example Plugin

This package contains a simple example of extending the PyRI WebUI that runs inside a browser. The Python
code is executed using [Pyodide](https://github.com/pyodide/pyodide), a Web Assembly implementation of Python. The
PyRI WebUI uses [Vue](https://vuejs.org/), and the panels are implemented a Vue components that are added to
the layout, typically as a new tab.

## Usage

The WebUI works by placing Python Wheels used by the WebUI in a special directory separate from the
standard Python package directory. These wheels are loaded into Pyodide by the browser when the page is loaded,
and extracted into the packages directory of Pyodide. The "entry points" listed in the `pyproject.toml`
file are then interrogated to load the correct plugin factories. For the WebUI plugins, the relevant entry points
are `pyri.plugins.webui_browser_panel` and `pyri.plugins.webui_browser_component`. The wheel directory is located
at `%LOCALAPPDATA%\pyri-project\pyri-webui-server\wheels` on Windows, and `$HOME/.local/pyri-webui-server/wheels`
on Linux and Mac.

The plugin can be installed automatically using `pyri-cli`. For development use, run:

```
pyri-cli dev --dev-install-webui
```

in the parent directory of your package source. This will compile the wheel, determine required dependencies,
and copy the compiled wheels and dependencies into the wheels directory.

For deployment, use `pyri-cli webui-install` as described in the core readme.

Note that the "keywords" section of pyproject.toml is important and must contain the `pyri-*` entries for
the cli to work correctly.

## Source file descriptions

- `README.md`: The readme (you are here!)
- `pyproject.toml`: Package configuration file
- `LICENSE.txt`: License file
- `.gitignore`: Git ignore file. Highly recommended to avoid committing temporary files.
- `pyri_example_browser/__init__.py`: Empty file to mark the directory as a Python package
- `pyri_example_browser/components/__init__.py`: Empty file to mark the directory as a Python package
- `pyri_example_browser/components/example_component.html`: Vue template HTML for the "example" component
- `pyri_example_browser/components/example_component.py`: Python implementation of the "example" component
- `pyri_example_browser/components/example_components.py`: Components factory class for the package
- `pyri_example_browser/panels/__init__.py`: Empty file to mark the directory as a Python package
- `pyri_example_browser/panels/example_panels.py`: Panel definition for the "Example" panel, and Panels factory class for the package

Note the `pyproject.toml` must contain special `pyri-*` keywords, entry points definitions for the factories,
and `tool.setuptools.package-data` entries to include non-Python files in the wheel.