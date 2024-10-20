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

function openEditCoursePopup() {
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
        document.querySelector(".edit_popup_box").style.display = "flex";
    }
}

// เอาไว้เปลี่ยนค่าจ้าง จำนวนวันตามรูปแบบงาน
document.getElementById('assistantType').addEventListener('change', function() {
    const wageInput = document.getElementById('wage');
    const daysInput = document.getElementById('days');
    const check3 = document.getElementById('check3');
    const check4 = document.getElementById('check4');
    const taskBox = document.getElementById('task-box');

    if (taskBox) {
        taskBox.remove();
    }
    if (this.options[this.selectedIndex].classList.contains('option1')) {
        wageInput.value = 100; 
        daysInput.value = null;
        daysInput.placeholder = "ไม่ต้องกรอกจำนวนวัน";
        wageInput.readOnly = true;
        daysInput.readOnly = true;
        daysInput.required = false;
        check3.setAttribute('disabled', true);
        check4.setAttribute('disabled', true);
        check3.checked = true;
    }
    else if (this.options[this.selectedIndex].classList.contains('option2') || this.options[this.selectedIndex].classList.contains('option3')
    || this.options[this.selectedIndex].classList.contains('option4') || this.options[this.selectedIndex].classList.contains('option5')) {
        wageInput.value = 50;
        daysInput.value = ""; 
        daysInput.placeholder = "กรอกได้ไม่เกิน 15 วัน";
        wageInput.readOnly = true;
        daysInput.readOnly = false;
        daysInput.required = true;
        check3.disabled = false;
        check4.disabled = false;
        check3.checked = false;
    }  
    else if (this.options[this.selectedIndex].classList.contains('option6')) {
        addTaskDetail();
        wageInput.value = ''; 
        daysInput.value = '';
        wageInput.readOnly = false;
        daysInput.readOnly = false;
        daysInput.required = true;
        check3.disabled = false;
        check4.disabled = false;
        check3.checked = false;
        check4.checked = false;
        daysInput.placeholder = "กรอกได้ไม่เกิน 15 วัน";
    }  
    else {
        wageInput.value = ''; 
        daysInput.value = '';
        wageInput.readOnly = false;
        daysInput.readOnly = false;
        daysInput.required = true;
        daysInput.placeholder = "กรอกได้ไม่เกิน 15 วัน";
        check3.disabled = false;
        check4.disabled = false;
        check3.checked = false;
        check4.checked = false;
    }
});

const numberInput = document.getElementById('days');
numberInput.addEventListener('input', function() {
    if (numberInput.value > 15) {
        numberInput.value = 15;
    }
});

const wagemin = document.getElementById('wage');
wagemin.addEventListener('input', function() {
    if (wagemin.value < 0) {
        wagemin.value = 0;
    }
});

function addTaskDetail(){
    const newHtml = `
                <div class="input-box" id="task-box">
                    <label for="task">งาน :</label>
                    <input type="text" id="task" placeholder="กรอกชื่องาน" required>
                </div>
            `;
            document.getElementById('task-detail').insertAdjacentHTML('afterbegin', newHtml);
}

// window.onload = function() {
//     const wageInput = document.getElementById('wage');
//     const daysInput = document.getElementById('days');
//     const check3 = document.getElementById('check3');
//     const check4 = document.getElementById('check4');
//     const taskBox = document.getElementById('task-box');
//     wageInput.value = 100; 
//         daysInput.value = null;
//         daysInput.placeholder = "ไม่ต้องกรอกจำนวนวัน";
//         wageInput.readOnly = true;
//         daysInput.readOnly = true;
//         daysInput.required = false;
//         check3.setAttribute('disabled', true);
//         check4.setAttribute('disabled', true);
//         check3.checked = true;
// };
