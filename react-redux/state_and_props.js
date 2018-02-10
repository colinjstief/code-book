// SFC = Stateless functional comopnent
// CBC = Class-based component

////////////////////////////
// React props

// SFC --> SFC
// CBC (Standard) --> SFC
// CBC (Standard) --> CBC (Standard)
// CBC (Standard) --> CBC (New class property syntax)

// SFC --> SFC
// Child uses props.propKey from props object passed to function

const Parent = () => (
  <div className="parent">
    <Child propA="valueA" />
    <OtherChild probB="valueB" propC="valueC" />
  </div>
);

const Child = (props) => ( // Whole object
  <div className="child">
    <p>{props.propA}</p>
  </div>
);

const OtherChild = ({ probB, propC }) => ( // Destructuring
  <div className="other-child">
    <p>{propB}</p>
    <p>{probC}</p>
  </div>
);

// CBC (Standard) --> SFC
// Child uses props.propKey from props object passed to function
// As a class, can also pass functions defined internally

export default class Parent extends React.Component {

  parentAction() {
    alert("hello!");
  }

  render() {
    return (
      <div className="parent">
        <Child propA="valueA" propAction={this.parentAction} />
      </div>
    )
  }
};

const Child = (props) => (
  <div className="child">
    <p>{props.propA}</p>
    <button onClick={props.propAction}>Click me</button>
  </div>
);

// CBC (Standard) --> CBC (Standard)
// Child uses this.props.propKey
// As a class, the parent component can also pass functions defined internally
// As a class, the child component defines a 'constructor' method so we can bind functions that reference 'this' keyword
// We also need to add super(props) in order to properly define things passed in from the parent

export default class Parent extends React.Component {

  parentAction() {
    alert("Hello from the parent!");
  }

  render() {
    return (
      <div className="parent">
        <Child propA="valueA" propAction={this.parentAction} />
      </div>
    )
  }
};

export default class Child extends React.Component {

  constructor(props) {
    super(props)
    this.childActionB = this.childActionB.bind(this);
  }

  childActionA() {
    alert("Hi from the child!");
  }

  childActionB() {
    alert(`Called from child with data from the parent! propA: ${this.props.propA}`);
  }

  render() {
    return (
      <div className="child">
        <p>{this.props.propA}</p>
        <button onClick={this.props.propAction}>Parent method</button>
        <button onClick={this.childActionA}>Child method</button>
        <button onClick={this.childActionB}>Child method, with parent data</button>
      </div>
    )
  }
};

// CBC (Standard) --> CBC (New class property syntax)
// Child uses this.props.propKey
// As a class, the parent component can also pass functions defined internally
// As a class with the new property syntax and arrow functions, the child component 
// does not need a constructor function to access the this keyword or parent props

export default class Parent extends React.Component {

  parentAction() {
    alert("Hello from the parent!");
  }

  render() {
    return (
      <div className="parent">
        <Child propA="valueA" propAction={this.parentAction} />
      </div>
    )
  }
};

export default class Child extends React.Component {

  childActionA = () => {
    alert(`Called from child with data from the parent! propA: ${this.props.propA}`);
  }

  render() {
    return (
      <div className="child">
        <p>{this.props.propA}</p>
        <button onClick={this.props.propAction}>Parent method</button>
        <button onClick={this.childActionA}>Child method, with parent data</button>
      </div>
    )
  }

};

////////////////////////////
// React state

// CBC (Standard) --> SFC
// CBC (Standard) --> CBC (Standard)
// CBC (Standard) --> CBC (New class property syntax)
// CBC (New class property syntax) --> SFC
// CBC (New class property syntax) --> CBC (New class property syntax)

// 1. Setup default state object
// 2. Component is rendered with default state values
// 3. Change state based on event
// 4. Component is re-rendered with new state values
// 5. Start again at 3


// CBC (Standard) --> SFC
export default class Parent extends React.Component {

  constructor(props) {
    super(props);
    this.handleAdd = this.handleAdd.bind(this);

    this.state = {
      count: 0
    }

  }

  handleAdd() {
    this.setState((prevState) => {
      return {
        count: prevState.count += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>In parent: {this.state.count}</p>
        <button onClick={this.handleAdd}>+1</button>
        <Child propFromState={this.state.count} />
      </div>
    )
  }
};

const Child = (props) => (
  <div className="child">
    <p>In child: {props.propFromState}</p>
  </div>
);

// CBC (Standard) --> CBC (Standard)
export default class Parent extends React.Component {

  constructor(props) {
    super(props);
    this.handleAddParent = this.handleAddParent.bind(this);

    this.state = {
      parentCount: 0
    }

  }

  handleAddParent() {
    this.setState((prevState) => {
      return {
        parentCount: prevState.parentCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From parent parent count: {this.state.parentCount}</p>
        <button onClick={this.handleAddParent}>+1 from parent</button>
        <Child propFromState={this.state.parentCount} handleAddParent={this.handleAddParent} />
      </div>
    )
  }
};

export default class Child extends React.Component {

  constructor(props) {
    super(props);
    this.handleAddChild = this.handleAddChild.bind(this);

    this.state = {
      childCount: 0
    }

  }

  handleAddChild() {
    this.setState((prevState) => {
      return {
        childCount: prevState.childCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From child parent count: {this.props.propFromState}</p>
        <p>From child child count: {this.state.childCount}</p>
        <button onClick={this.props.handleAddParent}>+1 from child to parent</button>
        <button onClick={this.handleAddChild}>+1 from child to child</button>
      </div>
    )
  }
};

// CBC (Standard) --> CBC (New class property syntax)
export default class Parent extends React.Component {

  constructor(props) {
    super(props);
    this.handleAddParent = this.handleAddParent.bind(this);

    this.state = {
      parentCount: 0
    }

  }

  handleAddParent() {
    this.setState((prevState) => {
      return {
        parentCount: prevState.parentCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From parent parent count: {this.state.parentCount}</p>
        <button onClick={this.handleAddParent}>+1 from parent</button>
        <Child propFromState={this.state.parentCount} handleAddParent={this.handleAddParent} />
      </div>
    )
  }
};

export default class Child extends React.Component {

  state = {
    childCount: 0
  }

  handleAddChild = () => {
    this.setState((prevState) => {
      return {
        childCount: prevState.childCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From child parent count: {this.props.propFromState}</p>
        <p>From child child count: {this.state.childCount}</p>
        <button onClick={this.props.handleAddParent}>+1 from child to parent</button>
        <button onClick={this.handleAddChild}>+1 from child to child</button>
      </div>
    )
  }
};

// CBC (New class property syntax) --> SFC
export default class Parent extends React.Component {

  state = {
    count: 0
  }

  handleAdd = () => {
    this.setState((prevState) => {
      return {
        count: prevState.count += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>In parent: {this.state.count}</p>
        <button onClick={this.handleAdd}>+1</button>
        <Child propFromState={this.state.count} />
      </div>
    )
  }
};

const Child = (props) => (
  <div className="child">
    <p>In child: {props.propFromState}</p>
  </div>
);

// CBC (New class property syntax) --> CBC (New class property syntax)
export default class Parent extends React.Component {

  state = {
    parentCount: 0
  }

  handleAddParent = () => {
    this.setState((prevState) => {
      return {
        parentCount: prevState.parentCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From parent parent count: {this.state.parentCount}</p>
        <button onClick={this.handleAddParent}>+1 from parent</button>
        <Child propFromState={this.state.parentCount} handleAddParent={this.handleAddParent} />
      </div>
    )
  }
};

export default class Child extends React.Component {

  state = {
    childCount: 0
  }

  handleAddChild = () => {
    this.setState((prevState) => {
      return {
        childCount: prevState.childCount += 1
      }
    });
  }

  render() {
    return (
      <div className="parent">
        <p>From child parent count: {this.props.propFromState}</p>
        <p>From child child count: {this.state.childCount}</p>
        <button onClick={this.props.handleAddParent}>+1 from child to parent</button>
        <button onClick={this.handleAddChild}>+1 from child to child</button>
      </div>
    )
  }
};