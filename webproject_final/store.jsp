<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*"%>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href = "cssstyle.css" >
<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<title>상점 상세 정보</title>
</head>
<body>
	<jsp:include page="menu.jsp"/>
	<div class="jumbotron">
		<div class="container">
			<h2 class ="display-4">레스토랑 상세 정보</h2>
		</div>
	</div>
	<%@include file="dbconn.jsp" %> 
	<%
		String storeId = request.getParameter("id");
		
		PreparedStatement pstat = null;
		ResultSet rs = null;
		
		String sql1 = "select * from store where s_id = ?";
		pstat = conn.prepareStatement(sql1);
		pstat.setString(1, storeId);
		rs = pstat.executeQuery();
		if(rs.next()){
	%>
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<img src="${pageContext.request.contextPath}/images/<%= rs.getString("s_img1_fname") %>" 
						style="width:350px; heigt : 200px;">
			</div>
			<div class="col-md-8">
				<h3><%= rs.getString("s_name") %></h3>
				<p><%= rs.getString("s_address") %></p>
				<p><b>상점 코드 : </b><span class="badge badge-danger"><%= rs.getString("s_id") %></span></p>
				<p><b>상세 설명 : </b><%= rs.getString("s_description") %></p>
				<p><a href="./order.jsp?id=<%=rs.getString("s_id")%>" class="btn btn-info">예약 하기 &raquo;</a>
					<a href="./stores.jsp" class="btn btn-secondary">레스토랑 목록 &raquo;</a>
			</div>
			<%
				}
				pstat = null;
				rs = null;
				String sql2 = "select * from menu where m_s_id = ?";
				pstat = conn.prepareStatement(sql2);
				pstat.setString(1, storeId);
				rs = pstat.executeQuery();
			%>
		</div>
	</div><br><hr>
	<div class="container" style = "background-color:#e3e7ec"><br>
		<h3 align=center style="font-siz:20px; font: Helvetica Nene"></h3>
		<div class = "row" align = "left">
			<% while(rs.next()){ %>
			<div class="col-md-4">
				<img src="${pageContext.request.contextPath}/images/<%= rs.getString("m_img1_fname") %>" 
						style="width:350px; heigt : 100px;"><br><br>
				<h3><%= rs.getString("m_name") %></h3>
				<p><b>가격 : </b><%= rs.getString("m_price") %>원 </p>
				<p><b>메뉴 코드 : </b><span class="badge badge-danger"><%= rs.getString("m_id") %></span></p>
				<p><b>상세 설명 : </b><%= rs.getString("m_content") %></p>
			</div>
			<% 
				}
				rs.close();
				pstat.close();
				conn.close();
			%>
			<div class="col-md-4">
				<p style = "height: 250px;border: 1px;font-size:25px; line-height: 250px; background-color:white" align = "center" >..추가중..</p>
			</div>
		</div>
		<hr>
	</div>
	<jsp:include page="footer.jsp"></jsp:include>
</body>
</html>