document.addEventListener('DOMContentLoaded', function () {
  const uploadButton = $('#uploadButton');
  const imageInput = $('#imageInput');
  uploadButton.on('click', () => {
    imageInput.click();
  });

  const usersUrl = 'https://techinspire.tech/api/v1/users';
  let currentUser;

  const loadCurrentUser = () => {
    const userImage = document.querySelector('.user-image');
    userImage.classList.add('user-pic');
    const img = document.createElement('img');
    const url = `http://16.16.162.146/api/v1/users/${currentUser.id}/image`;
    img.src = url;
    userImage.appendChild(img);
  };
  $.get(usersUrl).done((data) => {
    data.sort((a, b) => {
      const a1 = a.user_name.toLowerCase();
      const b1 = b.user_name.toLowerCase();
      if (a1 < b1) return -1;
      if (a1 > b1) return 1;
      return 0;
    });
    const u = [];
    const users = [];
    const curr = document.querySelector('.user').textContent;
    $.each(data, (i, user) => {
      if (user.user_name === curr) {
        currentUser = user;
      }
      u.push(user.user_name);
      users.push(user);
    });
    loadCurrentUser();
    const v = users.filter((user) => user.user_name !== curr);
    loadUsers(v, currentUser);
  });

  imageInput.on('change', function () {
    const file = imageInput[0].files[0];
    if (file) {
      let formData = new FormData();
      formData.append('image', file);
      const putUrl = `http://16.16.162.146/api/v1/users/${currentUser.id}/upload`;
      let path = '';
      formData.forEach((d) => {
        path = d.name;
      });
      $.ajax({
        url: putUrl,
        type: 'PUT',
        data: formData,
        contentType: false,
        processData: false,
        success: (() => {
          location.reload();
        }),
        error: ((er) => console.log('Error', er)),
      });
    }
  });
  const usersList = document.querySelector('.users-list');
  const messagesContainer = document.getElementById('messages-container');
  const typingIndicator = document.getElementById('typing-indicator');
  const messageInput = document.getElementById('message-input');
  const fileInput = document.getElementById('file-input');
  const header = document.querySelector('.chat-header');
  const sideBar = document.querySelector('.side-bar');
  const userPic = document.createElement('div');
  const userP = document.createElement('p');
  const userHeader = document.querySelector('.user-header');
//  const socket = io();
  let convId;
  let rec;
  let sender;
  //socket.connect('http:16.16.162.146');
  const getImage = (url) => {
    $.get(url).done((data) => {
      const b = new Blob([data]);
      const fr = new FileReader();
      fr.readAsDataURL(b);
      return fr;
    });
  };
  function loadUserImage(user, el, userPicDiv, userPar) {
    const url = `http://16.16.162.146/api/v1/users/${user.id}/image`;
    let imageSrc;
    imageSrc = getImage(url);
    const userImage = document.createElement('img');
    userPicDiv.innerHTML = '';
    userPar.innerHTML = '';
    userPicDiv.classList.add('user-pic');
    userPar.classList.add('user-name');
    userPicDiv.appendChild(userImage);
    userImage.src = url;
    const userName = document.createTextNode(user.user_name);
    userPar.appendChild(userName);

    el.appendChild(userPicDiv);
    el.appendChild(userPar);
  }

  function displayHeader(user, el, userPicDiv, userPar) {
    if (userPicDiv && userPar) {
      const userDiv = document.createElement('div');
      loadUserImage(user, userDiv, userPicDiv, userPar);
      el.appendChild(userDiv);
    } else {
      const userPic = document.createElement('div');
      const userP = document.createElement('p');
      loadUserImage(user, el, userPic, userP);
    }
  }
  let current = ''
  // Display users
  const loadUsers = (users, currentUser) => {
    users.forEach(user => {
      const userDiv = document.createElement('div');
      userDiv.addEventListener('click', () => {
        loadMessages(user, currentUser);
      });
      displayHeader(user, userDiv);
      usersList.appendChild(userDiv);
    });
  };

  //  loadMessages(users[0]);
  // Function to load and display messages for a user
  function loadMessages(user, currentUser) {
    const userConvIds = user.conversation_ids;
    const senderConvIds = currentUser.conversation_ids;

    const conv = userConvIds.find((id) => senderConvIds.includes(id));
    convId = conv;
    rec = user;
    sender = currentUser;
    let messages = [];
    const messageUrl = `http://16.16.162.146/api/v1/conversations/${convId}/messages`;
    $.get(messageUrl).done((data) => {
      $.each(data, (i, msg) => {
        const mess = [];
        mess.push(msg);
        messages.push(mess);
      });
      messages.forEach((message) => displayMessage(message, currentUser));
    });

    current = user;
    userHeader.innerHTML = '';
    messagesContainer.innerHTML = '';
    displayHeader(user, userHeader, userPic, userP);
  }
  // Function to display a message in the chat area
  function displayMessage(messageArray, currentUser, messageType, f) {
  const messageDiv = document.createElement('div');
    const content = messageArray[0].content;
    const sender = messageArray[0].sender_id;
    const fl = messageArray[0].file;
    if (sender === currentUser.id) {
      console.log(currentUser.id)
      messageDiv.style.marginTop = '10px';
      messageDiv.style.color = 'red';
      messageDiv.classList.add('sent-message');
    } else {
      messageDiv.classList.add('received-message');
    }
    if (messageType === 'image') {
      const reader = new FileReader();
      reader.addEventListener('load', () => {
        const thumbnailElement = document.createElement('img');
        thumbnailElement.src = reader.result;
        thumbnailElement.classList.add('uploaded-image');
        messageDiv.appendChild(thumbnailElement);
      });
      reader.readAsDataURL(messageArray[0]);
      messagesContainer.appendChild(messageDiv);
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
      return;
    }
    if (fl !== null) {
      console.log(currentUser.id, sender);
      const getUrl = `http://16.16.162.146/api/v1/conversations/${convId}/file`;
      const pdata = {
        path: fl,
      };
      $.post({
        url: getUrl,
        data: JSON.stringify(pdata),
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => {
        const reader = new FileReader();
        const blob = new Blob([data], { type: 'image/jpeg' });
        reader.readAsDataURL(blob);
        reader.onload = () => {
          const thumbnailElement = document.createElement('img');
          thumbnailElement.src = reader.result;
          thumbnailElement.classList.add('uploaded-image');
          messageDiv.appendChild(thumbnailElement);
        };
        URL.revokeObjectURL(url);
        
      }).fail((er) => console.log('Error', er));
      messagesContainer.appendChild(messageDiv);
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
      
    }

    const p = document.createElement('p');
    const m = document.createTextNode(messageArray[0]);
    p.appendChild(m);
    messageDiv.appendChild(p);
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  // Function to send a message
  const send = (message, convId) => {
    if (message !== '') {
      const messageArray = [message, currentUser.id];
      displayMessage(messageArray, currentUser);
      //  socket.emit('message', message);
      messageInput.value = '';
      messagesContainer.scrollTop = messagesContainer.scrollHeight;

      const postUrl = `http://16.16.162.146/api/v1/conversations/${convId}/messages`;
      let sdata = {
        content: message,
        sender_id: currentUser.id,
      };
      sdata = JSON.stringify(sdata);
      $.post({
        url: postUrl,
        data: sdata,
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => console.log('data', data))
        .fail((er) => console.error('Error:', er));
    }
  };

  sendMessage = function () {
    const message = messageInput.value.trim();
    if (convId === undefined) {
      let sdata = {
        participants: [currentUser.id, rec.id],
      };
      sdata = JSON.stringify(sdata);
      $.post({
        url: 'http://16.16.162.146/api/v1/conversations',
        data: sdata,
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => {
        convId = data.id;
        messagesContainer.innerHTML = '';

        send(message, convId);
      });
    }
    const isFile = fileInput.files.length > 0;
    if (isFile) {
      const file = fileInput.files[0];
      const messageArray = [file, currentUser.id];

      displayMessage(messageArray, currentUser, 'image');
      const fileUrl = `http://16.16.162.146/api/v1/conversations/${convId}/${currentUser.id}/messages/file`;
      const fData = new FormData();
      fData.append('file', file);
      //      messageArray[0] = fData;
      const fileData = {
        file: fData,
      };
      $.post({
        url: fileUrl,
        data: fData,
        contentType: false,
        processData: false,
      }).done((data) => console.log(data))
        .fail((er) => console.error('Error', er));
    }
    send(message, convId);
  };

  window.toggleSendButton = function () {
    const sendButton = document.getElementById('send-button');
    const messageInput = document.getElementById('message-input');

    const isMessage = messageInput.value.trim() !== '';

    const isFile = fileInput.files.length > 0;

    if (isMessage) {
      sendButton.style.display = 'inline-block';
    } else if (isFile) {
      sendButton.style.display = 'inline-block';
    } else {
      sendButton.style.display = 'none';
    }
  };
});
