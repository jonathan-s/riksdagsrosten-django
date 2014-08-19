# Ongoing todo list

* Pagination for polls
* Mediaqueries
    - Individual view
    - Polls
    - Partywithname
* Auth - allauth
    - Decide what topics interest you
    - What you voted on the last election
    - Open or closed profile. -- what does it mean -- 
    - Allow friends?
    - Friend graph
    - Personalized homepage when logged in. 
    - A friend feed?
* Person view
    - Cache pictures on my server
    - Orm manager for MPs for 2014
* Polls
    - Create view for looking at poll data in detailed view. 
    - CSS for that. 
    - BUG: The polls might not always have doc_item 1, but have other polls that are done in that issue. How to know which is the first poll?
    - 2795162, 2827413 has many votes. 
* A model for aggregation of votes, easier to handle.
* Look at utskottsforslag and see if it's possible to regex out yrkande and nummer with the document and then parse that. To include a summary. 
* Get Celery working for processes with redis, for aggregation of votes for instance. 
* Caching


# CSS
whats the compatibility?
combine to one css for production
one normalize in pure, one normalize as css
votes -> maybe you dont need a span-element
maw-width for mp-wrapper
dont do breaks in title
responsive for mobile?
google analytics in the end and with an analytics-id
gradient buttons --> browser-support?

