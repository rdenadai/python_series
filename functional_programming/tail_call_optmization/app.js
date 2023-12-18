const _recursive = (fnc, initializer, iterator) => {
  const item = iterator.splice(0, 1)?.[0];
  if (item) {
    initializer = fnc(initializer, item);
    return _recursive(fnc, initializer, iterator);
  }
  return initializer;
};

const reduce = (fnc, items, initializer) => {
  let _items = items.slice(0);
  if (!items) {
    throw Error("reduce() of empty sequence with no initial value");
  }
  if (initializer === undefined || initializer === null) {
    initializer = _items.splice(0, 1)?.[0];
  }
  return _recursive(fnc, initializer, _items);
};

console.assert(reduce((acc, cur) => acc + cur, [1, 2, 3, 4, 5]) === 15);
console.assert(
  reduce((acc, cur) => `${acc}+${cur}`, [1, 2, 3, 4, 5], "") === "+1+2+3+4+5"
);
console.assert(reduce((acc, cur) => acc + cur, [1, 2, 3, 4, 5]) === 15);

// On my machine 7_849 calls => RangeError: Maximum call stack size exceeded
console.assert(
  reduce((acc, cur) => acc + cur, [...Array(7_849).keys()]) === 30791628
);
