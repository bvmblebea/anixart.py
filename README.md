<body>
	<div>
		<h1 align="center"> anixart.py </h1>
		<img src="https://anixart.tv/images/logo.svg">
		Mobile-API for <a href="https://anixart.tv"> Anixart </a> anime app 
	</div>
	<br>
	<div>
		<h3 align="center"> Example: </h3>
		<pre>
import anixart
anixclient = anixart.AniXClient()
anixclient.login(login="email or login", password="password")
print(f"-- Account user_id::: {anixclient.user_id}")
		</pre>
	</div>
</body>
