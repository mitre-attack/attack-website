/**
 * Debouncer is a utility class for debouncing function calls. It is used to debounce keyboard input so that rapid
 * keypresses doesn't overwhelm the computer.
 */
module.exports = class Debouncer {
  // new debouncer, param is the amount of debounce delay time in ms
  constructor(delay) {
    this.callback = null;
    this.i = 0;
    this.delay = delay;
  }

  // callback with debounce
  debounce(callback) {
    this.callback = callback;
    this.i++;
    const { i } = this;
    const self = this;
    setTimeout(() => {
      self.resolve(i);
    }, this.delay);
  }

  // resolve the debounced callback
  resolve(i) {
    // only do the callback if a new debounced input hasn't been added.
    if (this.i == i) this.callback();
  }
};
