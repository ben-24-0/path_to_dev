/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        let val=x;
        let len= functions.length;
        for(let i=len;i>0;i--)
        {
          fun=functions[i-1];
          val=fun(val);
        }
        return val;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */