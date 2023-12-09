// app.js
// For simplicity, let's assume you have an array of users and messages
const users = ['User1', 'User2', 'User3'];
const messages = {
  'User1': ["ghh", "mmh"],
  'User2': ["hi", "me too"],
  'User3': ["okay"]
};

document.addEventListener('DOMContentLoaded', function () {
    const usersList = document.querySelector('.users-list');
    const messagesContainer = document.getElementById('messages-container');
    const typingIndicator = document.getElementById('typing-indicator');
    const messageInput = document.getElementById('message-input');

    // Display users
    users.forEach(user => {
        const userDiv = document.createElement('div');
        userDiv.innerText = user;
        userDiv.addEventListener('click', () => loadMessages(user));
        usersList.appendChild(userDiv);
    });

    // Load initial messages
    loadMessages(users[0]);

    // Function to load and display messages for a user
    function loadMessages(user) {
        messagesContainer.innerHTML = '';
        messages[user].forEach(message => {
            displayMessage(message);
        });
    }

    // Function to display a message in the chat area
  function displayMessage(message, messageType) {
        const messageDiv = document.createElement('div');
        messageDiv.innerText = message;
      messageDiv.classList.add(messageType == 'sent'? 'sent-message' : 'received-message';
        messagesContainer.appendChild(messageDiv);
    }

    // Function to simulate receiving a message (for testing purposes)
    function simulateReceiveMessage(user, message) {
        messages[user].push(message);
        if (user === activeUser) {
            displayMessage(message);
        }
    }

    // Simulate receiving messages (for testing purposes)
   // setInterval(() => {
    //    simulateReceiveMessage('User1', 'Hello!');
      //  simulateReceiveMessage('User2', 'Hi there!');
   // }, 5000);

    // Simulate typing indicator (for testing purposes)
    function showTypingIndicator(user) {
        typingIndicator.innerText = `${user} is typing...`;
    }

    function hideTypingIndicator() {
        typingIndicator.innerText = '';
    }

    let activeUser = users[0]; // Assume the first user is active initially

    // Function to send a message
    window.sendMessage = function () {
      const message = messageInput.value.trim();
      if (message !== '') {
        messages[activeUser].push(`You: ${message}`);
        displayMessage(`You: ${message}`, 'sent');
        messageInput.value = '';
        hideTypingIndicator();

      }
    };
  });
