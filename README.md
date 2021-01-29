# PadelWatch

### Idea
Idea for PadelWatch came from the need for reservation slots for our friend group in the Padel venue in Vaasa.
Padel is quickly gaining popularity and it is common to have every evening timeslot reserved in the venue.
It became tiring to check different dates multiple times a day to see if there has been a cancellation and even then, you had to be fast to reserve the slot.
The app used for reserving slots, Playtomic, does not offer any "watch agent" type of functionality, I decided to create a software to do the checking and notify the user if a match has been cancelled.

### Design
For the purpose of keeping the project simple enough for my skills, I opted to create a Discord channel and bot. The bot has a command in which the user can specify the time period to watch and if a slot opens, the bot posts a notification to the channel. For example, the user can put a "Watch Agent" for "20.2-25.2 15.00-20.00" which checks matches inbetween 15.00-20.00 and from date 20.2 to 25.2. This way I did not have to create any applications for both Android and iOS (might be a future addition to this project when I have more time).

Matches are fetched with HTTP requests from Playtomic through their API every 10 minutes.
