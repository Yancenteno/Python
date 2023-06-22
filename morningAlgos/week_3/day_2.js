
/* 
    Given a SORTED array of integers, dedupe the array 
    Because array elements are already in order, all duplicate values will be grouped together.

    Ok to use a new array

    Bonus: (no nested loops, new array ok)
    Bonus: Do it in-place (no new array)

*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
// Loop through the array, using a for/while loop.
// Conditions to look for: Checking if two indexes next to each other are equal. 
// If they are not equal -> Push to a new array. 

// To do this in place, we can use built ins like pop(). 


// Keep in mind, the array is safe to assume as always sorted lowest to highest. 
 */
function dedupeSorted(nums) {
    let temp = [];
    for (let i = 0; i < nums.length; i++) {
        if (temp.indexOf(nums[i]) === -1) {
            temp.push(nums[i]);
        }
    }
    return temp;
}
console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))
console.log(dedupeSorted(nums4))
/*****************************************************************************/


function dedupeSorted(nums) {
    let dupe = nums[0];
    let result = [dupe];
    for (let i = 1; i < nums.length; i++){
        if (nums[i] != dupe){
            dupe = nums[i];
            result.push(nums[i])
        }
    }
    return result
}
let test = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5]
// adjust array in place
function dedupeSorted2(nums){
    // set variable to check
    let dupe = nums[0]                      // constant to check if variable has changed
    let popCount = 0;                       // number of times we pop at the end
    let indexChange = 1;                    // position where we will move different variable to
    for (let i = 1; i < nums.length; i++){  // if value does not match dupe
        if (nums[i] == dupe){               // check if value matches dupe
            popCount++;                     // increase popCount for how many times we pop the array at the end
        } else if (nums[i] != dupe){        // if value does not match dupe
            dupe = nums[i];                 // update dupe value to new value
            nums[indexChange] = nums[i];    // move new value to earlier position in array
            indexChange++;                  // increment indexChange to point to next position in array
        }
    }
    for (let i = 0; i < popCount; i++){     // pop the array for the amount of duplicated numbers
        nums.pop();
    }
}
console.log('==== test super long array ====');
console.log(dedupeSorted(test)); // expected [1,2,3,4,5]
dedupeSorted2(test);
console.log(test);