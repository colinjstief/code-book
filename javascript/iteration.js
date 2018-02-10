////////////////
// Over object

// for-of
var obj = {
    a: 1,
    b: 2,
    c: 3
  };
  
  for (var prop in obj) {
    console.log(
      `obj.${prop} = ${obj[prop]}`
    );
  }
  
  // Output:
  // "obj.a = 1"
  // "obj.b = 2"
  // "obj.c = 3"


////////////////
// Over string

  for (var char of 'Hello') {
    console.log(char);
  }
  
  // output:
  // H
  // e
  // l
  // l
  // o
  

////////////////
// Over array

// Order is not necessarily maintainted
// 'value' is a string, not an integer, like you would expect 'i' to be in a loop

let list = [8, 3, 11, 9, 6];

for (let value of list) {
  console.log(value);
}

// Output:
// 8
// 3
// 11
// 9
// 6