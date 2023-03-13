<%@page import="java.io.PrintWriter"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
	<jsp:include page="/menu.jsp" />
	<div class="jumbotron">
		<div class="container">
			<h1 class="display-4">회원 정보</h1>
		</div>
	</div>
	<div class="container">
		<%
		String msg = request.getParameter("msg");
		
		if(msg != null){
			if (msg.equals("1")){
				PrintWriter o = response.getWriter();
				o.println("<script>alert('회원가입을 축하드립니다. 로그인해주세요.'); location.href='./login.jsp';</script> ");
				o.flush();
			}
			else if (msg.equals("2")){
				PrintWriter o = response.getWriter();
				o.println("<script>alert('환영합니다.'); location.href='./welcome.jsp';</script> ");
				o.flush();
			}
			else if (msg.equals("3")){
				PrintWriter o = response.getWriter();
				o.println("<script>alert('로그아웃 되었습니다.'); location.href='./welcome.jsp';</script> ");
				o.flush();
			}
		}
		%>
	</div>
</body>
</html>