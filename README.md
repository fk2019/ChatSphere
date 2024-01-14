
# Table of Contents

1.  [Introduction](#org50fbf1d)
2.  [Getting Started](#org6b717f6)
3.  [Screenshots](#org396b13a)
    1.  [conversation with text](#org32f51f3)
    2.  [conversation with images](#orge7f9dff)
4.  [Technologies](#org9729beb)
5.  [API](#org1d4b586)
    1.  [messages](#org0bb5db3)
    2.  [conversations](#org8529559)
    3.  [users](#orgc043000)
6.  [Related Projects](#org38d568e)
7.  [Future](#org1384172)
8.  [Authors](#org500fa3d)
9.  [Acknowledgements](#org809ccd1)
10. [License](#orge4034d3)



<a id="org50fbf1d"></a>

# Introduction

Experience the full spectrum of connection: Chatsphere - Where every exchange is a visual symphony.
Experience seamless connections with the most secure and reliable messaging platform.Use ChatSphere to start and join conversations.

This is my personal messaging project that allows people to communicate with each other with ease. They can share simple messages and even images during a conversation. It is a simple but complex project that propelled me to learn about Software Engineering.


<a id="org6b717f6"></a>

# Getting Started

1.  Visit the ChatSphere page
2.  Create account or login using Oauth or with your custom credentials


<a id="org396b13a"></a>

# Screenshots

![img](./web_dynamic/static/images/avatars/conv.png "conversations")


<a id="org32f51f3"></a>

## conversation with text

![img](./web_dynamic/static/images/avatars/ju.png)


<a id="orge7f9dff"></a>

## conversation with images


<a id="org9729beb"></a>

# Technologies

-   Frontend: HTML, CSS, JQuery, JavaScript
-   Backend: Flask - (create dynamic web pages by serving HTML templates using Jinja2, Handle Restful API requests, connect to DB, perform CRUD operations, and implement authentication and authorization)
-   Storage: MySQL (version 5.7\*) and Redis; the latter for caching. SQLAlchemy as the ORM of choice.
-   Authentication and authorization: Oauth2(google<sub>auth</sub><sub>oauthlib</sub>, google.oauth2 libraries, etc.) and Flask sessions among others.


<a id="org1d4b586"></a>

# API

The frontend communicates with the backend storage via a Flask API. Various endpoints have been configured to suite the needs of the project. 


<a id="org0bb5db3"></a>

## messages

A conversation can only be between two or more participants. As such, it would be best to group messages by a conversation such that two participants interact with each other through a Conversation object containing such participants and their messages.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">HTTP Method</td>
<td class="org-left">Endpoint</td>
<td class="org-left">Purpose</td>
</tr>


<tr>
<td class="org-left">-----------</td>
<td class="org-left">-------------------------------------------------------------</td>
<td class="org-left">-----------------------------------</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>>/messages</td>
<td class="org-left">Retrieve list of all Message objects</td>
</tr>


<tr>
<td class="org-left">POST</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>>/messages</td>
<td class="org-left">Post a Message object</td>
</tr>


<tr>
<td class="org-left">DELETE</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>>/messages/<message<sub>id</sub>></td>
<td class="org-left">Delete a Message object</td>
</tr>


<tr>
<td class="org-left">POST</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>>/<sender<sub>id</sub>>/messages/file</td>
<td class="org-left">Post a Message object with file</td>
</tr>
</tbody>
</table>


<a id="org8529559"></a>

## conversations

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">HTTP Method</td>
<td class="org-left">Endpoint</td>
<td class="org-left">Purpose</td>
</tr>


<tr>
<td class="org-left">-----------</td>
<td class="org-left">------------------------------------------</td>
<td class="org-left">----------------------------------------------</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/users/conversations/<uder<sub>id</sub>></td>
<td class="org-left">Retrieve list of all Conversation objects</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/conversations/<user1<sub>id</sub>>/<user2<sub>id</sub>></td>
<td class="org-left">Retrieve a Conversation object by participants</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>></td>
<td class="org-left">Retrieve a Conversation object by id</td>
</tr>


<tr>
<td class="org-left">POST</td>
<td class="org-left">api/v1/conversations/</td>
<td class="org-left">Post a Conversation object</td>
</tr>


<tr>
<td class="org-left">DELETE</td>
<td class="org-left">api/v1/conversations/<conversation<sub>id</sub>></td>
<td class="org-left">Delete a Conversation object</td>
</tr>
</tbody>
</table>


<a id="orgc043000"></a>

## users

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">HTTP Method</td>
<td class="org-left">Endpoint</td>
<td class="org-left">Purpose</td>
</tr>


<tr>
<td class="org-left">-----------</td>
<td class="org-left">-------------------------------</td>
<td class="org-left">--------------------------------------</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/users</td>
<td class="org-left">Retrieve list of all User objects</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/users/<user<sub>id</sub>></td>
<td class="org-left">Retrieve a User object by user id</td>
</tr>


<tr>
<td class="org-left">GET</td>
<td class="org-left">api/v1/users/<user<sub>id</sub>>/image</td>
<td class="org-left">Retrieve a User object's profile image</td>
</tr>


<tr>
<td class="org-left">POST</td>
<td class="org-left">api/v1/users</td>
<td class="org-left">Post a User object</td>
</tr>


<tr>
<td class="org-left">PUT</td>
<td class="org-left">api/v1/users/<user<sub>id</sub>></td>
<td class="org-left">Update a User object</td>
</tr>


<tr>
<td class="org-left">PUT</td>
<td class="org-left">api/v1/users/<user<sub>id</sub>>/upload</td>
<td class="org-left">Update a User object's image</td>
</tr>


<tr>
<td class="org-left">DELETE</td>
<td class="org-left">api/v1/users/<user<sub>id</sub>></td>
<td class="org-left">Delete a User object</td>
</tr>
</tbody>
</table>


<a id="org38d568e"></a>

# Related Projects


<a id="org1384172"></a>

# Future


<a id="org500fa3d"></a>

# Authors

Francis Kamau is a skilled Software Engineer trained by ALX.
Feel free to reach out to Francis for any opportunities or collaborations.


<a id="org809ccd1"></a>

# Acknowledgements

-   ALX: Thanks Julien and ALX mentors for the opportunity to learn, upskill and do hard things at ALX. Much thanks to all peers for the support.
-   \#TeamEmacs: Who needs the hell of exiting Vim?


<a id="orge4034d3"></a>

# License

