$(document).ready(function() {
    $('#profile-image-input').change(function() {
        var input = this;
        var url = $(this).data('url');
        var img = $('#profile-image-preview');
        var reader = new FileReader();
        reader.onload = function (e) {
            img.attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
        var formdata = new FormData();
        formdata.append('image', input.files[0]);
        $.ajax({
            url: url,
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false,
            success: function() {
                console.log('Profile image updated successfully');
            },
            error: function() {
                console.error('Error updating profile image');
            }
        });
    });
});
