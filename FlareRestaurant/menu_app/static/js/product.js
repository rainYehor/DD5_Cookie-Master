let buttonPlus = document.querySelector('.button-plus')
let buttonMinus = document.querySelector('.button-minus')
console.log(buttonMinus)
let counterPrice = document.getElementById('count')

function counterPlus() {
    counterPrice.removeAttribute('readonly');
    counterPrice.value ++;
    console.log(counterPrice.value)
    counterPrice.setAttribute('readonly', 'readonly')
}

function counterMinus() {
    if (counterPrice.value > 1) {
        counterPrice.removeAttribute('readonly')
        counterPrice.value --;
        console.log(counterPrice.value)
        counterPrice.setAttribute('readonly', 'readonly')
    }
}

buttonPlus.addEventListener('click', counterPlus)
buttonMinus.addEventListener('click', counterMinus)

$(document).ready(function () {
    $('#add-to-cart').submit(function(e) {
        e.preventDefault();
        let data = $(this).serializeArray()
        let form = $(this)
        console.log(data)
        $.ajax({
            type: 'POST',
            url: $('.product').val(),
            data: data,
            success: function() {

            }
        })
    })
})