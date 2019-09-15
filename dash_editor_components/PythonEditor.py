# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PythonEditor(Component):
    """A PythonEditor component.
PythonEditor is a Python code editor comopnent.
allowing for highlighting code in textarea component.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- value (string; default ""): The value of the textarea.
- tabSize (number; default 4): TabSize of PythonEditor.
- insertSpaces (boolean; default True): Determines whether to insert spaces.
- ignoreTabKey (boolean; default False): Determines whether to ignore tab key.
- padding (string | number; default 10): Padding of PythonEditor container.
- autoFocus (string; optional): The element should be automatically focused after the page loaded.
- disabled (string | boolean; optional): Indicates whether the user can interact with the element.
- form (string; optional): Indicates the form that is the owner of the element.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- placeholder (string; default "Type some code here..."): Provides a hint to the user of what can be entered in the field.
- readOnly (boolean | a value equal to: 'readOnly', 'readonly', 'READONLY'; optional): Indicates whether the element can be edited.
readOnly is an HTML boolean attribute - it is enabled by a boolean or
'readOnly'. Alternative capitalizations `readonly` & `READONLY`
are also acccepted.
- required (a value equal to: 'required', 'REQUIRED' | boolean; optional): Indicates whether this element is required to fill out or not.
required is an HTML boolean attribute - it is enabled by a boolean or
'required'. Alternative capitalizations `REQUIRED`
are also acccepted.
- className (string; optional): Often used with CSS to style elements with common properties.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, tabSize=Component.UNDEFINED, insertSpaces=Component.UNDEFINED, ignoreTabKey=Component.UNDEFINED, padding=Component.UNDEFINED, autoFocus=Component.UNDEFINED, disabled=Component.UNDEFINED, form=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'tabSize', 'insertSpaces', 'ignoreTabKey', 'padding', 'autoFocus', 'disabled', 'form', 'name', 'placeholder', 'readOnly', 'required', 'className', 'style', 'loading_state']
        self._type = 'PythonEditor'
        self._namespace = 'dash_editor_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'tabSize', 'insertSpaces', 'ignoreTabKey', 'padding', 'autoFocus', 'disabled', 'form', 'name', 'placeholder', 'readOnly', 'required', 'className', 'style', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PythonEditor, self).__init__(**args)
