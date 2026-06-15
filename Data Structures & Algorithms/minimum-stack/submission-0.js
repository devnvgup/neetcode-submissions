class MinStack {
  arr = [];
  // ex : [1,2,0]
  constructor() {}

  /**
   * @param {number} val
   * @return {void}
   */
  push(val) {
    this.arr.push(val);
  }

  /**
   * @return {void}
   */
  pop() {
    this.arr.pop();
  }

  /**
   * @return {number}
   */
  top() {
    return this.arr[this.arr.length - 1];
  }

  /**
   * @return {number}
   */
  getMin() {
    let min = this.arr[0];
    for (let el of this.arr) {
      if (min > el) {
        min = el;
      }
    }
    console.log(min);
    return min;
  }
}