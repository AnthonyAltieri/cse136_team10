<!doctype html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="style.css">
	<title>Delete a Bookmark</title>
</head>
<body>
  <div class="container">
	    <h2>Bookmarx</h2>
	    <p><b>Are you sure you want to delete this Bookmark?</b></p>
	    <p>Title :<i>Title of the selected bookmark in the previous page</i></p>
	    <p>URL :<i>URL of the selected bookmark</i></p>
	    <p>Keywords :<i>Keywords of the selected bookmark</i></p>
    <form id="delete-button-wrapper" style ="overflow:auto;"action="perform_delete.php" method="post">
    	<button type="submit" id="confirm_delete">Yes</button>
			<button type="button" onClick = "location.href='assignment2.html'"id="cancel_delete">No</button>
		</form>
  </div>
</body>
</html>
