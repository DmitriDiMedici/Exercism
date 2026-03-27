export function format(name, number) {
  let ordinalSuffix = "";
  let turn = number.toString();

  if (
    turn.slice(-2) === "11" ||
    turn.slice(-2) === "12" ||
    turn.slice(-2) === "13"
  ) {
    ordinalSuffix = "th";
  } else if (turn.at(-1) == "1") {
    ordinalSuffix = "st";
  } else if (turn.at(-1) == "2") {
    ordinalSuffix = "nd";
  } else if (turn.at(-1) == "3") {
    ordinalSuffix = "rd";
  } else {
    ordinalSuffix = "th";
  }

  return `${name}, you are the ${number}${ordinalSuffix} customer we serve today. Thank you!`;
}
