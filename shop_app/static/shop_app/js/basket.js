window.onload = function () {
    $('.basket_list').on("click", "input[type='number']", function () {
        const t_href = event.target;
        $.ajax({
            url: "/shop_app/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
        event.preventDefault();
    });
};