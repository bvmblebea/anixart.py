# anixart.py
Mobile-API for [Anixart](https://anixart.tv) anime app

## Example
```python3
# simple login
import anixart
anixclient = anixart.AniXClient()
anixclient.login(login="email or login", password="password")
print(f"-- Account user_id::: {anixclient.user_id}")
```
