 <%@page import="java.io.PrintWriter"%>
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
<title>예약 목록 </title>
</head>
<body>
	<jsp:include page = "menu.jsp"/>
	<div class = "jumbotron">
		<div class = "container">
			<h1 class = "display-4">예약 목록 </h1>
		</div>
	</div>
	<%@include file = "dbconn.jsp" %>
			<%
			String loginId = (String)session.getAttribute("sessionId");
			if(loginId != null){
				PreparedStatement pstat = null;
				PreparedStatement pstat2 = null;
				ResultSet rs = null;
				ResultSet rs2 = null;
				String sql = "select * from r_order where o_c_id = ? ";
				String sql2 = "select * from store where s_id = ? ";
				pstat = conn.prepareStatement(sql);
				pstat.setInt(1, Integer.valueOf(loginId));
				rs = pstat.executeQuery();
			%>
	<div class="container">
		<div class="row">
			<div class="col-md-3" align = center>
				<h3>예약 일자 </h3>
			</div>
			<div class="col-md-8">
				<h3>레스토랑 정보  </h3><br>
			</div>
		</div>
		<div class="row">
		<%
			while(rs.next()){ %>
			<div class="col-md-3" align = center>
				<h4><%=rs.getString("o_date") %></h4><br>
			</div>
			<div class="col-md-8">
				<%
				pstat2 = conn.prepareStatement(sql2);
				pstat2.setInt(1, Integer.valueOf(rs.getString("o_s_id")));
				rs2 = pstat2.executeQuery();
				if(rs2.next()){
				%>
				<h4><%=rs2.getString("s_name") %> / <%=rs2.getString("s_address") %></h4>
			</div>
			<%}} %>
		</div>
	</div>
	<%
			} else{
			PrintWriter o = response.getWriter();
			o.println("<script>alert('로그인을 해주세요!!'); location.href='./stores.jsp';</script> ");
			o.flush(); }
			%>
	<%@ include file="footer.jsp" %>

</body>
</html>