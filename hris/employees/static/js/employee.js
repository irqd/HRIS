const password = document.querySelector("#password");
const confirmPassword = document.querySelector("#confirmpassword");
const passwordValidation = document.querySelector("#password-validation");

confirmPassword.addEventListener("input", function () {
  if (this.value === "") {
    passwordValidation.innerHTML = "";
    confirmPassword.className = "form-control";
  } else if (password.value !== this.value) {
    passwordValidation.innerHTML = `
             <small class="text-danger" style="position: absolute; right: 170px;">
                Passwords do not match.
             </small>
       `;
    confirmPassword.className = "form-control is-invalid";
  } else {
    passwordValidation.innerHTML = `
             <small class="text-success" style="position: absolute; right: 225px;">
                Passwords match.
             </small>
       `;
    confirmPassword.className = "form-control is-valid";
  }
});

// ------------------------------------------------------------------------------------//

$("#datepicker").datepicker({
   uiLibrary: "bootstrap4",
   format: "yyyy-dd-mm",
 });

 $("#datepicker2").datepicker({
   uiLibrary: "bootstrap4",
   format: "yyyy-dd-mm",
 });

 $("#datepicker3").datepicker({
   uiLibrary: "bootstrap4",
   format: "yyyy-dd-mm",
 });

 // ------------------------------------------------------------------------------------//

const customFileInput = document.querySelector("#imageFile");
const customFileLabel = document.querySelector(".custom-file-label");

customFileInput.addEventListener("change", function () {
  customFileLabel.innerHTML = this.files[0].name;
});

imageFile.onchange = (evt) => {
  const [file] = imageFile.files;
  if (file) {
    imagePath.src = URL.createObjectURL(file);
  }
};

 // ------------------------------------------------------------------------------------//