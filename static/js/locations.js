window.onload = function () {
    $(".accordion-header").on("click", "button[type='button']", function () {
        let t_href = event.target;
        console.log(t_href.id)
        let production_id = this.getAttribute("production_id")
        let workshop_id = this.getAttribute("workshop_id")
        let compartment_id = this.getAttribute("compartment_id")
        $.ajax({
            url: '/locations/' + production_id + '/' + workshop_id + '/' + compartment_id + '/',
            success: function (data) {
                $(".equipments").html(data.result);
            }
        });
        event.preventDefault()
    })
}