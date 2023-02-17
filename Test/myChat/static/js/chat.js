$(function() {
    var roomName = $('#room-name').text();
    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');
    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        $('#chat-log').append('<div class="message">' + message + '</div>');
    };
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
    $('#chat-message-input').focus();
    $('#chat-message-input').on('keyup', function(e) {
        if (e.keyCode === 13) {  // Enter key
            $('#chat-message-submit').click();
        }
    });
    $('#chat-message-submit').on('click', function(e) {
        var messageInputDom = $('#chat-message-input');
        var message = messageInputDom.val();
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.val('');
    });
});

