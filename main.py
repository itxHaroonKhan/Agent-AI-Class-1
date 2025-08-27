
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
      "Catches and handles errors",
      "Loops through code",
      "Defines a function",
      "Creates an array"
    ],
    "answer": "Catches and handles errors",
    "difficulty": "Medium",
    "explanation": "A try-catch block executes code in the try block and catches any errors in the catch block for handling."
  },
  {
    "question": "What is logged in: try { let x = y; } catch (e) { console.log(e.name); }?",
    "options": [
      "ReferenceError",
      "TypeError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "Accessing an undefined variable 'y' throws a ReferenceError, which is caught and logged."
  },
  {
    "question": "What happens if no error occurs in a try block?",
    "options": [
      "The catch block is skipped",
      "The catch block executes",
      "The code throws an error",
      "The try block loops"
    ],
    "answer": "The catch block is skipped",
    "difficulty": "Medium",
    "explanation": "If no error occurs in the try block, the catch block is not executed."
  },
  {
    "question": "What does 'throw new Error('Invalid')' do in a try-catch block?",
    "options": [
      "Throws a custom error",
      "Logs a message",
      "Skips the catch block",
      "Returns a value"
    ],
    "answer": "Throws a custom error",
    "difficulty": "Medium",
    "explanation": "'throw new Error()' creates a custom error that can be caught by the catch block."
  },
  {
    "question": "What is the output of: try { throw 'Test'; } catch (e) { console.log(typeof e); }?",
    "options": [
      "string",
      "object",
      "undefined",
      "error"
    ],
    "answer": "string",
    "difficulty": "Medium",
    "explanation": "Throwing a string 'Test' results in the catch block receiving it as a string type."
  },
  {
    "question": "How do you handle multiple error types in a catch block?",
    "options": [
      "Check e instanceof ErrorType",
      "Use multiple catch blocks",
      "Use try-catch-else",
      "Use throw multiple times"
    ],
    "answer": "Check e instanceof ErrorType",
    "difficulty": "Medium",
    "explanation": "Use 'instanceof' to check the error type within a single catch block."
  },
  {
    "question": "What does a finally block do in try-catch?",
    "options": [
      "Executes regardless of error",
      "Catches errors",
      "Throws an error",
      "Skips the catch block"
    ],
    "answer": "Executes regardless of error",
    "difficulty": "Medium",
    "explanation": "The finally block runs after try and catch, whether an error occurs or not."
  },
  {
    "question": "What is a closure in JavaScript?",
    "options": [
      "A function with access to its outer scope",
      "A loop that closes a block",
      "An object with methods",
      "A variable declaration"
    ],
    "answer": "A function with access to its outer scope",
    "difficulty": "Medium",
    "explanation": "A closure is a function that retains access to its outer scope’s variables even after the outer function finishes."
  },
  {
    "question": "What is logged in: function outer() { let x = 1; return function inner() { return x; }; } let fn = outer(); console.log(fn());?",
    "options": [
      "1",
      "undefined",
      "null",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The inner function retains access to x via closure, returning 1 when called."
  },
  {
    "question": "How does a closure maintain variable state?",
    "options": [
      "By referencing outer scope variables",
      "By creating a global variable",
      "By using an array",
      "By resetting the variable"
    ],
    "answer": "By referencing outer scope variables",
    "difficulty": "Medium",
    "explanation": "Closures maintain state by keeping outer scope variables in memory."
  },
  {
    "question": "What is the output of: function counter() { let count = 0; return () => count++; } let c = counter(); console.log(c()); c(); console.log(c());?",
    "options": [
      "0, 2",
      "0, 1",
      "1, 2",
      "undefined, undefined"
    ],
    "answer": "0, 2",
    "difficulty": "Medium",
    "explanation": "The closure increments count, logging 0 on the first call and 2 on the third call after incrementing twice."
  },
  {
    "question": "What is a practical use of closures?",
    "options": [
      "Creating private variables",
      "Looping through arrays",
      "Defining global functions",
      "Handling errors"
    ],
    "answer": "Creating private variables",
    "difficulty": "Medium",
    "explanation": "Closures allow data encapsulation by keeping variables private within a function’s scope."
  },
  {
    "question": "What is the output of: let x = 10; function outer() { let x = 20; return () => x; } let fn = outer(); console.log(fn());?",
    "options": [
      "20",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "The inner function’s closure captures the local x (20), not the global x (10)."
  },
  {
    "question": "How do closures help in event handlers?",
    "options": [
      "By preserving loop variables",
      "By creating arrays",
      "By throwing errors",
      "By resetting variables"
    ],
    "answer": "By preserving loop variables",
    "difficulty": "Medium",
    "explanation": "Closures ensure variables in loops (e.g., index) are correctly captured in event handlers."
  },
  {
    "question": "What is a callback function in JavaScript?",
    "options": [
      "A function passed as an argument",
      "A function that loops",
      "A function that throws errors",
      "A function that creates objects"
    ],
    "answer": "A function passed as an argument",
    "difficulty": "Medium",
    "explanation": "A callback is a function passed to another function to be executed later."
  },
  {
    "question": "What is the output of: function run(cb) { cb(5); } run(x => console.log(x));?",
    "options": [
      "5",
      "undefined",
      "null",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The callback function logs the argument 5 passed to it by the run function."
  },
  {
    "question": "What is a common use of callbacks?",
    "options": [
      "Handling asynchronous operations",
      "Creating closures",
      "Defining constructors",
      "Looping arrays"
    ],
    "answer": "Handling asynchronous operations",
    "difficulty": "Medium",
    "explanation": "Callbacks are often used to handle asynchronous tasks, like API calls or timers."
  },
  {
    "question": "What does setTimeout(() => console.log('Hi'), 1000) do?",
    "options": [
      "Logs 'Hi' after 1 second",
      "Logs 'Hi' immediately",
      "Throws an error",
      "Creates a loop"
    ],
    "answer": "Logs 'Hi' after 1 second",
    "difficulty": "Medium",
    "explanation": "setTimeout executes the callback function after a 1000ms delay."
  },
  {
    "question": "What is the output of: function greet(name, cb) { cb('Hello ' + name); } greet('Alice', msg => console.log(msg));?",
    "options": [
      "Hello Alice",
      "Alice",
      "undefined",
      "Error"
    ],
    "answer": "Hello Alice",
    "difficulty": "Medium",
    "explanation": "The callback receives 'Hello Alice' and logs it."
  },
  {
    "question": "How do you pass multiple arguments to a callback?",
    "options": [
      "Call cb(arg1, arg2)",
      "Use cb([arg1, arg2])",
      "Use cb({arg1, arg2})",
      "Use cb(arg1 + arg2)"
    ],
    "answer": "Call cb(arg1, arg2)",
    "difficulty": "Medium",
    "explanation": "Callbacks can accept multiple arguments directly when called."
  },
  {
    "question": "What is a drawback of deeply nested callbacks?",
    "options": [
      "Callback hell",
      "Infinite loops",
      "Variable shadowing",
      "Memory leaks"
    ],
    "answer": "Callback hell",
    "difficulty": "Medium",
    "explanation": "Deeply nested callbacks create complex, hard-to-read code known as callback hell."
  },
  {
    "question": "What is the syntax for an arrow function with one parameter?",
    "options": [
      "x => x * 2",
      "function(x) => x * 2",
      "(x) => { return x * 2 }",
      "=> x { x * 2 }"
    ],
    "answer": "x => x * 2",
    "difficulty": "Medium",
    "explanation": "Arrow functions with one parameter omit parentheses and can use implicit return."
  },
  {
    "question": "What does const double = x => x * 2; console.log(double(5)); output?",
    "options": [
      "10",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The arrow function doubles the input, so double(5) returns 10."
  },
  {
    "question": "How does 'this' behave in an arrow function?",
    "options": [
      "Lexically bound to outer scope",
      "Bound to the caller",
      "Always undefined",
      "Bound to the function"
    ],
    "answer": "Lexically bound to outer scope",
    "difficulty": "Medium",
    "explanation": "Arrow functions inherit 'this' from their enclosing scope, unlike regular functions."
  },
  {
    "question": "What is the output of: const obj = { x: 1, fn: () => this.x }; console.log(obj.fn());?",
    "options": [
      "undefined",
      "1",
      "Error",
      "null"
    ],
    "answer": "undefined",
    " difficulty": "Medium",
    "explanation": "Arrow functions don’t bind their own 'this', so 'this.x' refers to the outer scope, likely undefined."
  },
  {
    "question": "What does () => {} represent?",
    "options": [
      "An arrow function with no parameters",
      "A regular function",
      "An object literal",
      "A closure"
    ],
    "answer": "An arrow function with no parameters",
    "difficulty": "Medium",
    "explanation": "The syntax () => {} defines an arrow function with no parameters."
  },
  {
    "question": "How do you write an arrow function with multiple statements?",
    "options": [
      "(x) => { let y = x * 2; return y; }",
      "x => x * 2; return x;",
      "(x) => x * 2",
      "(x) => { x * 2 }"
    ],
    "answer": "(x) => { let y = x * 2; return y; }",
    "difficulty": "Medium",
    "explanation": "Multiple statements require curly braces and an explicit return."
  },
  {
    "question": "What is the benefit of arrow functions in callbacks?",
    "options": [
      "Concise syntax and lexical 'this'",
      "Automatic error handling",
      "Global variable access",
      "Loop creation"
    ],
    "answer": "Concise syntax and lexical 'this'",
    "difficulty": "Medium",
    "explanation": "Arrow functions offer shorter syntax and inherit 'this' from the outer scope."
  },
  {
    "question": "What does [1, 2, 3].forEach(x => console.log(x)) do?",
    "options": [
      "Logs 1, 2, 3",
      "Logs [1, 2, 3]",
      "Returns a new array",
      "Throws an error"
    ],
    "answer": "Logs 1, 2, 3",
    "difficulty": "Medium",
    "explanation": "'forEach' calls the callback for each element, logging 1, 2, 3."
  },
  {
    "question": "What is the output of: let arr = [1, 2, 3]; let sum = 0; arr.forEach(x => sum += x); console.log(sum);?",
    "options": [
      "6",
      "0",
1, 2, 3",
      "undefined"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "'forEach' iterates over the array, adding each element to sum, resulting in 6."
  },
  {
    "question": "What does forEach return?",
    "options": [
      "undefined",
      "A new array",
      "The last element",
      "The sum of elements"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'forEach' performs an action for each element but returns undefined."
  },
  {
    "question": "How do you access the index in a forEach loop?",
    "options": [
      "arr.forEach((item, index) => ...)",
      "arr.forEach(item, i => ...)",
      "arr.forEach(item => index)",
      "arr.forEach((item) => item.index)"
    ]
    "answer": "arr.forEach((item, index) => ...)",
    "difficulty": "Medium",
    "explanation": "The forEach callback accepts an optional second parameter for the index."
  },
  {
    "question": "What does [1, 2, 3].forEach((x, i) => console.log(i)) output?",
    "options": [
      "0 1 2",
      "1 2 3",
      "undefined",
      "Error"
    ],
    "answer": "0 1 2",
    "difficulty": "Medium",
    "explanation": "The forEach callback logs the index of each element: 0, 1, 2."
  },
  {
    "question": "What does arr.forEach break do?",
    "options": [
      "Cannot break; use a for loop",
      "Exits the forEach loop",
      "Skips to the next iteration",
      "Throws an error"
    ],
    "answer": "Cannot break; use a for loop",
    "difficulty": "Medium",
    "explanation": "'forEach' cannot be exited with break; use a traditional for loop instead."
  },
  {
    "question": "What does [1, 2, 3].forEach(x闻言, 'x => x * 2', x => console.log(x)) output?",
    "options": [
      "Logs 2 4 6",
      "Logs 1 2 3",
      "Logs 1 4 9",
      "Logs nothing"
    ],
    "answer": "Logs 2 4 6",
    "difficulty": "Medium",
    "explanation": "The forEach callback multiplies each element by 2, logging 2, 4, 6."
  },
  {
    "question": "What does [1, 2, 3].map(x => x * 2) return?",
    "options": [
      "[2, 4, 6]",
      "[1, 2, 3]",
      "undefined",
      "[1, 4, 9]"
    ],
    "answer": "[2, 4, 6]",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with each element transformed by the callback, doubling each value."
  },
  {
    "question": "What is the output of: console.log([1, 2, 3].map(x => x + 1));?",
    "options": [
      "[2, 3, 4]",
      "[1, 2, 3]",
      "[1, 4, 9]",
      "undefined"
    ],
    "answer": "[2, 3, 4]",
    "difficulty": "Medium",
    "explanation": "'map' applies the callback to each element, adding 1 to produce a new array."
  },
  {
    "question": "What does [1, 2, 3].map((x, i) => x + i) return?",
    "options": [
      "[1, 3, 5]",
      "[1, 2, 3]",
      "[2, 4, 6]",
      "[0, 2, 4]"
    ],
    "answer": "[1, 3, 5]",
    "difficulty": "Medium",
    "explanation": "'map' adds the index i to each element x, resulting in [1+0, 2+1, 3+2]."
  },
  {
    "question": "What is the difference between map and forEach?",
    "options": [
      "map returns a new array; forEach returns undefined",
      "map modifies the original array; forEach doesn’t",
      "map is synchronous; forEach is asynchronous",
      "map uses closures; forEach doesn’t"
    ],
    "answer": "map returns a new array; forEach returns undefined",
    "difficulty": "Medium",
    "explanation": "'map' creates a new array with transformed elements, while 'forEach' performs actions without returning."
  },
  {
    "question": "What does [1, 2, 3].map(x => String(x)) return?",
    "options": [
      "['1', '2', '3']",
      "[1, 2, 3]",
      "['1, 2, 3']",
      "undefined"
    ],
    "answer": "['1', '2', '3']",
    "difficulty": "Medium",
    "explanation": "'map' converts each number to a string, producing a new array of strings."
  },
  {
    "question": "What does [1, 2, 3].map((x, i, arr) => arr[i] * 2) return?",
    "options": [
      "[2, 4, 6]",
      "[1, 2, 3]",
      "[1, 4, 9]",
      "undefined"
    ],
    "answer": "[2, 4, 6]",
    "difficulty": "Medium",
    "explanation": "'map' uses the array’s elements via arr[i], doubling each to produce a new array."
 nursing
    "question": "What does [1, 2, 3].find(x => x > 1) return?",
    "options": [
      "2",
      "1",
      "[2, 3]",
      "undefined"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'find' returns the first element that satisfies the condition, which is 2."
  },
  {
    "question": "What does [1, 2, 3].find((x, i) => i === 1) return?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    " difficulty": "Medium",
    "explanation": "'find' returns the element at index 1, which is 2."
  },
  {
    "question": "What happens if [1, 2, 3].find(x => x > 3) finds no match?",
    "options": [
      "Returns undefined",
      "Returns null",
      "Throws an error",
      "Returns an empty array"
    ],
    "answer": "Returns undefined",
    "difficulty": "Medium",
    "explanation": "'find' returns undefined if no element satisfies the condition."
  },
  {
    "question": "What does [1, 2, 3].find(x => x % 2 === 0) return?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'find' returns the first even number, which is 2."
  },
  {
    "question": "What does [1, 2, 3].find((x, i, arr) => arr[i] === 3) return?",
    "options": [
      "3",
      "2",
      "undefined",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "'find' returns the element where arr[i] === 3, which is 3."
  },
  {
    "question": "What does function Person(name) { this.name = name; } let p = new Person('Bob'); console.log(p.name); output?",
    "options": [
      "Bob",
      "Person",
      "undefined",
      "Error"
    ],
    "answer": "Bob",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'name' property, which is accessed as p.name."
  },
  {
    "question": "What is the purpose of a constructor function?",
    "options": [
      "To create and initialize objects",
      "To loop through arrays",
      "To handle errors",
      "To define callbacks"
    ],
    "answer": "To create and initialize objects",
    "difficulty": "Medium",
    "explanation": "Constructors are functions used with 'new' to create and initialize objects."
  },
  {
    "question": "What does new Constructor() return?",
    "options": [
      "A new object",
      "undefined",
      "null",
      "The constructor function"
    ],
    "answer": "A new object",
    "difficulty": "Medium",
    "explanation": "The 'new' keyword creates a new object instance of the constructor."
  },
  {
    "question": "What is the output of: function Car(model) { this.model = model; } let c = new Car('Toyota'); console.log(c.model);?",
    "options": [
      "Toyota",
      "Car",
      "undefined",
      "Error"
    ],
    "answer": "Toyota",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'model' property, which is accessed as c.model."
  },
  {
    "question": "How do you add a method to a constructor’s prototype?",
    "options": [
      "Constructor.prototype.method = function() {}",
      "Constructor.method = function() {}",
      "Constructor.addMethod(function() {})",
      "Constructor.setMethod(function() {})"
    ],
    "answer": "Constructor.prototype.method = function() {}",
    "difficulty": "Medium",
    "explanation": "Methods added to the prototype are shared by all instances of the constructor."
  },
  {
    "question": "What does function X() { this.y = 1; } X.prototype.z = 2; let x = new X(); console.log(x.z); output?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "The prototype property z is inherited by the instance x, so x.z returns 2."
  },
  {
    "question": "What does const { name } = { name: 'Alice', age: 25 }; console.log(name); output?",
    "options": [
      "Alice",
      "25",
      "undefined",
      "Error"
    ],
    "answer": "Alice",
    "difficulty": "Medium",
    "explanation": "Destructuring extracts the 'name' property into a variable named name."
  },
  {
    "question": "What does const [a, b] = [1, 2, 3]; console.log(a, b); output?",
    "options": [
      "1 2",
      "1 2 3",
      "undefined undefined",
      "Error"
    ],
    "answer": "1 2",
    "difficulty": "Medium",
    "explanation": "Array destructuring assigns the first two elements to a and b."
  },
  {
    "question": "What does function fn({x, y}) { return x + y; } console.log(fn({x: 1, y: 2})); output?",
    "options": [
      "3",
      "1 2",
      "undefined",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "Object destructuring in the parameter list extracts x and y, returning their sum."
  },
  {
    "question": "What does const [x, ...rest] = [1, 2, 3]; console.log(rest); output?",
    "options": [
      "[2, 3]",
      "[1, 2, 3]",
      "[1]",
      "undefined"
    ],
    "answer": "[2, 3]",
    "difficulty": "Medium",
    "explanation": "The rest parameter collects remaining elements into an array after x."
  },
  {
    "question": "What does const { x = 10 } = {}; console.log(x); output?",
    "options": [
      "10",
      "undefined",
      "null",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "Destructuring with a default value assigns 10 to x if the property is undefined."
  },
  {
    "question": "What does const [a, b = 5] = [1]; console.log(b); output?",
    "options": [
      "5",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "Array destructuring assigns the default value 5 to b if no value is provided."
  },
  {
    "question": "What does const x = 2; console.log(x > 1 ? 'Yes' : 'No'); output?",
    "options": [
      "Yes",
      "No",
      "undefined",
      "Error"
    ],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "The ternary operator returns 'Yes' if x > 1 is true, else 'No'."
  },
  {
    "question": "What does const result = x => x % 2 === 0 ? 'Even' : 'Odd'; console.log(result(3)); output?",
    "options": [
      "Odd",
      "Even",
      "undefined",
      "Error"
    ],
    "answer": "Odd",
    "difficulty": "Medium",
    "explanation": "The ternary operator checks if 3 is even, returning 'Odd'."
  },
  {
    "question": "What does const x = 0; console.log(x ? 'True' : 'False'); output?",
    "options": [
      "False",
      "True",
      "0",
      "undefined"
    ],
    "answer": "False",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates x as falsy, returning 'False'."
  },
  {
    "question": "What does const max = (a, b) => a > b ? a : b; console.log(max(5, 3)); output?",
    "options": [
      "5",
      "3",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The ternary operator returns the larger of a or b, which is 5."
  },
  {
    "question": "What does const x = null; console.log(x ? 'Yes' : 'No'); output?",
    "options": [
      "No",
      "Yes",
      "null",
      "undefined"
    ],
    "answer": "No",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates null as falsy, returning 'No'."
  },
  {
    "question": "What does [...[1, 2], 3] return?",
    "options": [
      "[1, 2, 3]",
      "[1, 2]",
      "[3]",
      "Error"
    ],
    "answer": "[1, 2, 3]",
    "difficulty": "Medium",
    "explanation": "The spread operator spreads the array [1, 2] and adds 3 to create a new array."
  },
  {
    "question": "What does const arr = [1, 2]; console.log([...arr, ...arr]); output?",
    "options": [
      "[1, 2, 1, 2]",
      "[1, 2]",
      "[1, 1, 2, 2]",
      "Error"
    ],
    "answer": "[1, 2, 1, 2]",
    "difficulty": "Medium",
    "explanation": "The spread operator spreads arr twice, creating a new array with its elements repeated."
  },
  {
    "question": "What does const obj = { a: 1 }; console.log({ ...obj, b: 2 }); output?",
    "options": [
      "{ a: 1, b: 2 }",
      "{ a: 1 }",
      "{ b: 2 }",
      "Error"
    ],
    "answer": "{ a: 1, b: 2 }",
    "difficulty": "Medium",
    "explanation": "The spread operator copies obj’s properties and adds b: 2 to the new object."
  },
  {
    "question": "What does function fn(...args) { return args; } console.log(fn(1, 2, 3)); output?",
    "options": [
      "[1, 2, 3]",
      "1, 2, 3",
      "undefined",
      "Error"
    ],
    "answer": "[1, 2, 3]",
    "difficulty": "Medium",
    "explanation": "The spread operator in parameters collects arguments into an array."
  },
  {
    "question": "What does const arr = [1, 2]; console.log([...arr].reverse()); output?",
    "options": [
      "[2, 1]",
      "[1, 2]",
      "undefined",
      "Error"
    ],
    "answer": "[2, 1]",
    "difficulty": "Medium",
    "explanation": "The spread operator creates a new array, which is then reversed."
  },
  {
    "question": "What does const obj = { a: 1 }; const newObj = { ...obj, a: 2 }; console.log(newObj.a); output?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "The spread operator copies obj, and the new a: 2 overrides the original a: 1."
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

















