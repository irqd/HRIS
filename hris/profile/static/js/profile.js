$("#datepicker").datepicker({
   uiLibrary: "bootstrap4",
   format: "yyyy-dd-mm",
});


const customFileInput = document.querySelector("#imageFile") ?? undefined;
const customFileLabel = document.querySelector(".custom-file-label");
const imageValidation = document.querySelector("#file_size_error");

const MAX_FILE_SIZE = 1 * 1024 * 1024; // 16MB in bytes

customFileInput?.addEventListener("change", function () {
  const file = this.files[0];
  if (file && file.size > MAX_FILE_SIZE) {
    
    this.value = null; // reset the file input
    customFileLabel.innerHTML = "Upload File"; // reset the label
    imageValidation.innerHTML = `
    <small class="text-danger mt-1" style="position: absolute;">
       File size is too large. Pleases select a file less than 1MB.
    </small>`;

    setTimeout(() => {
      imageValidation.innerHTML = "";
    }, 3000);
    
  } else {
    customFileLabel.innerHTML = file.name;
  }
});

imageFile?.addEventListener('change', (evt) => {
  const [file] = imageFile.files;
  if (file && file.size <= MAX_FILE_SIZE) {
    imagePath.src = URL.createObjectURL(file);
  }
});


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