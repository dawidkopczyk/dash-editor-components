import React, {Component} from 'react';
import PropTypes from 'prop-types';
import classnames from 'classnames';
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';

/**
 * PythonEditor is a Python code editor comopnent.
 * allowing for highlighting code in textarea component.
 */
export default class PythonEditor extends Component {

	constructor(props) {
        super(props);
	}
		
    render() {
		const { 
			id,
			value,
			className,
			loading_state, 
			setProps,
			...otherProps
		} = this.props;
  
        return (
			<Editor
			    data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
				textareaId={id}
				value={value}
				onValueChange={code => setProps({ value: code })}
				highlight={code => highlight(code, languages.python)}
				className={classnames('container__editor', className)}
				{...otherProps}
			/>
        );
    }
}

PythonEditor.defaultProps = {
    tabSize: 4,
    insertSpaces: true,
    ignoreTabKey: false,
    padding: 10,
	placeholder: "Type some code here...",
	value: ""
};

PythonEditor.propTypes = {
	/**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,

    /**
     * The value of the textarea.
     */
    value: PropTypes.string,

    /**
     * TabSize of PythonEditor.
     */
    tabSize: PropTypes.number,

    /**
     * Determines whether to insert spaces.
     */
    insertSpaces: PropTypes.bool,

    /**
     * Determines whether to ignore tab key.
     */
    ignoreTabKey: PropTypes.bool,

    /**
     * Padding of PythonEditor container.
     */
    padding: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
	
    /**
     * The element should be automatically focused after the page loaded.
     */
    autoFocus: PropTypes.string,

    /**
     * Indicates whether the user can interact with the element.
     */
    disabled: PropTypes.oneOfType([PropTypes.string, PropTypes.bool]),

    /**
     * Indicates the form that is the owner of the element.
     */
    form: PropTypes.string,

    /**
     * Name of the element. For example used by the server to identify the fields in form submits.
     */
    name: PropTypes.string,

    /**
     * Provides a hint to the user of what can be entered in the field.
     */
    placeholder: PropTypes.string,

    /**
     * Indicates whether the element can be edited.
     * readOnly is an HTML boolean attribute - it is enabled by a boolean or
     * 'readOnly'. Alternative capitalizations `readonly` & `READONLY`
     * are also acccepted.
     */
    readOnly: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['readOnly', 'readonly', 'READONLY']),
    ]),

    /**
     * Indicates whether this element is required to fill out or not.
     * required is an HTML boolean attribute - it is enabled by a boolean or
     * 'required'. Alternative capitalizations `REQUIRED`
     * are also acccepted.
     */
    required: PropTypes.oneOfType([
        PropTypes.oneOf(['required', 'REQUIRED']),
        PropTypes.bool,
    ]),

    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,

    /**
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,

	/**
	* Object that holds the loading state object coming from dash-renderer
	*/
	loading_state: PropTypes.shape({
		/**
		* Determines if the component is loading or not
		*/
		is_loading: PropTypes.bool,
		/**
		* Holds which property is loading
		*/
		prop_name: PropTypes.string,
		/**
		* Holds the name of the component that is loading
		*/
		component_name: PropTypes.string
	}),
	
    /**
     * Dash-assigned callback that gets fired when the value changes.
     */
    setProps: PropTypes.func
	
};
