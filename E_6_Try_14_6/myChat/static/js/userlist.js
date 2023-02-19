$(document).ready(function() {
    $('#user-list').on('click', '.add-user-btn', function() {
        var userId = $(this).data('user-id');
        var url = $(this).data('url');
        $.post(url, {user_id: userId})
            .done(function() {
                console.log('User added successfully');
            })
            .fail(function() {
                console.error('Error adding user');
            });
    });
    $('#user-list').on('click', '.remove-user-btn', function() {
        var userId = $(this).data('user-id');
        var url = $(this).data('url');
        $.post(url, {user_id: userId})
            .done(function() {
                console.log('User removed successfully');
            })
            .fail(function() {
                console.error('Error removing user');
            });
    });
});
