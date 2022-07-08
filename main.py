from fb import FaceBook


print("Let Us post in Facebook...")
page_id=input("ENter Facebook Page_ID : ")
page_token=input("Enter Page Access TOken : ")
obj1=FaceBook(page_token,page_id)
print("<-------- Connected to Your Facebook Page -------->")
print("<---- Let us post a text Message ---->")
hashtags=input("ENter Hashtags : ")
obj1.postText(msg,hashtags)
print("\n<---- Let us post a Image ---->")
img_url=input("Enter Image url : ")
msg=input("Enter Caption : ")
hashtags=input("ENter Hashtags : ")
obj1.postImage(img_url,msg,hashtags)
