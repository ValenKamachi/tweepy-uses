import tweepy
import json
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="WWSqxwKvqIAhizLlngOgFHfBQUU"
consumer_secret="LL9wgKZ1b33y4jBIn3KAN2HUWNhbpe5d6HVVwqpRz7NLdDGUDPxx"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="22422233770-tgNDtayNpq1aYcgjJaXMBQtcbwROVERESgvOfqJJ"
access_token_secret="WWF0kGhDXYNdLvzeW56WaPn7GO2XErffgRJj6e9Q9p3HO22"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
user = api.update_with_media('aa.png','Hi')
print (user)

user1 = api.me()
 
print('Name: ' + user1.name)
print('Location: ' + user1.location)
print('Friends: ' + str(user1.friends_count))


user2 = api.update_profile_image('960.jpg')
print (user2)
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status(status='Updating using OAuth authentication via Tweepy!')
#tweepy.SetDescription("Howdy")

print user._json
