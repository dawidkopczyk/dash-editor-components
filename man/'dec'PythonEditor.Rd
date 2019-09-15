% Auto-generated: do not edit by hand
\name{'dec'PythonEditor}

\alias{'dec'PythonEditor}

\title{PythonEditor component}

\description{
PythonEditor is a Python code editor comopnent. allowing for highlighting code in textarea component.
}

\usage{
'dec'PythonEditor(id=NULL, value=NULL, tabSize=NULL, insertSpaces=NULL, ignoreTabKey=NULL,
padding=NULL, autoFocus=NULL, disabled=NULL, form=NULL, name=NULL,
placeholder=NULL, readOnly=NULL, required=NULL, className=NULL, style=NULL,
loading_state=NULL)
}

\arguments{
\item{id}{Character. The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.}

\item{value}{Character. The value of the textarea.}

\item{tabSize}{Numeric. TabSize of PythonEditor.}

\item{insertSpaces}{Logical. Determines whether to insert spaces.}

\item{ignoreTabKey}{Logical. Determines whether to ignore tab key.}

\item{padding}{Character | numeric. Padding of PythonEditor container.}

\item{autoFocus}{Character. The element should be automatically focused after the page loaded.}

\item{disabled}{Character | logical. Indicates whether the user can interact with the element.}

\item{form}{Character. Indicates the form that is the owner of the element.}

\item{name}{Character. Name of the element. For example used by the server to identify the fields in form submits.}

\item{placeholder}{Character. Provides a hint to the user of what can be entered in the field.}

\item{readOnly}{Logical | a value equal to: 'readonly', 'readonly', 'readonly'. Indicates whether the element can be edited.
readOnly is an HTML boolean attribute - it is enabled by a boolean or
'readOnly'. Alternative capitalizations `readonly` & `READONLY`
are also acccepted.}

\item{required}{A value equal to: 'required', 'required' | logical. Indicates whether this element is required to fill out or not.
required is an HTML boolean attribute - it is enabled by a boolean or
'required'. Alternative capitalizations `REQUIRED`
are also acccepted.}

\item{className}{Character. Often used with CSS to style elements with common properties.}

\item{style}{Named list. Defines CSS styles which will override styles previously set.}

\item{loading_state}{Lists containing elements 'is_loading', 'prop_name', 'component_name'.
those elements have the following types:
  - is_loading (logical; optional): determines if the component is loading or not
  - prop_name (character; optional): holds which property is loading
  - component_name (character; optional): holds the name of the component that is loading. Object that holds the loading state object coming from dash-renderer}
}
