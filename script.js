document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("rain-form");
  const inputs = form.querySelectorAll("input");

  inputs.forEach((input) => {
    input.addEventListener("focus", () => {
      input.style.borderColor = "#1976d2";
    });
    input.addEventListener("blur", () => {
      input.style.borderColor = "#ccc";
    });
  });

  form.addEventListener("submit", () => {
    const button = document.getElementById("submit-btn");
    button.disabled = true;
    button.textContent = "Predicting...";
  });
});
