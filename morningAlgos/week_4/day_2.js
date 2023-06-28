
/* 
    Recursive Factorial

    Input: integer
    Output: integer, product of ints from 1 up to given integer
    
    If less than zero, treat as zero.
    Bonus: If not integer, truncate (remove decimals).
    
    Experts tell us 0! is 1.
    
    rFact(3) = 6 (1*2*3)
    rFact(6.8) = 720 (1*2*3*4*5*6)
*/


/**
 * Recursively multiples 1 to the given int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} n The int to factorial. Treat negatives as zero and
 *    floor decimals.
 * @returns {number} The result of !n.
// We want to round down. Math.floor(n)
// Establish what the step is, and then also remember to write an end condition. (Such as reaching the value of n, or if n becomes 0 from reducing it like yesterday)
*/
const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;



function factorial(n) {
    n = Math.floor(n)
    if(n <= 0){
        return 1;
    }

    return n * factorial(n - 1)
}
console.log(factorial(num1))
console.log(factorial(num2))
console.log(factorial(num3))




/*****************************************************************************/

/* 
    Return the fibonacci number at the nth position, recursively.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    (0+1 -> 1, 1+1 -> 2, 1+2 -> 3, 2 + 3 -> 5...)

    The next number is found by adding up the two numbers before it,
    starting with 0 and 1 as the first two numbers of the sequence.
*/

const num4 = 0;
const expected4 = 0;

const num5 = 1;
const expected5 = 1;

const num6 = 2;
const expected6 = 1;

const num7 = 3;
const expected7 = 2;

const num8 = 4;
const expected8 = 3;

const num9 = 8;
const expected9 = 21;

/**
 * Recursively finds the nth number in the fibonacci sequence.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num The position of the desired number in the fibonacci sequence.
 * @returns {number} The fibonacci number at the given position.
// If n < 2 return n

// Stopping condition: if position is less than 2 return that number
// Keeping in mind the logic of the fibbonaci sequence: we want to check the 2 numbers prior to a value. (-2)
 */
function fibonacci(num) {
    if (i == times){
        return variable
    }
    return fibonacci()
}

/*****************************************************************************/
