const checkForm = document.getElementById("checkForm");
const resultElement = document.getElementById("resultElement");

async function check(url) {
  const response = await fetch("/check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url }),
  });
  const json = await response.json();
  return json;
}

checkForm.addEventListener("submit", async e => {
  e.preventDefault();
  resultElement.textContent = "Checking...";
  const url = e.target[0].value;
  const result = await check(url);
  resultElement.textContent = result.label;
});
