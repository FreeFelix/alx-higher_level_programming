#!/usr/bin/node

$(document).ready(function() {
    $('#btn_translate').click(function() {
        let languageCode = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
