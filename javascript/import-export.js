////////////////
// Named

// export utils.js
const square = (x) => x * x;
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
export { square, add };

// import utils.js
import { square, add } from './utils.js';


////////////////
// Named - inline

// export utils.js
export const square = (x) => x * x;
export const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

// import utils.js
import { square, add } from './utils.js';


////////////////
// Default

// export utils.js
const square = (x) => x * x;
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
export { square as default };

// import utils.js
import squareDefault from './utils.js';   // Notice name doesn't matter


////////////////
// Default - inline

// export utils.js
const square = (x) => x * x;
const add = (a, b) => a + b;
export default (a, b) => a - b;

// import utils.js
import subtractDefault from './utils.js';   // Notice name doesn't matter


////////////////
// Default and Named together

// export utils.js
const square = (x) => x * x;
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
export { square, add, subract as default };

// import utils.js
import subtract, { square, add } from './utils.js';

