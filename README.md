
# Table of Contents

1.  [Introduction](#orgfb66184)
2.  [Getting Started](#orgf172c8d)
3.  [Screenshots](#org64d6ad5)
    1.  [conversation with text](#org926c6d7)
    2.  [conversation with images](#org2b21992)
4.  [Technologies](#org6cffdde)
5.  [API](#orge6554b4)
    1.  [messages](#org30c751e)
    2.  [conversations](#orga3285b5)
    3.  [users](#org6b3e927)
6.  [Related Projects](#org54fd1ec)
7.  [Future](#orgdcfc2a3)
8.  [Authors](#org6ced7c9)
9.  [Acknowledgements](#orgc0c568b)
10. [License](#org5677464)



<a id="orgfb66184"></a>

# Introduction

Experience the full spectrum of connection: Chatsphere - Where every exchange is a visual symphony.
Experience seamless connections with the most secure and reliable messaging platform.Use ChatSphere to start and join conversations.

This is my personal messaging project that allows people to communicate with each other with ease. They can share simple messages and even images during a conversation. It is a simple but complex project that propelled me to learn about Software Engineering.


<a id="orgf172c8d"></a>

# Getting Started

1.  Visit the [ChatSphere page](https://techinspire.tech/)
2.  Create account or login using Oauth or with your custom credentials


<a id="org64d6ad5"></a>

# Screenshots

![img](./web_dynamic/static/images/avatars/conv.png "conversations")


<a id="org926c6d7"></a>

## conversation with text

![img](./web_dynamic/static/images/avatars/ju.png)


<a id="org2b21992"></a>

## conversation with images


<a id="org6cffdde"></a>

# Technologies

-   Frontend: HTML, CSS, JQuery, JavaScript
-   Backend: Flask - (create dynamic web pages by serving HTML templates using Jinja2, Handle Restful API requests, connect to DB, perform CRUD operations, and implement authentication and authorization)
-   Storage: MySQL (version 5.7\*) and Redis; the latter for caching. SQLAlchemy as the ORM of choice.
-   Authentication and authorization: Oauth2(google<sub>auth</sub><sub>oauthlib</sub>, google.oauth2 libraries, etc.) and Flask sessions among others.


<a id="orge6554b4"></a>

# API

The frontend communicates with the backend storage via a Flask API. Various endpoints have been configured to suite the needs of the project. 


<a id="org30c751e"></a>

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


<a id="orga3285b5"></a>

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


<a id="org6b3e927"></a>

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


<a id="org54fd1ec"></a>

# Related Projects

-   [Star Wars Movie Guide](https://github.com/fk2019/Star_Wars_Movie_Guide)
-   [AirBnB Clone](https://github.com/fk2019/AirBnB_clone_v4)


<a id="orgdcfc2a3"></a>

# Future

-   Password reset feature
-   Furnish all pages in the frontend
-   DB replication


<a id="org6ced7c9"></a>

# Authors

[Francis Kamau](https://github.com/fk2019) is a skilled Software Engineer committed to quality and impactful products.
Feel free to reach out to Francis for any opportunities or collaborations.


<a id="orgc0c568b"></a>

# Acknowledgements

-   [ALX](https://www.alxafrica.com/): Thanks Julien and ALX mentors for the opportunity to learn, upskill and do hard things at ALX. Much thanks to all peers for the support.
-   \#TeamEmacs: Who needs the hell of exiting Vim?


<a id="org5677464"></a>

# License

