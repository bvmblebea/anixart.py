# anixart.py
Mobile-API for [Anixart](https://anixart.tv) anime app
![](https://camo.githubusercontent.com/d58347a593ee46b517d6646929855af2536942d5e2e4984ad8f088da3f7292a4/68747470733a2f2f616e69786172742e74762f696d616765732f6c6f676f5f656d61696c2e706e67)

## Example

```python3
# Simple login.
import anixart
anix_client = anixart.AniXClient()
anix_client.login(login="email or login", password="password")
print(f"-- Account user_id::: {anix_client.user_id}")
```
