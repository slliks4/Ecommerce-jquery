$('.select').click(function (e) { 
    e.preventDefault();
    var $form =  $(this).closest('.item_select');
    var url = '/order_item_select/';
    var csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val();
    var order_item_id = $form.find('input[name=order_item_id]').val();
    var selected = $form.find('input[name=selected]').val();
    $.ajax({
        type: "POST",
        url: url,
        data: {
            'csrfmiddlewaretoken':csrf_token,
            'order_item_id':order_item_id,
            'selected':selected
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token);
        },
        success: function(response) {
            if (response.status === 'selected'){
                console.log('order item selected successfully')
                $form.find('.select').val('unselected').addClass('selected').removeClass('unselected');
                $form.find('input[name=selected]').val('unselect');
            }
            else if (response.status === 'unselected'){             
                console.log('order item unselected successfully');
                $form.find('.select').val('selected').addClass('unselected').removeClass('selected');
                $form.find('input[name=selected]').val('select');
            }
            else{
                console.log("error")
            }
        },
        error: function(xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
});

$('.quantity_val').on('input', function() {
    var input = $(this);
    var value = input.val();
    var sanitizedValue = value.replace(/\D/g, ''); // Remove non-numeric characters

    if (value !== sanitizedValue) {
        input.val(sanitizedValue); // Update input value with sanitized value
    }
});

$('.delete_order_item').click(function (e) { 
    e.preventDefault();
    var $form = $(this).closest('.change_qty_form');
    var $order_item = $(this).closest('.order_item')
    var url = "/delete_order_item/";
    var csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val();
    var order_item_id = $form.find('input[name=order_item_id]').val();
    $.ajax({
        type: "POST",
        url: url,
        data: {
            'csrfmiddlewaretoken':csrf_token,
            'order_item_id':order_item_id
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token);
        },
        success: function(response) {
            console.log(response);
            $order_item.remove();
        },
        error: function(xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
});

$('.reduce_qty').click(function(e) {
    e.preventDefault();
    var $form = $(this).closest('.change_qty_form');
    var $text = $(this).closest('.text');
    var url = '/edit_cart_items/';
    var csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val();
    var order_item_id = $form.find('input[name=order_item_id]').val();
    var quantity_val = $form.find('.quantity_val');
    var quantity = parseInt(quantity_val.val());
    var price = parseFloat(quantity_val.data('price'));
    var totalPrice = price * (quantity - 1);

    var currentQuantity = parseInt(quantity_val.val());
    if (currentQuantity > 1) {
        var newQuantity = currentQuantity - 1;
        $text.siblings('.price').find('.product_price').text('$ ' + totalPrice.toFixed(2));
        updateQuantity(order_item_id, newQuantity, csrf_token, url, quantity_val);
    }
});

$('.add_qty').click(function(e) {
    e.preventDefault();
    var $form = $(this).closest('.change_qty_form');
    var $text = $(this).closest('.text');
    var url = '/edit_cart_items/';
    var csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val();
    var order_item_id = $form.find('input[name=order_item_id]').val();
    var quantity_val = $form.find('.quantity_val');
    var quantity = parseInt(quantity_val.val());
    var price = parseFloat(quantity_val.data('price'));
    var totalPrice = price * (quantity + 1);
    var currentQuantity = parseInt(quantity_val.val());
    var newQuantity = currentQuantity + 1;
    $text.siblings('.price').find('.product_price').text('$ ' + totalPrice.toFixed(2));
    updateQuantity(order_item_id, newQuantity, csrf_token, url, quantity_val);
});

function updateQuantity(order_item_id, newQuantity, csrf_token, url, quantity_val) {
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'order_item_id': order_item_id,
            'quantity_val': newQuantity,
            'csrfmiddlewaretoken': csrf_token
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token);
        },
        success: function(response) {
            quantity_val.val(newQuantity);
            console.log(response);
        },
        error: function(xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}

