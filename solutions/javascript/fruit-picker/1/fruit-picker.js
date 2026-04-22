import { notify } from "./notifier.js";
import { order } from "./grocer.js";

/**
 * @return void
 */
export function onSuccess() {
  notify({ message: "SUCCESS" });
}

/**
 * @return void
 */
export function onError() {
  notify({ message: "ERROR" });
}

/**
 * @param {GrocerQuery} query
 * @param {FruitPickerSuccessCallback} onSuccessCallback
 * @param {FruitPickerErrorCallback} onErrorCallback
 * @return void
 */
export function orderFromGrocer(query, onSuccessCallback, onErrorCallback) {
  order(query, onSuccess, onError);
}

/**
 * @param {string} variety
 * @param {number} quantity
 * @return void
 */
export function postOrder(variety, quantity) {
  const query = {
    variety: variety,
    quantity: quantity,
  };

  orderFromGrocer(query, onSuccess, onError);
}