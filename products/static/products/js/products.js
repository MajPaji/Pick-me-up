$(document).ready(function(){

    function handleButtonStatus(itemId) {
    var currentQty = parseInt($(`#id_qty_${itemId}`).val());
    var disableValueMinus = currentQty < 2;
    var disableValuePlus = currentQty > 98;
    $(`#decrease-qty_${itemId}`).prop('disabled', disableValueMinus);
    $(`#increase-qty_${itemId}`).prop('disabled', disableValuePlus);
    }

    $('.increase-qty').click(function(ev) {
        ev.preventDefault();
        var currentQty = parseInt($(this).parent().prev().val());
        $(this).parent().prev().val(currentQty+1);
        var itemId = $(this).data('item_id');
        $(`#update_btn_${itemId}`).css("display", "block");
        handleButtonStatus(itemId);
    })

    $('.decrease-qty').click(function(ev) {
        ev.preventDefault();
        var currentQty = parseInt($(this).parent().next().val());
        $(this).parent().next().val(currentQty-1);
        var itemId = $(this).data('item_id');
        $(`#update_btn_${itemId}`).css("display", "block");
        handleButtonStatus(itemId);
    })

    var allQtys = $('.qty_input');
    for(var i=0; i < allQtys.length; i++){
        var itemId=$(allQtys[i]).data('item_id');
        $(`#update_btn_${itemId}`).css("display", "none");
        handleButtonStatus(itemId);
    }

    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        $(`#update_btn_${itemId}`).css("display", "block");
        handleButtonStatus(itemId);
    });
});

