//Click Event for Delete Button
// document.getElementById("deletor").addEventListener("click", function () {
//     document.getElementById("hide").style.display = 'block';
//     document.getElementById("show-delete").style.display = 'none';

// });
function displayDelete() {
    document.getElementById("hide").style.display = 'block';
    document.getElementById("show-delete").style.display = 'none';

};

function cancelDelete() {
    document.getElementById("hide").style.display = 'none';
    document.getElementById("show-delete").style.display = 'block';

};

//Click Event for Cancel Button
// document.getElementById("cancelor").addEventListener("click", function () {
//     document.getElementById("hide").style.display = 'none';
//     document.getElementById("show-delete").style.display = 'block';

// });