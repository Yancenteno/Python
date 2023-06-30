
/*
Sum To One Digit
Implement a function sumToOne(num)​ that,
given a number, sums that number’s digits
repeatedly until the sum is only one digit. Return
that final one digit result.

Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/


/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
*/


const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;


function sumToOneDigit(num) {
    let strNum = num.toString();
    let sum = 0;
    for (let i = 0; i < strNum.length; i++) {
        sum += parseInt(strNum[i])
    }
    return sum
}
console.log(sumToOneDigit(num1));
console.log(sumToOneDigit(num2));
console.log(sumToOneDigit(num3));
/*****************************************************************************/


function sumToOneDigitGoTo(num, i, sum) {
    if (num < 10) {
        return num
    }
    if (i == strNum.length) {
        return sum
    }
    let strNum = num.toString();
    for (let i = 0; i < strNum.length; i++) {
        sum += parseInt(strNum[i])
    }
    return sumToOneDigitGoTo(num, i + 1)
}
console.log(sumToOneDigitGoTo(num1, 0, 0));
console.log(sumToOneDigitGoTo(num2, 0, 0));
console.log(sumToOneDigitGoTo(num3, 0, 0));