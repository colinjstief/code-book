import 'babel-core/polyfill'; // so I can use Promises
import fetch from 'isomorphic-fetch'; // so I can use fetch()

function doSomething() {
  return dispatch =>
    fetch(
      '/api/something'
    ).then(
      response => response.json()
      ).then(
      json => dispatch({ type: DO_SOMETHING, json }),
      err => dispatch({ type: SOMETHING_FAILED, err })
      );
}

function doSomethingElse() {
  return dispatch =>
    fetch(
      '/api/something'
    ).then(
      response => response.json()
      ).then(
      json => dispatch({ type: DO_SOMETHING_ELSE, json }),
      err => dispatch({ type: SOMETHING_ELSE_FAILED, err })
      );
}

// Note how I make it a point to return a Promise at the very end by keeping the chain as 
// return value of the function inside thunk action creators. This lets me do that:

store.dispatch(doSomething()).then(() => {
  console.log('I did something');
});

// When you use Redux Thunk, dispatch returns the return value of the function you returned 
// from the thunk action creator—in this case, the Promise.
// This lets you use combinators like Promise.all() to wait for completion of several actions:

Promise.all([
  store.dispatch(doSomething()),
  store.dispatch(doSomethingElse())
]).then(() => {
  console.log('I did everything!');
});

// However it is preferable to define another action creator that would act as a composition of 
// the previous action creators, and use Promise.all internally:

function doEverything() {
  return dispatch => Promise.all([
    dispatch(doSomething()),
    dispatch(doSomethingElse())
  ]);
}

// Now you can just write

store.dispatch(doEverything()).then(() => {
  console.log('I did everything!');
});