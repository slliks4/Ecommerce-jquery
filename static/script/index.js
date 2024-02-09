$('.add_to_cart').click(function (e) { 
    e.preventDefault();
    var $form = $(this).closest('.Cart');
    var url = "/add_to_cart/";
    var csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val();
    var product_id = $form.find('input[name=product_id]').val();
    $.ajax({
        type: "POST",
        url: url,
        data: {
            'csrfmiddlewaretoken':csrf_token,
            'product_id':product_id,
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token);
        },
        success: function(response) {
            console.log(response);
        },
        error: function(xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
});