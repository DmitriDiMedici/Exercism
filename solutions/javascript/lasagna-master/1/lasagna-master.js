export function cookingStatus(timer) {
  if (timer == undefined) {
    return "You forgot to set the timer.";
  } else if (timer == 0) {
    return "Lasagna is done.";
  } else {
    return "Not done, please wait.";
  }
}

export function preparationTime(layers, prepTime = 2) {
  return layers.length * prepTime;
}

export function quantities(layers) {
  let numOfNoodles = layers.filter((element) => element === "noodles").length;
  let numOfSauce = layers.filter((element) => element === "sauce").length;

  return {
    noodles: numOfNoodles * 50,
    sauce: numOfSauce * 0.2,
  };
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList.at(-1));
}

export function scaleRecipe(recipe, portions = 2) {
  let scaledRecipe = {};
  Object.keys(recipe).forEach((key) => {
    scaledRecipe[key] = recipe[key] * (portions / 2);
  });
  return scaledRecipe;
}