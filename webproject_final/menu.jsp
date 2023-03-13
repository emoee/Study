<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<% 
	request.setCharacterEncoding("UTF-8"); 
	String sessionId = (String)session.getAttribute("sessionId");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href = "cssstyle.css" >
<title>Insert title here</title>
</head>
<body>
<nav class="navbar navbar-expand navbar-dark bg-dark">
	<div class="container">
		<div class="navbar-header">
			<a class="navbar-brand" href="./welcome.jsp">Home</a>
			<a class="navbar-brand" href="./stores.jsp">Store</a>
			<a class="navbar-brand" href="./addStore.jsp">Add Store</a>
			<a class="navbar-brand" href="./addmenu.jsp">Add Menu</a>
			<a class="navbar-brand" href="./check.jsp">Check</a>
		</div>
	<ul class="nav navbar-nav navbar-right">
	<% String loginName = (String)session.getAttribute("sessionName");%>
		<c:choose>
			<c:when test="${empty sessionId}">
				<li style="list-style:none; font-size:18px; padding:0px 15px 0px 0px;">
				<a href="<c:url value="./findid.jsp" />">아이디 찾기</a></li>
				<li style="list-style:none; font-size:18px; padding:0px 15px 0px 0px;">
				<a href="<c:url value="./login.jsp" />">로그인</a></li>
				<li style="list-style:none; font-size:18px; padding:0px 15px 0px 0px;">
				<a href="<c:url value="./join.jsp" />">회원가입</a></li>
			</c:when>
			<c:otherwise>
				<li style="list-style:none; color:white; font-size:18px; padding:0px 15px 0px 0px;"><%= loginName %>&nbsp;[님]</li>
				<li style="list-style:none; font-size:18px; padding:0px 15px 0px 0px;">
				<a href="<c:url value="./logout.jsp" />">로그아웃</a></li>
			</c:otherwise>
	</c:choose>		
	</ul>	
	
	</div>		
</nav>
</body>
</html>