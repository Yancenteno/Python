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
    while(cents >=25){
        quarter++;
    }
    return console.log("quarter :", quarter)



}

console.log(fewestCoinChange(cents1))