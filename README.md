Social media platform for hireing and searching for musicians. LinkedIn for musicians. Built using Python, Django and SQLite. Current version does not include frontend. Still in early stages - it's a project I'm currently working on.


USED TECHNOLOGIES:
- Pyhton & Django
- SQLite3 database
- No frontend in current version of application.


FUNCTIONALITIES:
- Systems of user accounts. Additional models associated with account in M2M relatioship describing user properties like instruments, generes, preffered forms of cooperation and more.
- System of posts, comments and their replies. Author of post/comment/reply can edit published contents. Any user is able to publish posts, comments and replies on them. Comments live in FK relationship with themselves to establish ancestors (comment/reply).
- Contact us page connected to mailer.
- Musician search system by instruments, generes, forms of cooperation, location and pricings on it's way.
- I'm currently working on unit tests of everything I made so far.
