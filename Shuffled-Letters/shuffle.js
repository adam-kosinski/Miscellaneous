const textarea = document.getElementById("input");
const output = document.getElementById("output");

textarea.addEventListener("input", () => {
  output.innerHTML = processText(textarea.value);
});

function processText(text) {
  return text
    .replaceAll(/\w+/g, (s) => shuffleInnerLetters(s))
    .replaceAll(/\n/g, "<br>");
}

function shuffleInnerLetters(word) {
  if (word.length <= 3) return word;
  const inner = word.substring(1, word.length - 1);
  return word[0] + shuffle(inner) + word[word.length - 1];
}

function shuffle(s) {
  const letters = s.split("");
  let out = "";
  while (letters.length > 0) {
    const i = Math.floor(letters.length * Math.random());
    out += letters.splice(i, 1)[0];
  }
  return out;
}
