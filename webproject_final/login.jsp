<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="Stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<title>Insert title here</title>
</head>
<body>
<jsp:include page="./menu.jsp"/>
	<div class="jumbotron">
		<div class ="container">
			<h1 class = "display-4">로그인 </h1>
		</div>
	</div>
	<div class = "container">
		<div class="col-md-4 col-md-offset-4">
			<h3 class="form-signin-heading">Please sign in</h3>
			<%
				String error = request.getParameter("error");
				if (error != null) {
					out.println("<div class='alert alert-danger'>");
					out.println("아이디와 이름을 확인해주세요!");
					out.println("</div>");
				}
			%>
		<form name ="loginForm" action="./processlogin.jsp" class ="form-horizontal" method="post"
		enctype = "multipart/form-data" class="form-sign-in" >
			<div class="form-group row">
				<label class="col-md-3">아이디</label>
				<div class ="col-md-8">
					<input type="text" name="cid" class ="form-control" placeholder= "6자리 이하 숫자만 입력 가능" 
					oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" maxlength="6">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-md-3">이름 </label>
				<div class = "col-md-8">
					<input type="text" name = "cname" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<div class = "col-sm-offset-2 col-sm-10">
					<input type="submit" class="btn btn-primary" value="로그인"
					style = "background-color:#59a1d0; border-color:#59a1d0;">
				</div>
			</div>
		</form>
		</div>
	</div>
</body>
</html>