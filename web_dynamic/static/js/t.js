document.addEventListener('DOMContentLoaded', function () {
  const uploadButton = $('#uploadButton');
  const imageInput = $('#imageInput');
  uploadButton.on('click', () => {
    imageInput.click();
  });
  const form = document.querySelector('.settings');
  const formButton = $('.arrow');
  formButton.on('click', () => {
      form.style.display = 'none';
    });
  const more = $('.more-settings');
  more.on('click', () => {
    form.style.display = 'flex';
  });
  const usersURL = 'https://techinspire.tech/api/v1/users/';
  const messageURL = 'https://techinspire.tech/api/v1/conversations/';
  let currentUser;

  const loadCurrentUser = () => {
    const userImage = document.querySelector('.user-image');
    userImage.classList.add('user-pic');
    const img = document.createElement('img');
    const url = usersURL + currentUser.id + '/image';
    img.src = url;
    userImage.appendChild(img);
  };
  $.get(usersURL).done((data) => {
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
      const putUrl = usersURL + `${currentUser.id}/upload`;
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
  const socket = io();
  let convId;
  let rec;
  let sender;
  socket.connect('https://techinspire.tech');

  socket.on('receivedMessage', (message) => {
    console.log('receiving message', message);
    const content = message.message;
    const time = message.timestamp;
    const sender = message.sender;
    const messageA = [message]
    console.log(currentUser.id, message.sender_id);
    displayMessage(messageA);
  });
  socket.on('receivedFile', (message) => {
    displayFile([message]);
  });

  const getImage = (url) => {
    $.get(url).done((data) => {
      const b = new Blob([data]);
      const fr = new FileReader();
      fr.readAsDataURL(b);
      return fr;
    });
  };
  function loadUserImage(user, el, userPicDiv, userPar) {
    const url = usersURL + `${user.id}/image`;
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
  // Function to load and display messages for a user
  function loadMessages(user, currentUser) {
    const userConvIds = user.conversation_ids;
    const senderConvIds = currentUser.conversation_ids;

    const conv = userConvIds.find((id) => senderConvIds.includes(id));
    convId = conv;
    rec = user;
    sender = currentUser;
    let messages = [];
    const messageUrl = messageURL + `${convId}/messages`;
    //socket message
    if (convId != undefined) {
    $.get(messageUrl).done((data) => {
      $.each(data, (i, msg) => {
        const mess = [];
        mess.push(msg);
        messages.push(mess);
      });
      messages.forEach((message) => {
        displayMessage(message, currentUser);
      });
    });
    }

    current = user;
    userHeader.innerHTML = '';
    messagesContainer.innerHTML = '';
    displayHeader(user, userHeader, userPic, userP);
  }
  // display File to chat area
  const fileIds = [];
  const displayFile = (messageArray, currentUser) => {
    const messageDiv = document.createElement('div');
    const fileId = messageArray[0].id;

    const getUrl = messageURL + `${convId}/file/${fileId}`;
    setMessageClass(messageArray[0].sender_id, messageDiv);
    const thumbnailElement = document.createElement('img');

    thumbnailElement.src = getUrl
    thumbnailElement.classList.add('uploaded-image');
    const ftime = getTime(messageArray[0].timestamp);
    const pTime = document.createElement('p');
    pTime.classList.add('time');
    const m = document.createTextNode(ftime);
    pTime.appendChild(m);
    messageDiv.appendChild(thumbnailElement);
    messageDiv.appendChild(pTime);
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  // appendMessage to main message container
  const appendMessage = (messageDiv, content, time) => {
    const pMsg = document.createElement('p');
    const pTime = document.createElement('p');
    pTime.classList.add('time');
    const m = document.createTextNode(content);
    const m2 = document.createTextNode(time);
    pMsg.appendChild(m);
    pTime.appendChild(m2);
    messageDiv.appendChild(pMsg);
    messageDiv.appendChild(pTime);
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  const setMessageClass = (sender, messageDiv) => {
    if (sender === currentUser.id) {
      messageDiv.style.marginTop = '10px';
      messageDiv.style.color = 'red';
      messageDiv.classList.add('sent-message');
    } else {
      messageDiv.classList.add('received-message');
    }
  }
  // get local time
  const getTime = (serverTime) => {
    const time = new Date(serverTime);
    const tzone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const ftime = time.toLocaleTimeString(undefined, {tzone, hour: '2-digit', minute: '2-digit', hour12: false });
    return ftime;
  };
  // Function to display a message in the chat area
  function displayMessage(messageArray, currentUser, file) {
    const messageDiv = document.createElement('div');
    const content = messageArray[0].content;
    const ftime = getTime(messageArray[0].timestamp);
    const sender = messageArray[0].sender_id;
    fl = messageArray[0].isFile
    setMessageClass(sender, messageDiv);
    if (!file && !fl) {
      appendMessage(messageDiv, content, ftime);
    } else {
      displayFile(messageArray, currentUser);
    }
  }

  // Function to send a message
  const send = (message, convId) => {
    if (message !== '') {

      const postUrl = messageURL + `${convId}/messages`;
      const time = new Date();

      const messageArray = [message, currentUser.id, time];
      const messageData = {
        content: message,
        timestamp: time,
        sender_id: currentUser.id,
      };
      socket.emit('sendMessage', messageData);

      messageInput.value = ''; //clear input field

      let sdata = {
        content: message,
        sender_id: currentUser.id,
        timestamp: time,
      };
      sdata = JSON.stringify(sdata);
      $.post({
        url: postUrl,
        data: sdata,
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => {
        console.log('sent-message', data);
      })
        .fail((er) => console.error('Error:', er));
    }
  };
  const sendButton = $('#send-button');
  sendButton.on('click', () => {
    sendMessage();
  })
  const sendMessage = function () {
    const message = messageInput.value.trim();
    let isFile = fileInput.files.length > 0;
    if (message.length > 0 && convId === undefined && !isFile) {
      // create a conversatonId
      let sdata = {
        participants: [currentUser.id, rec.id],
      };
      sdata = JSON.stringify(sdata);
      $.post({
        url: messageURL,
        data: sdata,
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => {
        convId = data.id;
        messagesContainer.innerHTML = '';
        send(message, convId);
        toggleSendButton();
      });
    } else if (message.length > 0 && convId && !isFile) {
      send(message, convId);
      toggleSendButton();
    } else if (isFile && convId === undefined) {
      let sdata = {
        participants: [currentUser.id, rec.id],
      };
      sdata = JSON.stringify(sdata);
      $.post({
        url: messageURL,
        data: sdata,
        headers: { 'Content-Type': 'application/json' },
      }).done((data) => {
        convId = data.id;
        messagesContainer.innerHTML = '';

        const file = fileInput.files[0];
        const messageArray = [file, currentUser.id];
        socket.emit('sendFile', messageArray);
        const fileUrl = messageURL + `${convId}/${currentUser.id}/messages/file`;
        const fData = new FormData();
        fData.append('file', file);
        const fileData = {
          file: fData,
        };
        $.post({
          url: fileUrl,
          data: fData,
          contentType: false,
          processData: false,
        }).done((data) => {
          console.log(data);
          fileInput.value = ''
          toggleSendButton();
        })
          .fail((er) => console.error('Error', er));
      });
    } else {

      const file = fileInput.files[0];
      const fileUrl = messageURL + `${convId}/${currentUser.id}/messages/file`;
      const fData = new FormData();
      fData.append('file', file);
      const time = new Date();
      fData.append('timestamp', time);
      $.post({
        url: fileUrl,
        data: fData,
        contentType: false,
        processData: false,
      }).done((data) => {
        const messageArray = {
          id: data.id,
          sender_id: currentUser.id,
          timestamp: time,
        };
      socket.emit('sendFile', messageArray);
        fileInput.value = ''
        toggleSendButton()
      })
        .fail((er) => console.error('Error', er));
    }
  }

  window.toggleSendButton = function() {
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
