const users = ['User1', 'User2', 'User3'];
const messages = {
  'User1': ["one", "two"],
  'User2': ["hi", "me too"],
  'User3': ["okay"]
};

document.addEventListener('DOMContentLoaded', function () {
    const usersList = document.querySelector('.users-list');
    const messagesContainer = document.getElementById('messages-container');
    const typingIndicator = document.getElementById('typing-indicator');
  const messageInput = document.getElementById('message-input');
  const fileInput = document.getElementById('file-input');
   
  //const messageDiv = document.createElement('div');

    // Display users
    users.forEach(user => {
        const userDiv = document.createElement('div');
        userDiv.innerText = user;
        userDiv.addEventListener('click', () => loadMessages(user));
        usersList.appendChild(userDiv);
    });

    // Load initial messages
//  messages['User1'].forEach(message => {
//    window.alert(message);
//    displayMessage(message);
//  });
  loadMessages(users[0]);

    // Function to load and display messages for a user
  function loadMessages(user) {
    messagesContainer.innerHTML = '';
    messages[user].forEach(message => {
      //window.alert(message);
      displayMessage(message);
    });
  }

    // Function to display a message in the chat area
// app.js
// ... (previous JavaScript)

  let lastMessageType = null;

// Function to display a message in the chat area
  function displayMessage(message, messageType) {
    const messageDiv = document.createElement('div');
    messageDiv.innerText = message;

    messageDiv.classList.add(messageType === 'sent' ? 'sent-message' : 'received-message');
    messagesContainer.appendChild(messageDiv);
   // lastMessageType = messageType;
   // window.alert(message);
  }
  


// ... (remaining JavaScript)


});
