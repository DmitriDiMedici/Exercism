/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
  let minCeiled = Math.ceil(1000);
  let maxFloored = Math.floor(9999);
  let randomNumber = Math.floor(
    Math.random() * (maxFloored - minCeiled + 1) + minCeiled,
  );
  return `NCC-${randomNumber}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  return Math.random() * (42000.0 - 41000.0) + 41000.0;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  let options = ["D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"];
  let itemRandom = options[Math.floor(Math.random() * options.length)];
  return itemRandom;
}