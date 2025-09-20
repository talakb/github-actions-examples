/**
 * Simple test suite for the Node.js sample application
 */

const { greet, add } = require('./index');

function assert(condition, message) {
  if (!condition) {
    throw new Error(`Test failed: ${message}`);
  }
}

function runTests() {
  console.log('Running tests...');
  
  // Test greet function
  assert(greet() === 'Hello, World!', 'greet() should return "Hello, World!"');
  assert(greet('GitHub') === 'Hello, GitHub!', 'greet("GitHub") should return "Hello, GitHub!"');
  
  // Test add function
  assert(add(2, 3) === 5, 'add(2, 3) should return 5');
  assert(add(-1, 1) === 0, 'add(-1, 1) should return 0');
  assert(add(0, 0) === 0, 'add(0, 0) should return 0');
  
  // Test error handling
  try {
    add('2', 3);
    throw new Error('add("2", 3) should throw an error');
  } catch (error) {
    if (error.message !== 'Both arguments must be numbers') {
      throw error;
    }
  }
  
  console.log('✅ All tests passed!');
}

if (require.main === module) {
  runTests();
}