class TwitterThread(threading.Thread):
              def __init__(self, consumer_key, consumer_secret):
                  self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

              def authorization(self, access_token, access_secret):
                     self.authorize = self.auth.set_access_token(access_token, access_secret)
              def api(self):
                api = API(self.auth)
                threading.Thread.__init__(self, name="API-Thread-For-%s"%(api))
              def collect_followers(self):
                  all_my_followers = None #self.api Non
                  #logic will soon appear in here
              def run(self):
                self.lock = threading.Lock()
                with self.lock:
                    logging.info("Acquiring and disabling lock for user")
                    return
