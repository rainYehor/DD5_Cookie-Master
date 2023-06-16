$(document).ready(function () {
    $('.delete_button').on('click', function() {
        $.ajax({
            type: "POST",
            url: $('#url_delete_from_cart').val(),
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                product_pk: $(this).parent().find('.product').val(),
            },
            success: function(){
                
            }
        })
    })
})
