var form_elements = [...document.getElementsByTagName('input')];
var email_el = form_elements.find(element => element['id'] === "email");
var password_el = form_elements.find(element => element['id'] === "password");
var passwordconfirm_el = form_elements.find(element => element['id'] === "passwordconfirm");
var submit_button = document.getElementById('submit-button');
var clear_button = document.getElementById('clear-button')

window.onload = function () {
    clear_button.addEventListener('click', () => {
        form_elements.forEach(element => {
            element.value = ""
            element.classList.remove('is-valid')
            submit_button.setAttribute("disabled", true)
        })
    })
    form_elements.forEach(element => element.addEventListener('change', function () {
        Validate()
        if (hasValue(email_el) || hasValue(password_el) || hasValue(passwordconfirm_el)) {
            clear_button.removeAttribute("disabled")
        } else {
            clear_button.setAttribute("disabled", true)
        }
    }))
}

function Validate() {
    let email_valid;
    let password_valid;

    if (hasValue(email_el)) {
        if (!(hasValue(email_el, 5)) || !(email_el.value.includes('@'))) {
            email_el.classList.add("is-invalid");
            email_valid = false;
        } else {
            email_valid = true;
            email_el.classList.remove("is-invalid");
            email_el.classList.add("is-valid");
        }
    }

    if (hasValue(password_el, 5) && hasValue(passwordconfirm_el)) {
        if (!(password_el.value === passwordconfirm_el.value)) {
            passwordconfirm_el.classList.add("is-invalid");
            password_el.classList.remove('is-valid')
            password_valid = false;
        } else {
            password_valid = true;
            passwordconfirm_el.classList.remove("is-invalid")
            passwordconfirm_el.classList.add("is-valid")
            password_el.classList.add('is-valid')
        }
    }

    if (email_valid && password_valid) {
        if (submit_button.getAttribute("disabled") === "" || submit_button.getAttribute("disabled") === "true") {
            submit_button.removeAttribute("disabled")
        }
    } else {
        submit_button.setAttribute("disabled", true)
    }
}

function hasValue(element, val = 0) {
    return (element.value.length > val) ? true : false
}
