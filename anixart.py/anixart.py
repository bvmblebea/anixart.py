import enum
from typing import NoReturn

import requests


class AnixAPIURLs(enum.Enum):
    """
    API_URL: This is normal API_URL.
    API_URL_ALTERNATIVE: API_URL for ukraine.
    """

    API_URL = "https://api.anixart.tv"
    API_URL_ALTERNATIVE = "https://api-s2.anixart.tv/"


class AnixClient:
    def __init__(self, API_URL: AnixAPIURLs = AnixAPIURLs.API_URL):
        self.API_URL = API_URL
        self.headers = {
            "User-Agent": "AnixartApp/7.9.2-21121202 (Android 7.1.2; SDK 25; x86; samsung SM-N975F; ru)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"}
        self.token: str = str()
        self.user_id: int = 0

    def login(self, login: str, password: str) -> NoReturn:
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(
            f"{self.API_URL}/auth/signIn",
            data=data,
            headers=self.headers).json()

        self.token = response["profileToken"]["token"]
        self.user_id = response["profileToken"]["id"]

    def register(self,
                 email: str,
                 password: str,
                 login: str):
        data = {
            "login": login,
            "email": email,
            "password": password
        }
        return requests.post(
            f"{self.API_URL}/auth/signUp",
            data=data,
            headers=self.headers).json()

    def verify_registration(self,
                            email: str,
                            password: str,
                            login: str,
                            code: int,
                            hash_code: str) -> dict:
        data = {
                   "login": login,
                   "email": email,
                   "password": password,
                   "code": code,
                   "hash": hash_code
               },
        return requests.post(
            f"{self.API_URL}/auth/verify",
            data=data,
            headers=self.headers).json()

    def get_schedule(self) -> dict:
        return requests.get(
            f"{self.API_URL}/schedule?token={self.token}",
            headers=self.headers).json()

    def get_user_info(self, user_id: int) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/{user_id}?token={self.token}",
            headers=self.headers).json()

    def get_user_nickname_history(self, user_id: int, page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/login/history/all{user_id}/{page}",
            headers=self.headers).json()

    def get_blocklist(self, page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/blocklist/all/{page}?token={self.token}",
            headers=self.headers).json()

    def block_user(self, user_id: int) -> dict:
        return requests.post(
            f"{self.API_URL}/profile/blocklist/add/{user_id}?token={self.token}",
            headers=self.headers).json()

    def unblock_user(self, user_id: int) -> dict:
        return requests.post(
            f"{self.API_URL}/profile/blocklist/remove/{user_id}?token={self.token}",
            headers=self.headers).json()

    def get_user_voted_releases(
            self,
            user_id: int,
            sort: int = 1,
            page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/vote/release/voted/{user_id}/{page}?sort={sort}&token={self.token}",
            headers=self.headers).json()

    def get_user_unvoted_releases(
            self,
            user_id: int,
            sort: int = 1,
            page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/vote/release/unvoted/{user_id}/{page}?sort={sort}&token={self.token}",
            headers=self.headers).json()

    def get_all_type_of_sounds(self) -> dict:
        return requests.get(
            f"{self.API_URL}/type/all?token={self.token}",
            headers=self.headers).json()

    def get_user_friends(self, user_id: int, page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/friend/all/{user_id}/{page}?token={self.token}",
            headers=self.headers).json()

    def edit_profile_status(self, status: str) -> dict:
        data = {"status": status}
        return requests.post(
            f"{self.API_URL}/profile/preference/status/edit?token={self.token}",
            json=data,
            headers=self.headers).json()

    def edit_profile_social(
            self,
            instagram: str = None,
            telegram: str = None,
            vk: str = None,
            tiktok: str = None) -> dict:
        data = {}
        if instagram:
            data["instPage"] = instagram
        elif telegram:
            data["tgPage"] = telegram
        elif vk:
            data["vkPage"] = vk
        elif tiktok:
            data["ttPage"] = tiktok
        return requests.post(
            f"{self.API_URL}/profile/preference/social/edit?token={self.token}",
            json=data,
            headers=self.headers).json()

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
            request_url = f"{self.API_URL}/release/comment/add/{release_id}?token={self.token}"
        elif collection_id:
            request_url = f"{self.API_URL}/collection/comment/add/{collection_id}?token={self.token}"
        else:
            raise ValueError("Can't find release_id or collection_id.")
        return requests.post(
            request_url,
            json=data,
            headers=self.headers).json()

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
            request_url = f"{self.API_URL}/release/comment/edit/{release_comment_id}?token={self.token}"
        elif collection_comment_id:
            request_url = f"{self.API_URL}/collection/comment/edit/{collection_comment_id}?token={self.token}"
        else:
            raise ValueError("Can't find release_comment_id or collection_comment_id.")
        return requests.post(
            request_url,
            json=data,
            headers=self.headers).json()

    def get_random_release(self, extended_mode: bool = True) -> dict:
        return requests.get(
            f"{self.API_URL}/release/random?extended_mode={extended_mode}&token={self.token}",
            headers=self.headers).json()

    def get_collection_list(self, page: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/collection/all/{page}?token={self.token}",
            headers=self.headers).json()

    def get_release_info(self, release_id: int, extended_mode: bool = True) -> dict:
        return requests.get(
            f"{self.API_URL}/release/{release_id}?extended_mode={extended_mode}&token={self.token}",
            headers=self.headers).json()

    def get_release_comments(
            self,
            release_id: int,
            page: int = 0,
            sort: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/release/comment/all/{release_id}/{page}?sort={sort}&token={self.token}",
            headers=self.headers).json()

    def get_notification_count(self) -> dict:
        return requests.get(
            f"{self.API_URL}/notification/count?token={self.token}",
            headers=self.headers).json()

    def vote_release(self, release_id: int, star: int = 5) -> dict:
        return requests.get(
            f"{self.API_URL}/release/vote/add/{release_id}/{star}?token={self.token}",
            headers=self.headers).json()

    def add_into_profile_list(self, release_id: int, status: int = 3) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/list/add/{status}/{release_id}?token={self.token}",
            headers=self.headers).json()

    def delete_from_profile_list(self, release_id: int, status: int = 3) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/list/delete/{status}/{release_id}?token={self.token}",
            headers=self.headers).json()

    def add_release_to_favorite(self, release_id: int) -> dict:
        return requests.get(
            f"{self.API_URL}/favorite/add/{release_id}?token={self.token}",
            headers=self.headers).json()

    def delete_release_from_favorite(self, release_id: int) -> dict:
        return requests.get(
            f"{self.API_URL}/favorite/delete/{release_id}?token={self.token}",
            headers=self.headers).json()

    # reasons: 1 = error in design, 2 = missing series. 3 = other
    def report_release(self, release_id: int, message: str, reason: int = 3) -> dict:
        data = {
            "message": message,
            "reason": reason
        }
        return requests.post(
            f"{self.API_URL}/release/report/{release_id}?token={self.token}",
            data=data,
            headers=self.headers).json()

    # reasons: 1 = spam, 2 = insults, 3 = call for harassment, 4 = spoiler, 5
    # = other
    def report_release_comment(
            self,
            comment_id: int,
            message: str,
            reason: int = 5) -> dict:
        data = {
            "message": message,
            "reason": reason
        }
        return requests.post(
            f"{self.API_URL}/release/comment/report/{comment_id}?token={self.token}",
            data=data,
            headers=self.headers).json()

    def get_release_comment_votes(
            self,
            comment_id: int,
            page: int = 0,
            sort: int = 0) -> dict:
        return requests.get(
            f"{self.API_URL}/release/comment/votes/{comment_id}/{page}?sort={sort}&token={self.token}",
            headers=self.headers).json()

    def send_friend_request(self, user_id: int) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/friend/request/send/{user_id}?token={self.token}",
            headers=self.headers).json()

    def remove_friend_request(self, user_id: int) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/friend/request/remove/{user_id}?token={self.token}",
            headers=self.headers).json()

    def get_user_profile_list(self, user_id: int, page: int = 1, sort: int = 1) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/list/all/{user_id}/{page}/0?sort={sort}&token={self.token}",
            headers=self.headers).json()

    def get_login_info(self) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/preference/login/info?token={self.token}",
            headers=self.headers).json()

    def change_login(self, login: str) -> dict:
        return requests.post(
            f"{self.API_URL}/profile/preference/login/change?login={login}&token={self.token}",
            headers=self.headers).json()

    def bind_social_to_profile(
            self,
            vk_accessToken: str = None,
            google_idToken: str = None) -> dict:
        data = {}
        if vk_accessToken:
            data["accessToken"] = vk_accessToken
            request_url = f"{self.API_URL}/profile/preference/vk/bind?token={self.token}"
        elif google_idToken:
            data["idToken"] = google_idToken
            request_url = f"{self.API_URL}/profile/preference/google/bind?token={self.token}"
        else:
            raise ValueError("Can't find google_idToken or vk_accessToken.")
        return requests.post(
            request_url,
            data=data,
            headers=self.headers).json()

    def change_password(self, current_password: str, new_password: str) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/preference/password/change?current={current_password}&new={new_password}"
            f"&token={self.token}",
            headers=self.headers).json()

    def change_email(self, current_email: str, new_email: str, password: str) -> dict:
        return requests.get(
            f"{self.API_URL}/profile/preference/email/change?current_password={password}&current={current_email}"
            f"&new={new_email}&token={self.token}",
            headers=self.headers).json()

    def search_release(self, query: str) -> dict:
        data = {
            "query": query,
            "searchBy": 0
        }
        return requests.post(
            f"{self.API_URL}/search/releases/0?token={self.token}",
            data=data,
            headers=self.headers).json()

    def discover_interesting(self) -> dict:
        return requests.post(
            f"{self.API_URL}/discover/interesting",
            headers=self.headers).json()

    def discover_comments(self) -> dict:
        return requests.post(
            f"{self.API_URL}/discover/comments",
            headers=self.headers).json()

    def discover_discussing(self) -> dict:
        return requests.post(
            f"{self.API_URL}/discover/discussing?token={self.token}",
            headers=self.headers).json()

    def discover_collections(self) -> dict:
        return requests.post(
            f"{self.API_URL}/discover/comments",
            headers=self.headers).json()

    def search_profile(self, query: str) -> dict:
        data = {
            "query": query,
            "searchBy": 0
        }
        return requests.post(
            f"{self.API_URL}/search/profiles/0?token={self.token}",
            data=data,
            headers=self.headers).json()
