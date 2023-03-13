<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<link rel="Stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%@ include file="menu.jsp"%>
<div class="jumbotron">
		<div class="container">
			<h1 class="display-4">아이디 찾기 결과 </h1>
		</div>
</div>
	<div class="container">
		<div class="row">
			<div class="col-md-2">
				<p>이름 </p>
				<p>아이디 </p>
			</div>
			<div class="col-md-4">
				<p>${name }</p>
				<p>${id }</p>
			</div>
		</div>
	</div>
<hr>
<%@ include file="footer.jsp"%>
</body>
</html>