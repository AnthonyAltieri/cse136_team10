<!doctype html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="style.css">
	<title>Edit a Bookmark</title>
</head>
<body>
  <div class="container">
		<form id = "edit-form">
			<h2>Bookmarx</h2>
			<p>Edit Bookmark </p>
			<input type="text" name="title" placeholder="title"><br>
			<input type="text" name="url" placeholder="URL"><br>
			<input type="text" name="keywords" placeholder="keywords"><br>
			<button type = "submit" id="confirm_edit">Edit</button>
			<button type = "button" id="cancel_edit" onClick="location.href='assignment2.html'">Cancel</button>
		</form>

  </div>
</body>
</html>