/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { PythonEditor } from '../lib';

class App extends Component {

    constructor() {
        super();
    }

    render() {
        return (
            <div>
                <PythonEditor/>
            </div>
        )
    }
}

export default App;
