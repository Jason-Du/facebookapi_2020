![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_d4509ad99b8a6347c33ce990f67a7571.jpg)

# Facebook API

## Insallation
- 移動到你要工作的資料夾打開 git bash
```shell=
$ git clone https://playlab.computing.ncku.edu.tw:4001/khduh/facebook_api_file.git
```
***

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_147003c5e7b1df138f1de6c93df821eb.png)
- **package you need to install**
    - google-api-python-client
    - oauth2client


***
![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_5c367b466f7ab106e09427d45ea300ce.png)


***
- **設定引用library**

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_e0ae3a01768edf468a5ab44a89e60b35.png)


- **測試**

***

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_036fd11dbee4868765c1fc8514fbda0a.png)

***


![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_2b327297eea4f1474d74cc4233ca6764.png)




## Function List
- **get  會回傳想要的資訊**
- **show 只列印出值 不回傳**
- 
## 建議事項
- **若你對json檔格式熟悉者 僅須使用第一個函示庫 即可得到社團上的參與度資料檔 並自行分析得到自己想要的資訊**
- **若你對如何處理資料不太熟悉 可以參考API中函式庫提取資訊的寫法 這樣對日後的project想要提取自己想要的資訊 EMOJI COMMENT CONTENT.......會有較大的幫助**
***
### 1. **function 說明 : 下載google cloud 上的 json檔 到本機電腦**
- 引數 date 輸入日期可以得到對應日期的社團資訊 從 9/29 開始皆有檔案 輸入格式參考如下
```python=
get_json_from_cloud(date)
```
- **範例 取9/29 社團資訊**
```python=
get_json_from_cloud(date="0929")

```


- >**回傳 一個DICT 的dataset**
- >**dict的架構如下**
```python=
{
	'post_info':[{
			'poster': '',
			'post_content': '',
			'post_share_link': [],
			'comment_number': '',
			'reaction':[{'emoji_id': '',
					  'emoji_type': ''
					  }],
			'comment':[{
						'comment_id': '',
						'comment_content': '',
						'comment_link_num': '',
						'comment_gif_num': '',
						'comment_img_num': '',
						'comment_sticker': '',
						'comment_below':[comment_below_dict = {'comment_id':'',
											  'co mment_content':'',
											  'comment_link_num':'',
											  'comment_gif_num':'',
											  'comment_img_num':'',
											  'comment_sticker':'',
											  'comment_reaction':[emoji_dict ={'emoji_id': '',  'emoji_type': '' }]}]}],
			
					  
						'comment_reaction': [{'emoji_id': '', 'emoji_type': ''  }]
				}]
	'member_info'=[]
}
```
- >**使用範例**
```python=
dataset = get_json_from_cloud()
```

***


### 2. **function 說明 : 列印出所有貼文的資訊**
- > **會先列出post 的 id 再列出該PO文的資訊**
```python=
show_all_post(dataset):
```
- >**使用範例**
```python=
show_all_post(dataset)
```
- >**RESUT**
![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_d74cb6fbfce1a57de1decf6d5bbe67bd.png)



***


### 3. **function 說明 : 回傳所有貼文資訊**
- > **引數 post id** **dataset**   
- > **dataset引數放置前面從雲端抓到的dataset**
- > > **會回傳對應 post 的 PO 文資訊**
- > > **回傳 一個 dict 的PO 文資訊**
```python=
get_post_by_post_id(dataset,post_id)
```
- >**使用範例  回傳POSTID=2的PO文資訊**
```python=
dataset = get_json_from_cloud()
single_post_info=get_post_by_post_id(dataset=dataset,post_id=2)
```



***


### 4. **function 說明 : 回傳社團社員名單**
- > **dataset引數放置前面從雲端抓到的dataset**
- > > **回傳 一個l ist 的PO 文資訊**
```python=
get_user_id(dataset):
```
- >**使用範例  回傳社團社員名單 為一個list*
```python=
dataset = get_json_from_cloud()
get_user_id(dataset=dataset)

```


***


### 5. **function 說明 : 列印對應PO文下的comment名單**
- > **dataset引數放置前面從雲端抓到的dataset**
- > **列印出PO文ID COMMENT ID 再列印出COMMENT 內容**
```python=
show_all_comments_by_post_id(dataset, post_id):
```
- >**使用範例**
```python=
dataset = get_json_from_cloud()
show_all_comments_by_post_id(dataset=dataset,post_id=3)
```
- >**RESUT**
![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_6bd82f13afa943bb3b4c8655d13089fd.png)

***

### 其他FUNCTION


- 列印出 貼文編號為POST ID 下 貼文編號為comment id的資訊
```python=
show_all_comments_below_by_post_id_comment_id(dataset, post_id, comment_id)
```


***

- 回傳一個LIST 紀錄了  貼文編號為POST ID 下 貼文編號為comment id的資訊
```python=
get_comment_by_post_id_comment_id(dataset, post_id,omment_id):
```

***

- 回傳一個dict 
- 貼文編號為POST ID 下 貼文編號為comment id 下的回覆留言編號標號為 comment_below_id 的資訊
```python=
get_comment_below_by_post_id_comment_id_comment_below_id(dataset, post_id, comment_id, comment_below_id):
```














