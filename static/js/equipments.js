window.onload = function () {
    $(".accordion-header").on("click", "button[type='button']", function () {
        let t_href = event.target;

        let automation_id = this.getAttribute("automation_id")
        let equipment_type_id = this.getAttribute("equipment_type_id")
        let equipment_name_id = this.getAttribute("equipment_name_id")
        console.log(automation_id, equipment_type_id, equipment_name_id)
        $.ajax({
            url: '/factory_equipments/' + automation_id + '/' + equipment_type_id + '/' + equipment_name_id + '/',
            success: function (data) {
                $(".signals").html(data.result);
            }
        });
        event.preventDefault()
    })
}