/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let res = init;
    for(let i=0;i<nums.length;i++)
    {
        res=fn(res,nums[i]);
    }
    if (nums.length === 0) return init;

    return res;
};