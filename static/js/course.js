
function openSuccessPopup() {
    const form = document.querySelector('.form');
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    let allFilled = true;

    inputs.forEach(input => {
        if (!input.value && !(input.type === 'radio' && input.checked)) {
            allFilled = false; 
        }
    });

    const radioGroups = {};
    form.querySelectorAll('input[type="radio"][name]').forEach(radio => {
        if (!radioGroups[radio.name]) {
            radioGroups[radio.name] = { checked: false };
        }
        if (radio.checked) {
            radioGroups[radio.name].checked = true;
        }
    });

    for (const group in radioGroups) {
        if (!radioGroups[group].checked) {
            allFilled = false;
            break;
        }
    }

    if (allFilled) {
        document.querySelector(".popup_box").style.display = "flex";
    }
}

document.querySelector('.close_popup_button').addEventListener('click', function() {
    document.querySelector('.popup_box').style.display = 'none';
});
