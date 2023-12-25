
# Table of Contents

1.  [Introduction](#org07e530e)
2.  [Getting Started](#orgdca0e39)
3.  [Screenshots](#org6e97342)
4.  [Technologies](#orga3d11aa)
5.  [API](#orgddfecfb)
    1.  [messages](#orga0dc3b3)
    2.  [conversations](#org172a840)
    3.  [users](#orgbdd8b4d)
6.  [Related Projects](#org23ef06f)
7.  [Future](#org3397f9a)
8.  [Authors](#org864f8d3)
9.  [Acknowledgements](#org7b1b978)
10. [License](#org24ab9f0)



<a id="org07e530e"></a>

# Introduction

Experience the full spectrum of connection: Chatsphere - Where every exchange is a visual symphony.
Experience seamless connections with the most secure and reliable messaging platform.Use ChatSphere to start and join conversations.

This is my personal messaging project that allows people to communicate with each other with ease. They can share simple messages and even images during a conversation. It is a simple but complex project that propelled me to learn about Software Engineering.


<a id="orgdca0e39"></a>

# Getting Started

1.  Visit the ChatSphere page
2.  Create account or login using Oauth or with your custom credentials


<a id="org6e97342"></a>

# Screenshots


<a id="orga3d11aa"></a>

# Technologies

-   Frontend: HTML, CSS, JQuery, JavaScript
-   Backend: Flask - (create dynamic web pages by serving HTML templates using Jinja2, Handle Restful API requests, connect to DB, perform CRUD operations, and implement authentication and authorization)
-   Storage: MySQL (version 5.7\*) and Redis; the latter for caching. SQLAlchemy as the ORM of choice.
-   Authentication and authorization: Oauth2(google<sub>auth</sub><sub>oauthlib</sub>, google.oauth2 libraries, etc.) and Flask sessions among others.


<a id="orgddfecfb"></a>

# API

The frontend communicates with the backend storage via a Flask API. Various endpoints have been configured to suite the needs of the project. 


<a id="orga0dc3b3"></a>

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


<a id="org172a840"></a>

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


<a id="orgbdd8b4d"></a>

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


<a id="org23ef06f"></a>

# Related Projects


<a id="org3397f9a"></a>

# Future


<a id="org864f8d3"></a>

# Authors

Francis Kamau is a skilled Software Engineer trained by ALX.
Feel free to reach out to Francis for any opportunities or collaborations.


<a id="org7b1b978"></a>

# Acknowledgements

-   ALX: Thanks Julien and ALX mentors for the opportunity to learn, upskill and do hard things at ALX. Much thanks to all peers for the support.
-   \#TeamEmacs: Who needs the hell of exiting Vim?


<a id="org24ab9f0"></a>

# License

