$(document).ready(function () {
    $('.delete-from-cart').submit(function(e) {
        e.preventDefault();
        let data = $(this).serializeArray()
        let form = $(this)
        let receiptProduct = $('.solo-product-'+data[1].value)
        let totalPrice = parseInt($('.total-price').text());
        console.log(receiptProduct)
        console.log(totalPrice)
        console.log(data[1].value)
        // console.log(data)
        $.ajax({
            type: "POST",
            url: $('#url_delete_from_cart').val(),
            data: data,
            success: function(){
                form.remove()
                receiptProduct.remove()
                // totalPrice = 0
                // $('.total-price').html(totalPrice)
            }
        })
    })
})

// function updateFinalPrice() {
//     let total
// }