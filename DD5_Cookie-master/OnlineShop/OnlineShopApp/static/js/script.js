
// Поиск элементов класса button-plus по действию click
$('.button-plus').on('click', function() {
// Создание переменной number в котором находится элемент, которым мы манипулируем, берём родительский элемент, нахождение элемента span в родительском элементе, получение содержимого
    let amount = $(this).parent().find("span").html();
    let price = $(this).parent().find("h3").html();
// Добавляем к переменной number единицу
    amount++;
    let final_price = amount*price
    console.log(final_price)
// элемент, которым мы манипулируем, берём родительский элемент, находим элемент span в родительском элементе, меняем содержимое на переменную number
    $(this).parent().find("span").html(amount);
    $(this).parent().find("h2").html(final_price);
})


$('.button-minus').on('click', function() {
    let amount = $(this).parent().find('span').html();
    let price = $(this).parent().find("h3").html();
    if (amount > 1) {
        amount--;
        let final_price = amount*price
        $(this).parent().find('span').html(amount);
        $(this).parent().find("h2").html(final_price);
    }
})


$(document).ready(function() {
    $('.button').on('click', function(e){
        e.preventDefault();
        let thisButton = $(this).val();
        thisButton = document.getElementById(`${thisButton}`);
        $.ajax({
            url : $('.url_get').val(),
            type : 'POST',
            data : {
                amount : $(this).parent().find("span").html(),
                product : $(this).parent().find("button").val(),
                csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
            },
            success : function(){
                if (thisButton.classList.contains('button-del')) {
                    thisButton.closest('form').style.display = 'none';
                }
            },
        });
    });
});


