
# from dotenv import load_dotenv

# import os

# load_dotenv()
# API_KEY = os.getenv("GEMIMI_API_KEY")








import streamlit as st
import random
from datetime import datetime
import uuid


# Quiz data with 67 questions covering specified JavaScript topics
quiz =[
  {
    "question": "What does a try-catch block do in JavaScript?",
    "options": [
      "Handles exceptions gracefully",
      "Repeats code execution",
      "Defines a function",
      "Creates an array"
    ],
    "answer": "Handles exceptions gracefully",
    "difficulty": "Medium",
    "explanation": "A try-catch block catches errors in the try block, allowing the program to continue running."
  },
  {
    "question": "What is logged in: try { undefinedVar; } catch (e) { console.log(e.name); }?",
    "options": [
      "ReferenceError",
      "TypeError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "Accessing an undefined variable throws a ReferenceError, caught and logged by the catch block."
  },
  {
    "question": "What happens if an error occurs outside a try-catch block?",
    "options": [
      "The program stops with an uncaught error",
      "The error is automatically caught",
      "The program continues running",
      "The error is logged to the console"
    ],
    "answer": "The program stops with an uncaught error",
    "difficulty": "Medium",
    "explanation": "Uncaught errors outside a try-catch block halt program execution."
  },
  {
    "question": "What does 'throw new Error('Invalid')' do in a try block?",
    "options": [
      "Triggers the catch block with a custom error",
      "Logs 'Invalid' to the console",
      "Exits the function",
      "Returns 'Invalid'"
    ],
    "answer": "Triggers the catch block with a custom error",
    "difficulty": "Medium",
    "explanation": "'throw new Error()' creates a custom error, caught by the catch block."
  },
  {
    "question": "What is the output of: try { throw 'Test'; } catch (e) { console.log(typeof e); }?",
    "options": [
      "string",
      "object",
      "error",
      "undefined"
    ],
    "answer": "string",
    "difficulty": "Medium",
    "explanation": "Throwing a string value results in 'string' being logged as the type of the caught error."
  },
  {
    "question": "What does the 'finally' block do in try-catch?",
    "options": [
      "Executes regardless of an error",
      "Catches errors",
      "Repeats the try block",
      "Skips the catch block"
    ],
    "answer": "Executes regardless of an error",
    "difficulty": "Medium",
    "explanation": "The 'finally' block runs after try and catch, whether an error occurs or not."
  },
  {
    "question": "What is logged in: try { let x = 1 / 0; } catch (e) { console.log(e.message); }?",
    "options": [
      "Infinity",
      "Division by zero",
      "undefined",
      "No error is thrown"
    ],
    "answer": "No error is thrown",
    "difficulty": "Medium",
    "explanation": "Dividing by zero in JavaScript results in Infinity, not an error, so the catch block is skipped."
  },
  {
    "question": "How do you handle multiple error types in a catch block?",
    "options": [
      "Use if-else to check e.name",
      "Use multiple catch blocks",
      "Use a switch statement",
      "Use a loop"
    ],
    "answer": "Use if-else to check e.name",
    "difficulty": "Medium",
    "explanation": "A single catch block can use if-else to handle different error types based on e.name."
  },
  {
    "question": "What does try { JSON.parse('invalid'); } catch (e) { console.log(e.name); } log?",
    "options": [
      "SyntaxError",
      "ReferenceError",
      "TypeError",
      "ParseError"
    ],
    "answer": "SyntaxError",
    "difficulty": "Medium",
    "explanation": "Invalid JSON in 'JSON.parse()' throws a SyntaxError, logged by the catch block."
  },
  {
    "question": "What is the purpose of a throw statement?",
    "options": [
      "To create and raise a custom error",
      "To exit a loop",
      "To return a value",
      "To log a message"
    ],
    "answer": "To create and raise a custom error",
    "difficulty": "Medium",
    "explanation": "'throw' creates an error that can be caught by a catch block."
  },
  {
    "question": "What is a closure in JavaScript?",
    "options": [
      "A function with access to its outer scope’s variables",
      "A loop that runs indefinitely",
      "A function with no parameters",
      "A variable declared globally"
    ],
    "answer": "A function with access to its outer scope’s variables",
    "difficulty": "Medium",
    "explanation": "A closure is a function that retains access to its lexical scope’s variables even after the outer function finishes."
  },
  {
    "question": "What does this closure do: function outer() { let x = 1; return function() { return x++; }; } let fn = outer(); console.log(fn());?",
    "options": [
      "Logs 1",
      "Logs 2",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 1",
    "difficulty": "Medium",
    "explanation": "The inner function retains access to x, logging 1 and incrementing x to 2 for the next call."
  },
  {
    "question": "What is the output of: let fn = (function() { let count = 0; return function() { return count++; }; })(); console.log(fn(), fn());?",
    "options": [
      "0 1",
      "1 2",
      "0 0",
      "1 1"
    ],
    "answer": "0 1",
    "difficulty": "Medium",
    "explanation": "The closure increments count each call, logging 0 on the first call and 1 on the second."
  },
  {
    "question": "How does a closure maintain variable state?",
    "options": [
      "By retaining the outer function’s scope",
      "By using global variables",
      "By resetting variables each call",
      "By copying variables"
    ],
    "answer": "By retaining the outer function’s scope",
    "difficulty": "Medium",
    "explanation": "Closures preserve the outer function’s variables in memory, allowing state persistence."
  },
  {
    "question": "What is logged by: function makeCounter() { let n = 0; return () => n++; } let counter = makeCounter(); console.log(counter());?",
    "options": [
      "0",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "0",
    "difficulty": "Medium",
    "explanation": "The closure returns n (0) and increments it to 1 for the next call."
  },
  {
    "question": "What is a common use of closures?",
    "options": [
      "Creating private variables",
      "Repeating loops",
      "Defining arrays",
      "Handling events"
    ],
    "answer": "Creating private variables",
    "difficulty": "Medium",
    "explanation": "Closures are often used to encapsulate variables, making them private to the inner function."
  },
  {
    "question": "What does this closure return: function outer(x) { return function(y) { return x + y; }; } let add5 = outer(5); console.log(add5(3));?",
    "options": [
      "8",
      "5",
      "3",
      "15"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "The inner function adds x (5) and y (3), returning 8."
  },
  {
    "question": "What is the output of: let x = 10; function closure() { let x = 20; return function() { return x; }; } console.log(closure()());?",
    "options": [
      "20",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "The inner function accesses the local x (20) from the closure, not the global x (10)."
  },
  {
    "question": "Why are closures useful in event handlers?",
    "options": [
      "They retain access to outer variables",
      "They prevent events from firing",
      "They reset variables",
      "They simplify DOM access"
    ],
    "answer": "They retain access to outer variables",
    "difficulty": "Medium",
    "explanation": "Closures allow event handlers to access variables from their outer scope."
  },
  {
    "question": "What does this closure do: let fn = (function() { let id = 0; return () => id += 2; })(); console.log(fn());?",
    "options": [
      "Logs 2",
      "Logs 0",
      "Logs 1",
      "Throws an error"
    ],
    "answer": "Logs 2",
    "difficulty": "Medium",
    "explanation": "The closure increments id by 2, returning 2 on the first call."
  },
  {
    "question": "What is a callback function in JavaScript?",
    "options": [
      "A function passed as an argument to another function",
      "A function that returns a value",
      "A function that loops",
      "A function that creates an object"
    ],
    "answer": "A function passed as an argument to another function",
    "difficulty": "Medium",
    "explanation": "Callbacks are functions passed to another function to be executed later."
  },
  {
    "question": "What is the output of: function run(cb) { cb(5); } run(x => console.log(x * 2));?",
    "options": [
      "10",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The callback multiplies x (5) by 2, logging 10."
  },
  {
    "question": "What does setTimeout(callback, 1000) do?",
    "options": [
      "Executes callback after 1 second",
      "Repeats callback every 1 second",
      "Delays the entire program",
      "Calls callback immediately"
    ],
    "answer": "Executes callback after 1 second",
    "difficulty": "Medium",
    "explanation": "'setTimeout' schedules the callback to run after a 1000ms delay."
  },
  {
    "question": "What is logged by: function process(arr, cb) { for (let x of arr) cb(x); } process([1, 2], x => console.log(x + 1));?",
    "options": [
      "2 3",
      "1 2",
      "3 4",
      "1 1"
    ],
    "answer": "2 3",
    "difficulty": "Medium",
    "explanation": "The callback adds 1 to each array element, logging 2 and 3."
  },
  {
    "question": "What is a common issue with callbacks?",
    "options": [
      "Callback hell (nested callbacks)",
      "Infinite loops",
      "Variable shadowing",
      "Syntax errors"
    ],
    "answer": "Callback hell (nested callbacks)",
    "difficulty": "Medium",
    "explanation": "Deeply nested callbacks can make code hard to read, known as callback hell."
  },
  {
    "question": "What does this callback do: function asyncOp(cb) { setTimeout(() => cb('done'), 100); } asyncOp(console.log);?",
    "options": [
      "Logs 'done' after 100ms",
      "Logs 'done' immediately",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'done' after 100ms",
    "difficulty": "Medium",
    "explanation": "The callback (console.log) is called with 'done' after a 100ms delay."
  },
  {
    "question": "What is the output of: function callTwice(cb) { cb(); cb(); } callTwice(() => console.log('Hi'));?",
    "options": [
      "Logs 'Hi' twice",
      "Logs 'Hi' once",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'Hi' twice",
    "difficulty": "Medium",
    "explanation": "The callback is executed twice, logging 'Hi' each time."
  },
  {
    "question": "How do you pass data to a callback function?",
    "options": [
      "Pass arguments when calling the callback",
      "Use global variables",
      "Define the callback inside a loop",
      "Use a closure"
    ],
    "answer": "Pass arguments when calling the callback",
    "difficulty": "Medium",
    "explanation": "Callbacks receive data as arguments when invoked by the calling function."
  },
  {
    "question": "What is logged by: let fn = cb => cb(3); fn(x => console.log(x * x));?",
    "options": [
      "9",
      "3",
      "6",
      "undefined"
    ],
    "answer": "9",
    "difficulty": "Medium",
    "explanation": "The callback squares x (3), logging 9."
  },
  {
    "question": "Why are callbacks used in asynchronous operations?",
    "options": [
      "To handle results after the operation completes",
      "To loop through arrays",
      "To define objects",
      "To create closures"
    ],
    "answer": "To handle results after the operation completes",
    "difficulty": "Medium",
    "explanation": "Callbacks allow handling of results or errors after an async operation finishes."
  },
  {
    "question": "What is the syntax for an arrow function with one parameter?",
    "options": [
      "x => x * 2",
      "(x) => { return x * 2; }",
      "function(x) => x * 2",
      "=> x * 2"
    ],
    "answer": "x => x * 2",
    "difficulty": "Medium",
    "explanation": "Arrow functions with one parameter can omit parentheses for concise syntax."
  },
  {
    "question": "What does this arrow function return: let fn = x => x + 1; console.log(fn(5));?",
    "options": [
      "6",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "The arrow function adds 1 to x (5), returning 6."
  },
  {
    "question": "What is the output of: let fn = (x, y) => x * y; console.log(fn(2, 3));?",
    "options": [
      "6",
      "5",
      "23",
      "undefined"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "The arrow function multiplies x (2) and y (3), returning 6."
  },
  {
    "question": "How does an arrow function differ from a regular function in terms of 'this'?",
    "options": [
      "Arrow functions inherit 'this' from their enclosing scope",
      "Arrow functions have their own 'this'",
      "Arrow functions cannot use 'this'",
      "Arrow functions redefine 'this'"
    ],
    "answer": "Arrow functions inherit 'this' from their enclosing scope",
    "difficulty": "Medium",
    "explanation": "Arrow functions do not have their own 'this'; they use the 'this' of their lexical scope."
  },
  {
    "question": "What does this arrow function do: let obj = { value: 10, fn: () => this.value }; console.log(obj.fn());?",
    "options": [
      "Logs undefined",
      "Logs 10",
      "Logs obj",
      "Throws an error"
    ],
    "answer": "Logs undefined",
    "difficulty": "Medium",
    "explanation": "Arrow functions don’t bind 'this' to the object, so 'this.value' is undefined."
  },
  {
    "question": "What is the output of: let double = x => x * 2; console.log(double(4));?",
    "options": [
      "8",
      "4",
      "16",
      "undefined"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "The arrow function doubles x (4), returning 8."
  },
  {
    "question": "Can arrow functions be used as constructors?",
    "options": [
      "No, they cannot be used with 'new'",
      "Yes, like regular functions",
      "Only if they return an object",
      "Only with prototypes"
    ],
    "answer": "No, they cannot be used with 'new'",
    "difficulty": "Medium",
    "explanation": "Arrow functions lack a prototype property and cannot be used as constructors."
  },
  {
    "question": "What does () => ({ x: 1 }) return?",
    "options": [
      "An object { x: 1 }",
      "The value 1",
      "undefined",
      "A function"
    ],
    "answer": "An object { x: 1 }",
    "difficulty": "Medium",
    "explanation": "The arrow function with parentheses around the object returns { x: 1 }."
  },
  {
    "question": "What is the output of: let fn = () => 42; console.log(fn());?",
    "options": [
      "42",
      "undefined",
      "null",
      "Error"
    ],
    "answer": "42",
    "difficulty": "Medium",
    "explanation": "The arrow function implicitly returns 42."
  },
  {
    "question": "Why are arrow functions preferred in callbacks?",
    "options": [
      "They have concise syntax and lexical 'this'",
      "They always return objects",
      "They are faster than regular functions",
      "They create closures automatically"
    ],
    "answer": "They have concise syntax and lexical 'this'",
    "difficulty": "Medium",
    "explanation": "Arrow functions are concise and inherit 'this', making them ideal for callbacks."
  },
  {
    "question": "What does [1, 2, 3].forEach(x => console.log(x * 2)) do?",
    "options": [
      "Logs 2, 4, 6",
      "Logs 1, 2, 3",
      "Returns a new array",
      "Logs nothing"
    ],
    "answer": "Logs 2, 4, 6",
    "difficulty": "Medium",
    "explanation": "'forEach' calls the callback for each element, doubling and logging each value."
  },
  {
    "question": "What is the output of: let sum = 0; [1, 2, 3].forEach(x => sum += x); console.log(sum);?",
    "options": [
      "6",
      "3",
      "0",
      "undefined"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "'forEach' adds each element to sum, resulting in 1 + 2 + 3 = 6."
  },
  {
    "question": "What does forEach return?",
    "options": [
      "undefined",
      "A new array",
      "The last element",
      "The original array"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'forEach' executes a callback for each element and returns undefined."
  },
  {
    "question": "What is logged by: [1, 2].forEach((x, i) => console.log(i, x));?",
    "options": [
      "0 1, 1 2",
      "1 0, 2 1",
      "1 2, 2 1",
      "0 1, 0 2"
    ],
    "answer": "0 1, 1 2",
    "difficulty": "Medium",
    "explanation": "'forEach' provides the index and element, logging index 0 with 1, then index 1 with 2."
  },
  {
    "question": "Can you stop a forEach loop early?",
    "options": [
      "No, forEach cannot be stopped",
      "Yes, with break",
      "Yes, with return",
      "Yes, with continue"
    ],
    "answer": "No, forEach cannot be stopped",
    "difficulty": "Medium",
    "explanation": "'forEach' runs for all elements; 'break' or 'return' cannot stop it."
  },
  {
    "question": "What does ['a', 'b'].forEach((x, i, arr) => arr[i] = x.toUpperCase()) do?",
    "options": [
      "Modifies array to ['A', 'B']",
      "Returns ['A', 'B']",
      "Logs 'A', 'B'",
      "Throws an error"
    ],
    "answer": "Modifies array to ['A', 'B']",
    "difficulty": "Medium",
    "explanation": "'forEach' modifies the original array by setting each element to uppercase."
  },
  {
    "question": "What is logged by: [1, 2, 3].forEach(x => { if (x === 2) return; console.log(x); });?",
    "options": [
      "1 3",
      "1 2 3",
      "2",
      "Nothing"
    ],
    "answer": "1 3",
    "difficulty": "Medium",
    "explanation": "'return' in forEach skips the current iteration, logging only 1 and 3."
  },
  {
    "question": "What does [10, 20].forEach((x, i) => console.log(i + ': ' + x)) log?",
    "options": [
      "0: 10, 1: 20",
      "10: 0, 20: 1",
      "1: 10, 2: 20",
      "10, 20"
    ],
    "answer": "0: 10, 1: 20",
    "difficulty": "Medium",
    "explanation": "'forEach' logs the index and element as a string for each iteration."
  },
  {
    "question": "What is the purpose of forEach compared to a for loop?",
    "options": [
      "More concise for iterating arrays",
      "Faster execution",
      "Returns a new array",
      "Handles errors"
    ],
    "answer": "More concise for iterating arrays",
    "difficulty": "Medium",
    "explanation": "'forEach' provides a cleaner way to iterate over arrays compared to a for loop."
  },
  {
    "question": "What does [1, 2].forEach(() => console.log('test')) log?",
    "options": [
      "test test",
      "test",
      "undefined",
      "Nothing"
    ],
    "answer": "test test",
    "difficulty": "Medium",
    "explanation": "'forEach' runs the callback for each element (2 times), logging 'test' twice."
  },
  {
    "question": "What does [1, 2, 3].map(x => x * 2) return?",
    "options": [
      "[2, 4, 6]",
      "[1, 2, 3]",
      "undefined",
      "Logs 2, 4, 6"
    ],
    "answer": "[2, 4, 6]",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with each element doubled."
  },
  {
    "question": "What is the output of: console.log([1, 2].map((x, i) => i));?",
    "options": [
      "[0, 1]",
      "[1, 2]",
      "[0, 0]",
      "[1, 1]"
    ],
    "answer": "[0, 1]",
    "difficulty": "Medium",
    "explanation": "'map' returns an array of indices (0, 1) for each element."
  },
  {
    "question": "What does ['a', 'b'].map(x => x.toUpperCase()) return?",
    "options": [
      "['A', 'B']",
      "['a', 'b']",
      "undefined",
      "Logs A, B"
    ],
    "answer": "['A', 'B']",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with each string converted to uppercase."
  },
  {
    "question": "What is the output of: [1, 2, 3].map(x => x > 1 ? x : 0);?",
    "options": [
      "[0, 2, 3]",
      "[1, 2, 3]",
      "[0, 0, 0]",
      "[1, 1, 1]"
    ],
    "answer": "[0, 2, 3]",
    "difficulty": "Medium",
    "explanation": "'map' returns 0 for elements <= 1 and the element itself if > 1."
  },
  {
    "question": "What does map do compared to forEach?",
    "options": [
      "Returns a new array, forEach returns undefined",
      "Logs values, forEach modifies arrays",
      "Iterates faster than forEach",
      "Handles errors"
    ],
    "answer": "Returns a new array, forEach returns undefined",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with transformed values, while 'forEach' does not."
  },
  {
    "question": "What is the output of: [1, 2].map((x, i, arr) => arr[i] * 2);?",
    "options": [
      "[2, 4]",
      "[1, 2]",
      "[0, 1]",
      "undefined"
    ],
    "answer": "[2, 4]",
    "difficulty": "Medium",
    "explanation": "'map' doubles each element using the array and index, returning [2, 4]."
  },
  {
    "question": "What does [null, 1].map(x => x || 0) return?",
    "options": [
      "[0, 1]",
      "[null, 1]",
      "[0, 0]",
      "undefined"
    ],
    "answer": "[0, 1]",
    "difficulty": "Medium",
    "explanation": "'map' replaces falsy values (null) with 0, keeping 1 unchanged."
  },
  {
    "question": "What is logged by: console.log([1, 2].map(x => ({ x })));?",
    "options": [
      "[{ x: 1 }, { x: 2 }]",
      "[1, 2]",
      "[{ x: 1 }, { x: 1 }]",
      "undefined"
    ],
    "answer": "[{ x: 1 }, { x: 2 }]",
    "difficulty": "Medium",
    "explanation": "'map' creates objects with property x for each element."
  },
  {
    "question": "What does [1, 2, 3].map(x => x % 2 === 0 ? 'even' : 'odd') return?",
    "options": [
      "['odd', 'even', 'odd']",
      "['even', 'odd', 'even']",
      "[1, 2, 3]",
      "undefined"
    ],
    "answer": "['odd', 'even', 'odd']",
    "difficulty": "Medium",
    "explanation": "'map' labels each number as 'even' or 'odd' based on x % 2."
  },
  {
    "question": "What is the purpose of the map method?",
    "options": [
      "Transform elements into a new array",
      "Iterate without returning",
      "Modify the original array",
      "Filter elements"
    ],
    "answer": "Transform elements into a new array",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with the results of the callback applied to each element."
  },
  {
    "question": "What does [1, 2, 3].find(x => x > 1) return?",
    "options": [
      "2",
      "[2, 3]",
      "1",
      "undefined"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'find' returns the first element where the callback returns true (x > 1)."
  },
  {
    "question": "What is the output of: console.log([1, 2, 3].find((x, i) => i === 1));?",
    "options": [
      "2",
      "1",
      "undefined",
      "0"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'find' returns the element at index 1, which is 2."
  },
  {
    "question": "What does ['apple', 'banana'].find(x => x.includes('an')) return?",
    "options": [
      "banana",
      "apple",
      "undefined",
      "an"
    ],
    "answer": "banana",
    "difficulty": "Medium",
    "explanation": "'find' returns the first string containing 'an', which is 'banana'."
  },
  {
    "question": "What does [1, 2, 3].find(x => x > 5) return?",
    "options": [
      "undefined",
      "null",
      "1",
      "[1, 2, 3]"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'find' returns undefined if no element satisfies the callback."
  },
  {
    "question": "What does [ { id: 1 }, { id: 2 } ].find(obj => obj.id === 2) return?",
    "options": [
      "{ id: 2 }",
      "{ id: 1 }",
      "2",
      "undefined"
    ],
    "answer": "{ id: 2 }",
    "difficulty": "Medium",
    "explanation": "'find' returns the first object where id === 2."
  },
  {
    "question": "What is the output of: console.log([0, 1, 0].find(x => x));?",
    "options": [
      "1",
      "0",
      "undefined",
      "[0, 1, 0]"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "'find' returns the first truthy value, which is 1."
  },
  {
    "question": "What does find return if no element is found?",
    "options": [
      "undefined",
      "null",
      "[]",
      "0"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'find' returns undefined when no element matches the callback."
  },
  {
    "question": "What is logged by: console.log([1, 2, 3].find((x, i, arr) => arr[i] === 2));?",
    "options": [
      "2",
      "1",
      "3",
      "undefined"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'find' returns the element at index where arr[i] === 2."
  },
  {
    "question": "What does ['cat', 'dog'].find(x => x.length > 3) return?",
    "options": [
      "undefined",
      "cat",
      "dog",
      "null"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'find' returns undefined since no string has length > 3."
  },
  {
    "question": "What is the purpose of the find method?",
    "options": [
      "Returns the first element matching a condition",
      "Returns a new array",
      "Modifies the original array",
      "Logs all elements"
    ],
    "answer": "Returns the first element matching a condition",
    "difficulty": "Medium",
    "explanation": "'find' returns the first element where the callback returns true."
  },
  {
    "question": "What is a constructor function in JavaScript?",
    "options": [
      "A function used with 'new' to create objects",
      "A function that loops",
      "A function that returns a string",
      "A function with no parameters"
    ],
    "answer": "A function used with 'new' to create objects",
    "difficulty": "Medium",
    "explanation": "Constructors create and initialize objects when called with 'new'."
  },
  {
    "question": "What does this constructor do: function Car(model) { this.model = model; } let car = new Car('Toyota'); console.log(car.model);?",
    "options": [
      "Logs 'Toyota'",
      "Logs undefined",
      "Logs Car",
      "Throws an error"
    ],
    "answer": "Logs 'Toyota'",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'model' property, accessed as car.model."
  },
  {
    "question": "What is the output of: function User(name) { this.name = name; } let u = new User('Alice'); console.log(u instanceof User);?",
    "options": [
      "true",
      "false",
      "undefined",
      "Error"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "'instanceof' checks if u was created by the User constructor, returning true."
  },
  {
    "question": "How do you add a method to a constructor?",
    "options": [
      "Inside the constructor or via prototype",
      "Using a loop",
      "Using an array",
      "Using a callback"
    ],
    "answer": "Inside the constructor or via prototype",
    "difficulty": "Medium",
    "explanation": "Methods can be defined in the constructor or added to the prototype for shared functionality."
  },
  {
    "question": "What does this do: function Person() { this.age = 30; } Person.prototype.greet = function() { return 'Hi'; }; let p = new Person(); console.log(p.greet());?",
    "options": [
      "Logs 'Hi'",
      "Logs undefined",
      "Logs 30",
      "Throws an error"
    ],
    "answer": "Logs 'Hi'",
    "difficulty": "Medium",
    "explanation": "The greet method on the prototype is inherited by p, logging 'Hi'."
  },
  {
    "question": "What is the output of: function Item(id) { this.id = id; } let item = new Item(1); console.log(item.id);?",
    "options": [
      "1",
      "undefined",
      "Item",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'id' property, accessed as item.id."
  },
  {
    "question": "What does 'new' do when calling a constructor?",
    "options": [
      "Creates a new object and sets its prototype",
      "Calls the function without an object",
      "Returns a string",
      "Loops through properties"
    ],
    "answer": "Creates a new object and sets its prototype",
    "difficulty": "Medium",
    "explanation": "'new' creates an object, sets its prototype, and binds 'this' to it."
  },
  {
    "question": "What is logged by: function Test() { this.x = 5; } Test.prototype.x = 10; let t = new Test(); console.log(t.x);?",
    "options": [
      "5",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The constructor’s property (x = 5) overrides the prototype’s property (x = 10)."
  },
  {
    "question": "What does this constructor do: function Book(title) { this.title = title; this.getTitle = () => this.title; } let b = new Book('JS'); console.log(b.getTitle());?",
    "options": [
      "Logs 'JS'",
      "Logs undefined",
      "Logs Book",
      "Throws an error"
    ],
    "answer": "Logs 'JS'",
    "difficulty": "Medium",
    "explanation": "The arrow function in the constructor returns the title property."
  },
  {
    "question": "Why add methods to a constructor’s prototype?",
    "options": [
      "To share methods across instances",
      "To make methods private",
      "To loop through instances",
      "To create closures"
    ],
    "answer": "To share methods across instances",
    "difficulty": "Medium",
    "explanation": "Prototype methods are shared, saving memory compared to instance methods."
  },
  {
    "question": "What does let { name, age } = { name: 'Alice', age: 25 }; console.log(name); do?",
    "options": [
      "Logs 'Alice'",
      "Logs undefined",
      "Logs { name: 'Alice' }",
      "Throws an error"
    ],
    "answer": "Logs 'Alice'",
    "difficulty": "Medium",
    "explanation": "Object destructuring assigns the 'name' property to a variable named 'name'."
  },
  {
    "question": "What is the output of: let [a, b] = [1, 2]; console.log(a + b);?",
    "options": [
      "3",
      "12",
      "undefined",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "Array destructuring assigns 1 to a and 2 to b, so a + b = 3."
  },
  {
    "question": "What does let { x = 10 } = { }; console.log(x); do?",
    "options": [
      "Logs 10",
      "Logs undefined",
      "Logs null",
      "Throws an error"
    ],
    "answer": "Logs 10",
    "difficulty": "Medium",
    "explanation": "Destructuring with a default value assigns 10 to x when the property is undefined."
  },
  {
    "question": "What is the output of: let [x, ...rest] = [1, 2, 3]; console.log(rest);?",
    "options": [
      "[2, 3]",
      "[1, 2, 3]",
      "2",
      "undefined"
    ],
    "answer": "[2, 3]",
    "difficulty": "Medium",
    "explanation": "The rest operator in destructuring collects remaining elements into an array."
  },
  {
    "question": "What does function fn({ name }) { console.log(name); } do when called with fn({ name: 'Bob' });?",
    "options": [
      "Logs 'Bob'",
      "Logs undefined",
      "Logs { name: 'Bob' }",
      "Throws an error"
    ],
    "answer": "Logs 'Bob'",
    "difficulty": "Medium",
    "explanation": "Destructuring in the parameter extracts the 'name' property, logging 'Bob'."
  },
  {
    "question": "What does let x = true ? 'yes' : 'no'; console.log(x); do?",
    "options": [
      "Logs 'yes'",
      "Logs 'no'",
      "Logs true",
      "Throws an error"
    ],
    "answer": "Logs 'yes'",
    "difficulty": "Medium",
    "explanation": "The ternary operator returns 'yes' if true, so x is 'yes'."
  },
  {
    "question": "What is the output of: console.log(5 > 3 ? 'greater' : 'less');?",
    "options": [
      "greater",
      "less",
      "true",
      "undefined"
    ],
    "answer": "greater",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates 5 > 3 as true, returning 'greater'."
  },
  {
    "question": "What does let result = x => x % 2 === 0 ? 'even' : 'odd'; console.log(result(4)); do?",
    "options": [
      "Logs 'even'",
      "Logs 'odd'",
      "Logs 4",
      "Throws an error"
    ],
    "answer": "Logs 'even'",
    "difficulty": "Medium",
    "explanation": "The ternary operator checks if 4 is even, returning 'even'."
  },
  {
    "question": "What does [...[1, 2], 3] return?",
    "options": [
      "[1, 2, 3]",
      "[1, 2]",
      "[3, 1, 2]",
      "undefined"
    ],
    "answer": "[1, 2, 3]",
    "difficulty": "Medium",
    "explanation": "The spread operator flattens [1, 2] and adds 3, creating [1, 2, 3]."
  },
  {
    "question": "What is the output of: let a = [1, 2]; let b = [...a, 3]; console.log(b);?",
    "options": [
      "[1, 2, 3]",
      "[1, 2]",
      "[3, 1, 2]",
      "[1, 2, [3]]"
    ],
    "answer": "[1, 2, 3]",
    "difficulty": "Medium",
    "explanation": "The spread operator copies a’s elements and adds 3, resulting in [1, 2, 3]."
  }
]
# Cache shuffled quiz (removed for testing, re-add if needed)
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

# Initialize session state
if "quiz_data" not in st.session_state:
    if not quiz:
        st.error("Quiz list is empty!")
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz) if quiz else [],
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "started": False,
        "max_streak": 0
    })
    st.write(f"Initialized quiz with {len(st.session_state.quiz_data)} questions")

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)  # 60 minutes
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,  # 60 minutes
        "streak": 0,
        "max_streak": 0,
        "started": False
    })
    st.rerun()

# CSS for enhanced UI
st.markdown("""
<style>
body {
    background: var(--bg-gradient);
    color: var(--text-color);
    font-family: 'Inter', 'Arial', sans-serif;
    transition: all 0.3s ease;
}
:root {
    --bg-gradient: linear-gradient(180deg, #1a1a3b, #2c2c54);
    --bg-container: #2c2c54;
    --text-color: #ffffff;
    --button-bg: linear-gradient(45deg, #6b21a8, #a855f7);
    --button-hover: linear-gradient(45deg, #8b5cf6, #c084fc);
    --code-bg: #1e1e1e;
    --shadow: rgba(0,0,0,0.3);
}
[data-theme="light"] {
    --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
    --bg-container: #ffffff;
    --text-color: #1f2937;
    --button-bg: linear-gradient(45deg, #4f46e5, #7c3aed);
    --button-hover: linear-gradient(45deg, #6366f1, #a78bfa);
    --code-bg: #f1f5f9;
    --shadow: rgba(0,0,0,0.1);
}
.main-container {
    background: var(--bg-container);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 8px 25px var(--shadow);
    max-width: 900px;
    margin: 20px auto;
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 10px;
    padding: 12px;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
    margin: 6px 0;
    cursor: pointer;
    transition: all 0.3s ease;
    transform: scale(1);
}
.stButton>button:hover {
    background: var(--button-hover);
    transform: scale(1.05);
    box-shadow: 0 4px 12px var(--shadow);
}
.stButton>button:disabled {
    background: #6b7280;
    cursor: not-allowed;
    transform: scale(1);
}
.selected-correct {
    background: #34c759 !important;
    transform: scale(1.05);
}
.selected-wrong {
    background: #ff3b30 !important;
    transform: scale(1.05);
}
.question-container {
    background: var(--bg-container);
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 12px var(--shadow);
    margin-bottom: 15px;
}
.feedback-correct {
    color: #34c759;
    font-weight: 600;
    font-size: 18px;
    margin: 15px 0;
    animation: fadeIn 0.5s ease;
}
.feedback-wrong {
    color: #ff3b30;
    font-weight: 600;
    font-size: 18px;
    margin: 15px 0;
    animation: fadeIn 0.5s ease;
}
.progress-bar {
    background: #4b4b6b;
    border-radius: 10px;
    height: 12px;
    margin: 10px 0;
    position: relative;
}
.progress-fill {
    background: var(--button-bg);
    height: 100%;
    border-radius: 10px;
    transition: width 0.5s ease;
}
.progress-text {
    position: absolute;
    top: -20px;
    right: 0;
    color: var(--text-color);
    font-size: 12px;
}
.title {
    font-size: 36px;
    text-align: center;
    margin-bottom: 8px;
    color: var(--text-color);
}
.caption {
    text-align: center;
    color: #b0b0d0;
    font-size: 16px;
    margin-bottom: 20px;
}
.timer {
    font-size: 16px;
    color: #ff6b6b;
    font-weight: 600;
    text-align: center;
    margin-top: 10px;
}
.difficulty {
    font-size: 14px;
    color: #b0b0d0;
    margin-bottom: 10px;
}
.stCodeBlock {
    background-color: var(--code-bg) !important;
    border-radius: 8px;
    padding: 15px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 14px;
    line-height: 1.5;
    border: 1px solid #4b4b6b;
}
.stCodeBlock pre, .stCodeBlock code {
    color: var(--text-color);
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@media (max-width: 600px) {
    .main-container {
        padding: 15px;
        margin: 10px;
    }
    .title {
        font-size: 28px;
    }
    .stButton>button {
        font-size: 14px;
        padding: 8px;
    }
}
</style>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Expertise!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 67 comprehensive questions!</p>
        <p style="color: #b0b0d0;">60 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.write(f"Quiz started with {len(st.session_state.quiz_data)} questions")
        st.rerun()
else:
    # Timer
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = int(progress * 100)
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 13px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code
                if "```javascript" in q["question"]:
                    question_parts = q["question"].split("```javascript\n")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language="javascript")
                else:
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{q['question']}**")

                # Option buttons
                for i, option in enumerate(q["display_options"]):
                    button_class = ""
                    if st.session_state.selected_option == option:
                        button_class = "selected-correct" if option == q["labeled_answer"] else "selected-wrong"
                    if st.button(
                        option,
                        key=f"q{i}_{st.session_state.current_q}",
                        disabled=st.session_state.selected_option is not None
                    ):
                        is_correct = option == q["labeled_answer"]
                        st.session_state.selected_option = option
                        st.session_state.feedback = {
                            "is_correct": is_correct,
                            "correct_answer": q["labeled_answer"],
                            "explanation": q["explanation"]
                        }
                        st.session_state.answers[st.session_state.current_q] = {
                            "question": q["question"],
                            "user_answer": option,
                            "correct_answer": q["labeled_answer"],
                            "is_correct": is_correct,
                            "difficulty": q["difficulty"]
                        }
                        if is_correct:
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        # Move to next question or show results
                        if st.session_state.current_q < len(st.session_state.quiz_data) - 1:
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                        else:
                            st.session_state.show_results = True
                        st.rerun()

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)  # 60 minutes
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 15px;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.max_streak}
            </div>
            """, unsafe_allow_html=True)

            # Confetti for high score
            if accuracy > 80:
                st.markdown("""
                <script>
                    confetti({
                        particleCount: 100,
                        spread: 70,
                        origin: { y: 0.6 }
                    });
                </script>
                """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 10px;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


















