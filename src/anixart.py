import requests

class Anixart:
	def __init__(self, proxies: dict = None) -> None:
		self.api = "https://api.anixart.tv"
		self.headers = {
			"User-Agent": "AnixartApp/8.0-22050323 (Android 7.1.2; SDK 25; x86; samsung SM-N975F; ru)",
			"Connection": "Keep-Alive",
			"Accept-Encoding": "gzip",
			"Content-Type": "application/json"
		}
		self.token = None
		self.user_id = None
		self.proxies = proxies

	def login(
			self,
			login: str,
			password: str) -> dict:
		data = {
			"login": login,
			"password": password
		}
		response = requests.post(
			f"{self.api}/auth/signIn",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
		if "profile" in response:
			self.token = response["profileToken"]["token"]
			self.user_id = response["profile"]["id"]
		return response

	def register(
			self,
			email: str,
			password: str,
			login: str) -> dict:
		data = {
			"login": login,
			"email": email,
			"password": password
		}
		return requests.post(
			f"{self.api}/auth/signUp",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def verify_registration(
			self,
			email: str,
			password: str,
			login: str,
			code: int,
			hash: str) -> dict:
		data = {
			"login": login,
			"email": email,
			"password": password,
			"code": code,
			"hash": hash
		}
		return requests.post(
			f"{self.api}/auth/verify",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
			
	def get_login_firebase(self) -> dict:
		return requests.post(
			f"{self.api}/auth/firebase?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_schedule(self) -> dict:
		return requests.get(
			f"{self.api}/schedule?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
		
	def get_user_info(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/profile/{user_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()

	def get_user_nickname_history(self, user_id: int, page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/profile/login/history/all{user_id}/{page}",
			headers=self.headers,
			proxies=self.proxies).json()
			
	def get_blocklist(self, page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/profile/blocklist/all/{page}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def block_user(self, user_id: int) -> dict:
		return requests.post(
			f"{self.api}/profile/blocklist/add/{user_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def unblock_user(self, user_id: int) -> dict:
		return requests.post(
			f"{self.api}/profile/blocklist/remove/{user_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_user_voted_releases(
			self,
			user_id: int,
			sort: int = 1,
			page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/profile/vote/release/voted/{user_id}/{page}?sort={sort}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_user_unvoted_releases(
			self,
			user_id: int,
			sort: int = 1,
			page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/profile/vote/release/unvoted/{user_id}/{page}?sort={sort}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_all_type_of_sounds(self) -> dict:
		return requests.get(
			f"{self.api}/type/all?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_user_friends(
			self,
			user_id: int,
			page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/all/{user_id}/{page}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def edit_profile_status(self, status: str) -> dict:
		data = {
			"status": status
		}
		return requests.post(
			f"{self.api}/profile/preference/status/edit?token={self.token}",
			json=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def edit_profile_social(
			self,
			instagram: str = None,
			telegram: str = None,
			vkontakte: str = None,
			tiktok: str = None,
			discord: str = None) -> dict:
		data = {}
		if instagram:
			data["instPage"] = instagram
		if telegram:
			data["tgPage"] = telegram
		if vkontakte:
			data["vkPage"] = vkontakte
		if tiktok:
			data["ttPage"] = tiktok
		if discord:
			data["discordPage"] = discord
		return requests.post(
			f"{self.api}/profile/preference/social/edit?token={self.token}",
			json=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def send_comment(
			self,
			message: str,
			release_id: int = None,
			collection_id: int = None,
			parent_comment_id: str = None,
			replyTo: str = None,
			spoiler: bool = False) -> dict:
		data = {
			"message": message,
			"parentCommentId": parent_comment_id,
			"replyToProfileId": replyTo,
			"spoiler": spoiler
		}
		if release_id:
			url = f"{self.api}/release/comment/add/{release_id}?token={self.token}"
		elif collection_id:
			url = f"{self.api}/collection/comment/add/{collection_id}?token={self.token}"
		return requests.post(
			url,
			json=data, 
			headers=self.headers,
			proxies=self.proxies).json()
	
	def edit_comment(
			self,
			message: str,
			release_comment_id: int = None,
			collection_comment_id: int = None,
			spoiler: bool = False) -> dict:
		data = {
			"message": message,
			"spoiler": spoiler
		}
		if release_comment_id:
			url = f"{self.api}/release/comment/edit/{release_comment_id}?token={self.token}"
		elif collection_comment_id:
			url = f"{self.api}/collection/comment/edit/{collection_comment_id}?token={self.token}"
		return requests.post(
			url,
			json=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_random_release(self, extended_mode: bool = True) -> dict:
		return requests.get(
			f"{self.api}/release/random?extended_mode={extended_mode}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_collection_list(self, page: int = 0) -> dict:
		return requests.get(
			f"{self.api}/collection/all/{page}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_release_info(
			self,
			release_id: int,
			extended_mode: bool = True) -> dict:
		return requests.get(
			f"{self.api}/release/{release_id}?extended_mode={extended_mode}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_release_comments(
			self,
			release_id: int,
			page: int = 0,
			sort: int = 0) -> dict:
		return requests.get(
			f"{self.api}/release/comment/all/{release_id}/{page}?sort={sort}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def get_notification_count(self) -> dict:
		return requests.get(
			f"{self.api}/notification/count?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def vote_release(
			self,
			release_id: int,
			star: int) -> dict:
		return requests.get(
			f"{self.api}/release/vote/add/{release_id}/{star}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def add_into_profile_list(
			self,
			release_id: int,
			status: int = 3) -> dict:
		return requests.get(
			f"{self.api}/profile/list/add/{status}/{release_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def delete_from_profile_list(
			self,
			release_id: int,
			status: int = 3) -> dict:
		return requests.get(
			f"{self.api}/profile/list/delete/{status}/{release_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def add_release_to_favorite(self, release_id: int) -> dict:
		return requests.get(
			f"{self.api}/favorite/add/{release_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def delete_release_from_favorite(self, release_id: int) -> dict:
		return requests.get(
			f"{self.api}/favorite/delete/{release_id}?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def report_release(
			self,
			release_id: int,
			message: str,
			reason: int) -> dict:
		"""
		RELEASE-REPORT REASON-TYPES:
			1 - MISTAKE IN DESIGN,
			2 - MISSING SOME SERIES,
			3 - OTHER
		"""
		data = {
			"message": message,
			"reason": reason
		}
		return requests.post(
			f"{self.api}/release/report/{release_id}?token={self.token}",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def report_release_comment(
			self,
			comment_id: int,
			message: str,
			reason: int) -> dict:
		"""
		COMMENT-REPORT REASON-TYPES:
			1 - SPAM,
			2 - INSULTS,
			3 - HARASSMENT,
			4 - SPOILER,
			5 - OTHER
		"""
		data = {
			"message": message,
			"reason": reason
		}
		return requests.post(
			f"{self.api}/release/comment/report/{comment_id}?token={self.token}",
			data=data,
			headers=self.headers, proxies=self.proxies).json()
	
	def get_release_comment_votes(
			self,
			comment_id: int,
			page: int = 0,
			sort: int = 0) -> dict:
		return requests.get(
			f"{self.api}/release/comment/votes/{comment_id}/{page}?sort={sort}&token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def send_friend_request(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/request/send/{user_id}?token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def remove_friend_request(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/request/remove/{user_id}?token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def get_user_profile_list(self, user_id: int, page: int = 1, sort=1) -> dict:
		return requests.get(
			f"{self.api}/profile/list/all/{user_id}/{page}/0?sort={sort}&token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def get_login_info(self) -> dict:
		return requests.get(
			f"{self.api}/profile/preference/login/info?token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def change_login(self, login: str) -> dict:
		return requests.post(
			f"{self.api}/profile/preference/login/change?login={login}&token={self.token}",
			headers=self.headers, proxies=self.proxies).json()
	
	def bind_social_to_profile(
			self,
			vk_access_token: str = None,
			google_id_token: str = None) -> dict:
		data = {}
		if vk_access_token:
			data["accessToken"] = vk_access_token
			url = f"{self.api}/profile/preference/vk/bind?token={self.token}"
		if google_id_token:
			data["idToken"] = google_id_token
			url = f"{self.api}/profile/preference/google/bind?token={self.token}"
		return requests.post(
			url,
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def change_password(self, current_password: str, new_password: str) -> dict:
		return requests.get(
			f"{self.api}/profile/preference/password/change?current={current_password}&new={new_password}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def change_email(self, current_email: str, new_email: str, password: str) -> dict:
		return requests.get(
			f"{self.api}/profile/preference/email/change?current_password={password}&current={current_email}&new={new_email}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def search_release(self, query: str) -> dict:
		data = {
			"query": query,
			"searchBy": 0
		}
		return requests.post(
			f"{self.api}/search/releases/0?token={self.token}",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()
	
	def discover_interesting(self) -> dict:
		return requests.post(
			f"{self.api}/discover/interesting",
			headers=self.headers,
			proxies=self.proxies).json()
           
	def discover_comments(self) -> dict:
		return requests.post(
			f"{self.api}/discover/comments",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def discover_discussing(self) -> dict:
		return requests.post(
			f"{self.api}/discover/discussing?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()

	def discover_collections(self) -> dict:
		return requests.post(
			f"{self.api}/discover/comments",
			headers=self.headers,
			proxies=self.proxies).json()
	
	def search_profile(self, query: str) -> dict:
		data = {
			"query": query,
			"searchBy": 0
		}
		return requests.post(
			f"{self.api}/search/profiles/0?token={self.token}",
			data=data,
			headers=self.headers,
			proxies=self.proxies).json()

	def get_friend_requests(self) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/requests/in/last?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()

	def get_sent_friend_requests(self) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/requests/out/last?token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()

	def get_friend_recommendations(self) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/recommendations?token={self.token}", 
			headers=self.headers,
			proxies=self.proxies).json()

	def accept_friend_request(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/profile/friend/request/send/{user_id}?token={self.token}", 
			headers=self.headers,
			proxies=self.proxies).json()

	def get_user_comments(
			self,
			user_id: int,
			page: int = 0,
			sort: int = 0) -> dict:
		return requests.get(
			f"{self.api}/release/comment/all/profile/{user_id}/{page}?sort={sort}&token={self.token}",
			headers=self.headers,
			proxies=self.proxies).json()
