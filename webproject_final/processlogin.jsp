<%@page import="java.sql.Statement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@page import="java.io.PrintWriter"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<script>
</script>
<body>
<%@include file = "dbconn.jsp" %>
<%
	request.setCharacterEncoding("UTF-8");
	String filename = "";
	String realFolder = "./images/";
	int maxsize = 5*1024*1024;
	String encType = "utf-8";
	String filePath = application.getRealPath(realFolder);
	
	MultipartRequest multi = new MultipartRequest(request, filePath, maxsize, encType,
	new DefaultFileRenamePolicy());
	String cid		= multi.getParameter("cid");
	String cname	= multi.getParameter("cname");
	
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	String sql = "select * from cust where c_id = ?";
	pstmt = conn.prepareStatement(sql);
	pstmt.setString(1, cid);
	rs = pstmt.executeQuery();
	if(rs.next()){
		if (rs.getString("c_name").equals(cname)){
			session.setAttribute("sessionId",cid);
			session.setAttribute("sessionName",cname);	
			pstmt.close();
			conn.close();
			response.sendRedirect("resultMember.jsp?msg=2");
		} else {
			pstmt.close();
			conn.close();
			response.sendRedirect("login.jsp?error=1");
		}
	}else{
		pstmt.close();
		conn.close();
		response.sendRedirect("login.jsp?error=1");
	}
%>
</body>
</html>