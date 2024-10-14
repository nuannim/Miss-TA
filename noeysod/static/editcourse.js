function addRequirements(){
    const requirements_column = document.getElementById("requirements-column");
    const old_button = requirements_column.querySelector(".add-requirement-button");
    if (old_button) {
        old_button.remove();
    }

        const input_box = document.createElement("div");
        input_box.className = "input-box";

        const text_label = document.createElement("label");
        text_label.innerHTML = "Requirements :";
        text_label.htmlFor = "text";

        const text_input = document.createElement("input");
        text_input.type = "text";
        text_input.placeholder = "requirements";
        text_input.required = true;

        const add_button = document.createElement("button");
        add_button.innerHTML = "add";
        add_button.type = "button";
        add_button.className = "add-requirement-button";
        add_button.setAttribute( "onClick", "javascript: addRequirements();" );
            
        const check = document.createElement("div");
        check.className = "check";
        
        const required_label = document.createElement("label");
        required_label.innerHTML = "จำเป็นต้องตอบคำถามนี้";

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        
        check.appendChild(required_label);
        check.appendChild(checkbox);
        
        input_box.appendChild(text_label);
        input_box.appendChild(text_input);
        input_box.appendChild(add_button);
        input_box.appendChild(check);
    
        requirements_column.appendChild(input_box);
}

function openDeletePopup(){
    document.querySelector(".popup_box").style.display = "flex";
}

document.querySelector('.close_popup_button').addEventListener('click', function() {
    document.querySelector('.popup_box').style.display = 'none';
});
document.querySelector('.confirm_button').addEventListener('click', function() {
    document.querySelector('.popup_box').style.display = 'none';
});

document.querySelector('.edit_close_popup_button').addEventListener('click', function() {
    document.querySelector('.edit_popup_box').style.display = 'none';
});

function openEditCoursePopup(){
    document.querySelector('.but button').addEventListener('click', function() {
    
        const form = document.querySelector('.form');
        const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        let allFilled = true;
    
        inputs.forEach(input => {
            if (!input.value) {
                allFilled = false; 
            }
        });
    
        if (allFilled) {
            document.querySelector(".edit_popup_box").style.display = "flex";
        }
    });
}