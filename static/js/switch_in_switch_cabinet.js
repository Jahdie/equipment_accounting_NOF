window.onload = function () {
    $(".accordion-header").on("click", "button[type='button']", function () {
        let t_href = event.target;
        console.log(t_href)
        console.log(t_href.id)
        console.log(t_href.name)
        // console.log(t_href.slot)

        $.ajax({
            url: '/switch_cabinets/' + t_href.name + '/' + t_href.id + '/',
            success: function (data) {
                $(".ports").html(data.result);
            }
        });
        event.preventDefault()
    })
}
