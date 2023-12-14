$('#copy-button').on('click', function () {
    var copyText = $("#copy-input");
    copyText.select();
    try {
        var success = document.execCommand('copy');
        if (success) {
            $('#copy-button').trigger('copied', ['Copied!']);
        } else {
            $('#copy-button').trigger('copied', ['Copy with Ctrl-c']);
        }
    } catch (err) {
        $('#copy-button').trigger('copied', ['Copy with Ctrl-c']);
    }

    alert("Copied the text: " + copyText.val());
});

$('.form-signin').on('submit', function (event) {
    event.preventDefault();

    var inputUrl = $('#inputUrl').val();

    var url = window.location.origin + "/" + inputUrl;

    var copyableLink = $('#copy-input');
    copyableLink.val(url); // set the value of the input to the generated URL

    copyableLink.on('click', function (event) {
        event.preventDefault();
        navigator.clipboard.writeText(url);
    });
});