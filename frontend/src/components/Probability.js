import React, {Component} from 'react';
import PropTypes from 'prop-types';

class Probability extends Component {

    propTypes = {
        probability: PropTypes.number.isRequired
    };

    render() {
        const green = Math.round((this.props.probability + 1) * 128);
        const red = 255 - green;
        const textColor = {
            backgroundColor: 'rgb(' + red + ', ' + green + ', 0)',
            padding: '15px'
        };

        return <div style={textColor}> Probability of stroke is {this.props.probability} % </div>
    }
}

export default Probability;