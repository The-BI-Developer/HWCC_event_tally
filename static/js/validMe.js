function validateInteger() {
    const inputField = document.querySelector("input");
    const inputValue = inputField.value;

    if (!/^[0-9]+$/.test(inputValue)) {
        alert("Please enter a valid integer.");
        return false; // Prevent form submission
    }

    alert("Form submitted")

    const form = document.querySelector("form");
    form.reset();

    return true; // Allow form submission
}
