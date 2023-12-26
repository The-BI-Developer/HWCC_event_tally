function validateInteger() {
    const inputField = document.querySelector("input");
    const inputValue = inputField.value;
    const form = document.querySelector("form");

    if (!/^[0-9]+$/.test(inputValue)) { //forward slashes bound regex whilst ! means logical not
        alert("Please enter a valid integer!");
        inputField.reset();
        return false; // Prevent form submission
    }

    alert("Sucess!Form submitted")

    return true; // Allow form submission
}
