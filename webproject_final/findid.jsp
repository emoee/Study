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
			<h1 class="display-4">아이디 찾기 </h1>
		</div>
</div>
	<div class="container">
		<form name ="find" action="MServlet" class ="form-horizontal">
			<div class="form-group row">
				<label class="col-sm-2">이름 </label>
				<div class ="col-sm-3">
					<input type="text" name="name" class ="form-control">
				</div> 
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">이메일 </label>
				<div class = "col-sm-5">
					<input type="email" name = "email" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<div class = "col-sm-offset-2 col-sm-10">
					<input type="submit" class="btn btn-primary" value="검색"
					style = "background-color:#59a1d0; border-color:#59a1d0;">
				</div>
			</div>
		</form>
	</div>
<hr>
<%@ include file="footer.jsp"%>
</body>
</html>