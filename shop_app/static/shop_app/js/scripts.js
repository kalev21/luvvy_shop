$(document).ready(function (){
    const form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e){
        e.preventDefault();
        console.log('123');
        const nmb = $('#number').val();
        console.log(nmb);
        const submit_btn = $('#submit_btn');

        const product_id = submit_btn.data('product_id');
        const product_name = submit_btn.data('name');
        const product_price = submit_btn.data('price');
        console.log(product_id)
        console.log(product_name)
        console.log(product_price)

    })
});
