import { getCookie } from "./main.js";

$(function ($) {
    $("#form_ajax").submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            headers: {"X-CSRFToken": getCookie("csrftoken")},
            dataType: "json",
            success: function (response) {
                if (response.status === 201) {
                    window.location.reload()
                } else if (response.status === 400) {
                    $('#danger_login').text(response.error).removeClass("d-none")
                }
            },
            error: function (response) {
                console.log("error - ", response)
            }
        })
    })
})