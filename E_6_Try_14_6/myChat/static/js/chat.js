$(function() {
    var roomName = $('#room-name').text();
    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');
    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        $('#messages').append('<div class="message">' + message + '</div>');
    };
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
    $('#message-form').on('submit', function(e) {
        e.preventDefault();
        var messageInputDom = $('#message-form input[name="message"]');
        var message = messageInputDom.val();
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.val('');
    });
});
