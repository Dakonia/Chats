let chat = document.querySelector("#chat");
let input = document.querySelector("#message-input");
let btnSubmit = document.querySelector("#btn-submit");
let chatId = 1;
const webSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${chatId}/`);

webSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    chat.innerHTML += '<div class="msg">' + data.message + '</div>';
};

btnSubmit.addEventListener("click", () => {
    let message = input.value;
    webSocket.send(JSON.stringify({
        'message': message
    }));
    input.value = '';
});
