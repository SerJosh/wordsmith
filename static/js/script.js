// var deleteButton = document.querySelector('.deletor');
// var deleteNotice = document.querySelector('.del-modal');

// function openModal() {
//     deleteNotice.style.display = 'block'
// }


// openModal();

document.getElementById("deletor").addEventListener("click", function () {
    document.getElementById("hide").style.display = 'block';
    document.getElementById("show-delete").style.display = 'none'

});

document.getElementById("cancelor").addEventListener("click", function () {
    document.getElementById("hide").style.display = 'none';
    document.getElementById("show-delete").style.display = 'block'

});