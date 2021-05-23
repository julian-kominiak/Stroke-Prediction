import React, {Component} from 'react';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import Paper from 'material-ui/Paper';
import Probability from "./components/Probability";

const style = {
    marginLeft: 12,
};

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            sample: '',
            probability: undefined
        };
    };

    analyzeSample() {
        fetch('http://localhost:8080/sample_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: this.textField.getValue()
        })
            .then(response => response.json())
            .then(data => this.setState(data));
    }

    onEnterPress = e => {
        if (e.key === 'Enter') {
            this.analyzeSample();
        }
    };

    render() {
        const probabilityComponent = this.state.probability !== undefined ?
            <Probability sample={this.state.sample} probability={this.state.probability}/> :
            null;

        return (
            <MuiThemeProvider>
                <div className="centerize">
                    <Paper zDepth={1} className="content">
                        <h2>Stroke Prediction</h2>
                        <TextField ref={ref => this.textField = ref} onKeyUp={this.onEnterPress.bind(this)}
                                   hintText="Enter Your data sample:"/>
                        <RaisedButton  label="Send" style={style} onClick={this.analyzeSample.bind(this)}/>
                        {probabilityComponent}
                    </Paper>
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;