/* 
    Given an int to represent how much change is needed
    calculate the fewest number of coins needed to create that change,
    using the standard US denominations
*/


/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
*/
// Start with the highest denomination coins and work down.
// Divide the total number of cents by the highest value. ( cents / 25 )
// Subtracting the selected coin from the total cents we are trying to make. 

// We've finished when total cents reaches zero. 

// Return a object with the coin name and the total # of that coin.

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };


function fewestCoinChange(cents) {
    let quarter = 0;
    let dime = 0;
    let nickel = 0;
    let penny = 0;
    while(cents >= 25){
        cents = cents - 25;
        quarter++;
    }
    while(cents >= 10){
        cents = cents - 10;
        dime++;
    }
    while (cents >= 5){
        cents = cents - 5;
        nickel++;
    }
    while (cents >= 1){
        cents = cents - 1;
        penny++
    }
    return console.log("quarter :", quarter, "dime :", dime, "nickel :", nickel, "penny :", penny);
}

fewestCoinChange(cents1)
fewestCoinChange(cents2)
fewestCoinChange(cents3)
fewestCoinChange(cents4)
/*****************************************************************************/
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };


function fewestCoinChange(cents) {
    let quarter = 0;
    let dime = 0;
    let nickel = 0;
    let penny = 0;
    while(cents >= 25){
        cents = cents - 25;
        quarter++;
    }
    while(cents >= 10){
        cents = cents - 10;
        dime++;
    }
    while (cents >= 5){
        cents = cents - 5;
        nickel++;
    }
    while (cents >= 1){
        cents = cents - 1;
        penny++
    }
    return console.log("quarter :", quarter, "dime :", dime, "nickel :", nickel, "penny :", penny);
}

fewestCoinChange(cents1)
fewestCoinChange(cents2)
fewestCoinChange(cents3)
fewestCoinChange(cents4)