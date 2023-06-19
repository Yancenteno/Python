/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    let reverseString="";
    for(var i=str.length-1; i>=0; i--) {
        reverseString += str[i]
    }
    return reverseString
}

function forwardReverse(str) {
    let forward="";
    for(let i=0; i<str.length; i++){
        forward=str[i] + forward
    }
    return forward
}

console.log(forwardReverse("yolo"))


//TEST CODE FOR REVERSE
console.log(reverseString("creature"))
console.log(reverseString("yolo"))

// try to do it without any built in methods!
// try to do it looping forwards only!