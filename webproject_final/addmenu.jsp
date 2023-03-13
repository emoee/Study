<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href = "cssstyle.css" >
<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<title>레스토랑 메뉴 등록</title>
</head>
<body>
	<jsp:include page="./menu.jsp"/>
	<div class="jumbotron">
		<div class ="container">
			<h1 class = "display-4">레스토랑 메뉴 등록</h1>
		</div>
	</div>
	<div class = "container">
		<form name ="newMenu" action="./processAddmenu.jsp" class ="form-horizontal" method="post"
		enctype = "multipart/form-data">
			<div class="form-group row">
				<label class="col-sm-2">상점 코드</label>
				<div class ="col-sm-3">
			<%@include file = "dbconn.jsp" %>
			<%
				Statement stat = null;
				ResultSet rs = null;
				String sql = "select * from store";
				stat = conn.createStatement();
				rs = stat.executeQuery(sql);
				while(rs.next()){
			%>
					<input type="radio" name = "msid" value="<%=rs.getString("s_id")%>"> <%=rs.getString("s_name")%><br>
			<% }
				rs.close();
				stat.close();
				conn.close();
			%>
			</div>
			</div>
			<div class="form-group row">
				<label class="col-sm-2">메뉴 코드</label>
				<div class ="col-sm-3">
					<input type="text" name="mid" class ="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">이름</label>
				<div class = "col-sm-3">
					<input type="text" name = "mname" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">가격</label>
				<div class = "col-sm-3">
					<input type="text" name = "mprice" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">이미지</label>
				<div class = "col-sm-5">
					<input type="file" name = "mimg1_fname" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">상세 정보</label>
				<div class = "col-sm-5">
					<textarea name="mcontent" cols="50" rows="2" class="form-control"></textarea>
				</div>
			</div>
			<div class = "form-group row">
				<div class = "col-sm-offset-2 col-sm-10">
					<input type="submit" class="btn btn-primary" value="등록"
					style = "background-color:#59a1d0; border-color:#59a1d0;">
				</div>
			</div>
		</form>
	</div>
</body>
</html>