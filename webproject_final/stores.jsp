 <%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import = "java.util.ArrayList" %>
<%@page import="java.sql.*" %>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="cssstyle.css">
<link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<title>레스토랑 목록 </title>
</head>
<body>
	<jsp:include page = "menu.jsp"/>
	<div class = "jumbotron">
		<div class = "container">
			<h1 class = "display-4">레스토랑 목록 </h1>
		</div>
	</div>
	<div class = "container">
		<div class = "row" align = "center">
			<%@include file = "dbconn.jsp" %>
			<%
				Statement stat = null;
				ResultSet rs = null;
				String sql = "select * from store";
				stat = conn.createStatement();
				rs = stat.executeQuery(sql);
				while(rs.next()){
			%>
			<div class="row">
				<div class="col-md-4" align="center">	
					 <img src = "./images/<%= rs.getString("s_img1_fname") %>">
				</div>
				<div class="col-md-4" align="left">
					<h3><%= rs.getString("s_name") %></h3>
					<p><%= rs.getString("s_address") %>
					<p><%= rs.getString("s_description") %>	
				</div>
				<div class="col-md-2" style = "top : 10px">
					<p><a href="./store.jsp?id=<%=rs.getString("s_id")%>"
					class ="btn btn-secondary" role="button">상세 정보 &raquo;</a>
					<p><a href="./order.jsp?id=<%=rs.getString("s_id")%>"" class="btn btn-info">예약 하기 &raquo;</a>
				</div>
			</div><br>
			<% }
				rs.close();
				stat.close();
				conn.close();
			%>
		</div>
		<hr>
	</div>
	<%@ include file="footer.jsp" %>

</body>
</html>