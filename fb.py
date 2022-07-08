import requests

class FaceBook:
        def __init__(self,page_token,page_id):
            self.page_token = page_token
            self.page_id = page_id
            
        def postImage(self,img_url,msg,hashtags):
            post_url = 'https://graph.facebook.com/{}/photos'.format(self.page_id)
            payload = {
                #'url': img_url,
                'caption': msg+"\n"+hashtags,
    		'access_token': self.page_token
    		}
            files = {
                'file': open(img_url, 'rb')
            }
            r = requests.post(post_url, data=payload,files=files)
            print('--------Image posted to FaceBook--------')
            print(r.text)
            
        def postText(self,msg,hashtags):
        		post_url = 'https://graph.facebook.com/{}/feed'.format(self.page_id)
        		msg=msg+"\n"+hashtags
        		payload = {
        		'message': msg+"\n"+hashtags,
        		'access_token': self.page_token
        		}
        		r = requests.post(post_url, data=payload)
        		print('--------Text posted to FaceBook--------')
        		print(r.text) 
		
        def postvideo(self,video_url,msg,hashtags):
            post_url = 'https://graph.facebook.com/{}/videos'.format(self.page_id)
            payload = {
    		'caption': msg+"\n"+hashtags,
    		'access_token': self.page_token
    		}
            files = {
                'file': open(video_url, 'rb')
            }
            r = requests.post(post_url, data=payload,files=files)
            print('--------video posted to FaceBook--------')
            print(r.text)
            
        