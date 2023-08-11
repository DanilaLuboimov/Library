import { getCookie } from "./main.js";

$(function ($) {
    $("#form_feedback_ajax").submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            headers: {"X-CSRFToken": getCookie("csrftoken")},
            dataType: "json",
            success: function (response) {
                if (response.status === 201) {
                    $('#danger_feedback').text(response.error).addClass("d-none")
                    $('#success_feedback').text(response.message).removeClass("d-none")
                } else if (response.status === 400) {
                    $('#success_feedback').text(response.message).addClass("d-none")
                    $('#danger_feedback').text(response.error).removeClass("d-none")
                }
            },
            error: function (response) {
                console.log("error - ", response)
            }
        })
    })
})