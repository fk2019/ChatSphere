// Add a "typing..." indicator to the last message when the user is typing.
const lastMessage = document.querySelector('.messages .message:last-child');
const typingIndicator = document.createElement('span');
typingIndicator.classList.add('typing-indicator');
typingIndicator.textContent = 'Typing...';

document.addEventListener('keydown', event => {
if (event.target === lastMessage.querySelector('input')) {
lastMessage.appendChild(typingIndicator);
}
});

document.addEventListener('keyup', event => {
if (event.target === lastMessage.querySelector('input')) {
lastMessage.removeChild(typingIndicator);
}
});
