# Zettelkasten Webserver

This is a project to create a server to add analytics to my Zettelkasten. I created a private project to manage my
own readings and thoughts about my research activities. The idea is based on the essay by Niklas Luhmann:
[Kommunikation mit Zettelkästen](https://ckrybus.com/static/papers/luhmann1981.pdf). I have organised my Zettel in a
directory structure, where each directory is named by the date the Zettel was created. Every Zettel is
written in md, so you can link any Zettel to any other. There is a separate directory for the meta categories. So
each Zettel can be tagged by several topics.

This project gives me the freedom to create a new perspective to my Zettelkasten. Following tasks should be fulfilled
with this project:
* [ ] Add the Zettelkasten directory to this project
* [ ] Show a random Zettel on the startup page
* [ ] After choosing a category all Zettel should be visible in a scrollable timeline
* [ ] dockerize everything

This server is based on [Django](https://www.djangoproject.com/)