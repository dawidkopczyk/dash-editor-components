# AUTO GENERATED FILE - DO NOT EDIT

'dec'PythonEditor <- function(id=NULL, value=NULL, tabSize=NULL, insertSpaces=NULL, ignoreTabKey=NULL, padding=NULL, autoFocus=NULL, disabled=NULL, form=NULL, name=NULL, placeholder=NULL, readOnly=NULL, required=NULL, className=NULL, style=NULL, loading_state=NULL) {
    
    props <- list(id=id, value=value, tabSize=tabSize, insertSpaces=insertSpaces, ignoreTabKey=ignoreTabKey, padding=padding, autoFocus=autoFocus, disabled=disabled, form=form, name=name, placeholder=placeholder, readOnly=readOnly, required=required, className=className, style=style, loading_state=loading_state)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PythonEditor',
        namespace = 'dash_editor_components',
        propNames = c('id', 'value', 'tabSize', 'insertSpaces', 'ignoreTabKey', 'padding', 'autoFocus', 'disabled', 'form', 'name', 'placeholder', 'readOnly', 'required', 'className', 'style', 'loading_state'),
        package = 'dashEditorComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
