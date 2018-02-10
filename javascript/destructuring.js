
////////////////
// From object

////////////////
// From array

////////////////
// Arguments from functions 

// Do this...
const add = ({a, b}, c) => {
  return a + b;
}

// Instead of this...
const add = (data, c) => {
  return data.a + data.b;
};

console.log(add({a: 1, b: 2}, 1000));
