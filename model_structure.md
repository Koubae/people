#### TODO: Add Django Default Admin/Auth models 

* account
* Likes
* Comment
* Post
* Image
* Video
* setting 

* Connection 
* Group
* Events
* Contacts <- not yet.


### Relations ships

* (one-to-many) account_post: account <-- post,post,post
* (one-to-many) account_media image|video: account <-- image,video,image,video
* (one-to-many) media_like_account: media image|video <-- account,like
* (one-to-one) account_setting: account <-> setting (maybe a json object???)

##### Likes - Comments

* (one-to-many) post_like_account: post <-- account,like
* (one-to-many) post_comment_account: post <-- account,comment

* (many-to-many) connection_account_account: account <--> account
* (one-to-many)  connection_group_account: group <-- account,account,account
* (one-to-many)  connection: event <-- group,group,account,account

### Notes


* I think media (image and video) should be really just a sub-type of a post
* post is a 'base class' or an 'object' that can be visible/not visble to others and can be 'reactable'
  * Maybe the subtype or 'mixin' can be a 'ReactMixin' where someone or some entity can react (so give comment, like and so on.. )
