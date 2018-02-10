////////////////
// Array spread operator

// Return a new array with old items and new ones
const itemsA = ['hat', 'spoon', 'car'];
const itemsB = [...itemsA, 'lamp'];
const itemsC = ['flower', ...itemsB, 'surfboard'];


////////////////
// Object spread operator

// Return a new object with old properties and new ones
const userA = {
  name: 'Colin',
  age: 30
};

const userB = {
  ...userA,
  'age': 29,
  'height': 65
}