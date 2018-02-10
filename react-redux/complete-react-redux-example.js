// Provider preload
// Component dispatch (mapDispatchToProps)
// -----> Middleware
// Action
// Reducer
// Store
// -----> Selector (mapStateToProps)
// Component render

/* --------------------------------------------------------------------------------------------------------------- */

/////////////////////////
// 1. Component

// React-redux
import React from 'react';
import { connect } from 'react-redux';

// Components
import Child from './components/Child';
import Item from './components/Item';

// Actions
import { changeTool } from '../actions/toolbox';

// Selectors

export default class Parent extends React.Component {

  state = {
    count: 0
  }

  handleClick = () => {
    this.setState((prevState) => {
      return {
        clicks: prevState.clicks += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>In parent: {this.state.clicks}</p>
        <button onClick={this.handleClick}>+1</button>
        <Child localState={this.state.clicks} localAction={this.handleClick} />
        <ul className="itemList">
          {
            props.items.length === 0 ? (
              <p>No items</p>
            ) : (
                props.items.map((expense) => {
                  return <Item key={expense.id} {...expense} />;
                })
              )
          }
        </ul>
      </div>
    )
  }
};

const mapStateToProps = (state) => ({
  items: state.list
});

const mapDispatchToProps = (dispatch) => ({
  changeTool: (tool) => dispatch(changeTool(tool))
});

export default connect(mapStateToProps, mapDispatchToProps)(Parent);


// ./components/Child
const Child = (props) => (
  <div className="child">
    <p>In child: {props.localState}</p>
    <button onClick={props.localAction}>+1 from child</button>
  </div>
);

// ./components/Item
const Item = ({ id, description, amount, createdAt }) => (
  <div>
    <Link to={`/edit/${id}`}>
      <h3>{description}</h3>
    </Link>
    <p>
      {numeral(amount / 100).format('$0,0.00')}
      -
      {moment(createdAt).format('MMMM Do, YYYY')}
    </p>
  </div>
);

export class Sidebar extends React.Component {

  changeTool = (e) => {
    const tool = e.target.dataset.tool || "";
    this.props.changeTool(tool);
  }

  render() {
    return (
      <div className={!this.props.menuOpen ? "sidebar" : 'sidebar sidebar--open'}>
        <div className="masthead">
          <img src="/images/ct-logo.png" className="ct-logo" />
        </div>
        <Toolbox tool={this.props.tool} changeTool={this.changeTool} />
      </div>
    )
  }

}

const mapStateToProps = (state) => ({
  tool: state.toolbox.tool,
  menuOpen: state.menu.open
});

const mapDispatchToProps = (dispatch) => ({
  changeTool: (tool) => dispatch(changeTool(tool))
});

export default connect(mapStateToProps, mapDispatchToProps)(Sidebar);

/////////////////////////
// 2. Middlware


/////////////////////////
// 3. Action


/////////////////////////
// 4. Reducer


/////////////////////////
// 5. Component