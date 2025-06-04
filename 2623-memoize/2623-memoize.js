/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map()
    let res;
    return function(...args) {
        key=JSON.stringify(args)
        if(cache.has(key))
        {
            return (cache.get(key))
        }
        else{
            res=fn(...args)
            cache.set(key,res)
            return res
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */