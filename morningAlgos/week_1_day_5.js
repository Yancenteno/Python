/* 
    Zip Arrays into Map
    
    
    Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.

    Associative arrays are sometimes called maps because a key (string) maps to a value 
 */
function jsHash(keys, values) {
    let hashMap = {};
    for (let index = 0; index < keys.length; ++ index) {
        hashMap[keys[index]] = values[index];
    }
    return hashMap
}
    
    const keys1 = ["abc", 3, "yo"];
    const vals1 = [42, "wassup", true];
    console.log(jsHash(keys1, vals1));

    
function invertHash(dictionary) {
    const dictionaryKeys = Object.keys(dictionary);
    const dictionaryValues = Object.values(dictionary);
        return jsHash(dictionaryValues, dictionaryKeys);
}
    
console.log(invertHash(jsHash(keys1, vals1)));


// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

// const keys2 = [];
// const vals2 = [];
// const expected2 = {};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
// const keys = ["abc", 3, "yo"];
// const values = [42, "wassup", true];

// function zipArraysIntoMap(keys, values) { 
//     var obj = {};
//     keys.forEach(elem, index) => {
//         obj[elem] = values[index]
//     }
//     return obj
// }

// console.log(zipArraysIntoMap())

// function zipArraysIntoMap(keys, values){
//     var obj
// }

/*****************************************************************************/


/* 
    Invert Hash

    A hash table / hash map is an obj / dictionary

    Given an object / dict,
    return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj_1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected_1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) { }

/*****************************************************************************/
