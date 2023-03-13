<%@page import="java.io.PrintWriter"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*"%>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<link rel="stylesheet" href = "cssstyle.css" >
<title>예약</title>
</head>
<body>
	<jsp:include page="./menu.jsp"/>
	<div class="jumbotron">
		<div class ="container">
			<h1 class = "display-4">예약 </h1>
		</div>
	</div>
	<%@include file="dbconn.jsp" %> 
	<%
		String loginId = (String)session.getAttribute("sessionId");
		if(loginId != null){
		String storeId = request.getParameter("id");
		
		PreparedStatement pstat = null;
		ResultSet rs = null;
		
		String sql1 = "select * from store where s_id = ?";
		pstat = conn.prepareStatement(sql1);
		pstat.setInt(1,Integer.valueOf(storeId));
		rs = pstat.executeQuery();
		if(rs.next()){
			String sname = rs.getString("s_name");
			String sid = rs.getString("s_id");
			%>
	<div class = "container">
		<form name ="newOrder" action="./processorder.jsp" class ="form-horizontal" method="post"
		enctype = "multipart/form-data">
		
			<div class="form-group row">
				<label class="col-sm-2">레스토랑</label>
				<div class ="col-sm-3">
					<input type="text" name = "osname" class="form-control" value = "<%=sname%>"
					onchange="changesN(this)">
					<script> //레스토랑 이름 변경 불가능하도록 설정 
					function changesN(N) {
					  N.value = '<%=sname%>';
					}
					</script>
					<input type="hidden" name = "osid" class="form-control" value = "<%=sid%>">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">주소</label>
				<div class = "col-sm-3">
					<p><%=rs.getString("s_address") %></p>
				</div>
			</div>
			<%}
				pstat = null;
				rs = null;
				String sql2 = "select * from menu where m_s_id = ?";
				pstat = conn.prepareStatement(sql2);
				pstat.setString(1, storeId);
				rs = pstat.executeQuery(); 
			%>
			<div class = "form-group row">
				<label class="col-sm-2">메뉴 </label>
				<div class = "col-sm-5">
				<%while(rs.next()){  %>
					<input type="radio" name = "omid" value="<%=rs.getString("m_id")%>"> <%=rs.getString("m_name")%> : <%=rs.getString("m_price")%>원 
					<h7><br><%=rs.getString("m_content")%><br><br></h7>
				<% 
					}
				pstat = null;
				rs = null;
				String sql3 = "select * from cust where c_id = ?";
				pstat = conn.prepareStatement(sql3);
				pstat.setInt(1, Integer.valueOf(loginId));
				rs = pstat.executeQuery(); 
				if(rs.next()){
				%>
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">예약 일자 </label>
				<div class = "col-sm-3">
					<input type="date" id = "odate" name = "odate" class="form-control">
					<script>
					document.getElementById('odate').valueAsDate = new Date();
					</script>
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">예약자 정보 </label>
				<div class = "col-sm-3">
					<p><%=rs.getString("c_name") %></p>
					<input type="hidden" name = "ocid" class="form-control" value = "<%=loginId%>" maxlength = 6>
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">예약자 전화번호 </label>
				<div class = "col-sm-3">
					<p><%=rs.getString("c_phone") %></p>
				</div>
			</div>
			<% }
				rs.close();
				pstat.close();
				conn.close();
			%>
			<div class = "form-group row">
				<div class = "col-sm-offset-2 col-sm-10">
					<p><a href="./store.jsp?id=<%=storeId%>" class="btn btn-secondary">레스토랑 &raquo;</a>
					<input type="submit" class="btn btn-primary" value="예약  &raquo" 
					style = "background-color:#59a1d0; border-color:#59a1d0;">
				</div>
			</div>
		</form>
		<%
			} else{
			PrintWriter o = response.getWriter();
			o.println("<script>alert('로그인을 해주세요!!'); location.href='./login.jsp';</script> ");
			o.flush(); }
			%>
	</div>
</body>
</html>