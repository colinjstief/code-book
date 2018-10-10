import React from 'react';
import App from './App/App';

export default class AppContainer extends React.Component {
  state = {};

  componentDidMount() {
    console.log('componentDidMount()');
  }
  render() {
    return <App />;
  }
}