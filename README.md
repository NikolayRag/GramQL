# GramQL

is a GraphQL library which uses Telegram as a storage engine.

## Idea

is to store entries as separate messages in specific chat, group or channel.


### Technical issues.

Since TG bots bont have direct access to messages by demand,
specific message is picked by making a reply to it.

