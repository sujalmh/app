document.querySelector("form").addEventListener("submit", function (e) {
    const emailField = document.getElementById("email");
    if (!emailField.value.includes("@")) {
        alert("Please enter a valid email address.");
        e.preventDefault();
    }
});
