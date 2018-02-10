// I/O is short for input output. This is the communication of things. Writing to a database in a form of i/o
// node uses an event driven non-blocking i/o model

// Call stack     --> Data structure that keeps track of program execution. 
//                    It can (1) place an item on top and (2) remove the top item
//                    Starts with main(), the wrapper function that node wraps around your program
// 
// Node APIs      --> Stores registered callback functions
//                    Passes them to the Callback queue when it is time to do so
//
// Callback queue --> Stores callback functions that are ready to fire
//                    Passes them to the Call stack when the Call stack is empty
//
// Event loop     --> Checks the Call stack to see if it is empty, 
//                    then checks the Callback queue to see if there are callbacks waiting


////////////////       ////////////////
// Call stack //       // Node APIs  //
//------------//       //------------//
//            //  -->  //            // 
//            //       //            //
////////////////       ///////////////

// Event loop //              |
//     <-     //              |
//    |  ^    //              |
//    v  |    //              |
//     ->     //              |
////////////////              v

/////////// Callback queue ////////////
//                                   //
//                                   //
///////////////////////////////////////



console.log('Starting');

setTimeout(() => {
    console.log('Inside 2 second callback');
}, 2000);
// Registered in Node API

setTimeout(() => {
    console.log('Inside 0 second callback');
}, 0);
// But this fires after the last console.log
// In fact, it gets placed in the callback queue, which starts when the current sync script finishes

console.log('Finishing');