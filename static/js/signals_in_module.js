window.onload = function () {
    $(".accordion-header").on("click", "button[type='button']", function () {
        let t_href = event.target;
        console.log(t_href)
        console.log(t_href.name)
        // console.log(t_href.slot)

        $.ajax({
            url: '/technical_equipments/' + t_href.name + '/' + t_href.id + '/' + t_href.slot + '/',
            success: function (data) {
                $(".signals").html(data.result);
            }
        });
        event.preventDefault()
    })
}
