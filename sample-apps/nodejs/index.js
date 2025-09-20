/**
 * Sample Node.js application for GitHub Actions examples
 */

function greet(name = 'World') {
  return `Hello, ${name}!`;
}

function add(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Both arguments must be numbers');
  }
  return a + b;
}

function main() {
  console.log(greet('GitHub Actions'));
  console.log(`2 + 3 = ${add(2, 3)}`);
  console.log('Sample Node.js application is running!');
}

// Export functions for testing
module.exports = { greet, add };

// Run main function if this file is executed directly
if (require.main === module) {
  main();
}