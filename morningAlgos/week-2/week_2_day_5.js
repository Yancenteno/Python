
/* 
    Given an array of objects / dictionaries to represent new inventory,
    and an array of objects / dictionaries to represent current inventory,
    update the quantities of the current inventory
    
    if the item doesn't exist in current inventory, add it to the inventory

    return the current inventory after updating it.
*/

const newInv1 = [
    { name: "Grain of Rice", quantity: 9000 },
    { name: "Peanut Butter", quantity: 50 },
    { name: "Royal Jelly", quantity: 20 },
];
const currInv1 = [
    { name: "Peanut Butter", quantity: 20 },
    { name: "Grain of Rice", quantity: 1 },
];
const expected1 = [
    { name: "Peanut Butter", quantity: 70 },
    { name: "Grain of Rice", quantity: 9001 },
    { name: "Royal Jelly", quantity: 20 },
];

const newInv2 = [];
const currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
const expected2 = [{ name: "Peanut Butter", quantity: 20 }];

const newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
const currInv3 = [];
const expected3 = [{ name: "Peanut Butter", quantity: 20 }];

/**
 * @typedef {Object} Inventory
 * @property {string} Inventory.name The name of the item.
 * @property {number} Inventory.quantity The quantity of the item.
 */

/**
 * Updates the current inventory based on the new inventory.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<Inventory>} newInv A shipment of new inventory.
 *    An array of inventory objects.
 * @param {Array<Inventory>} currInv
 * @return The currInv after being updated.
 */
function updateInventory(newInv, currInv) {

    // Check key values from the inventory, to see if it exists in the inventory.
    // If it exists: We increase the quantity of the found key.
    // If it does not exist: append a new key/value pair into the existing inventory. 

    // Options:
    // Nested For Loops to itterate with dictionaries. 
    // Possibly  use any built in object methods in JS: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object
}

/*****************************************************************************/
function updateInventory(newInv, currInv) {
    for (let i = 0; i < newInv.length; i++) {               // loop through newInv
        let isInCurrent = false;                            // boolean to check if new item is in current list
        for (let j = 0; j < currInv.length; j++) {          // loop through currInv
            if (currInv[j].name == newInv[i].name) {        // check if newInv is in currInv
                currInv[j].quantity += newInv[i].quantity;  // add newInv quantity to currInv
                isInCurrent = true;                         // set boolean check to true
            }
        }                                                   // if new item is not in current inventory
        if (isInCurrent == false){                          // boolean remains false
            currInv.push(newInv[i]);                        // so we add the new item to current list
        }
    }

    return currInv
}