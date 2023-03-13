<%@page import="java.io.PrintWriter"%>
<%@page import="java.util.Enumeration"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import = "dto.Cust" %>
<%@ page import="java.sql.*"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	request.setCharacterEncoding("UTF-8");
	String filename = "";
	String realFolder = "./images/";
	int maxsize = 5*1024*1024;
	String encType = "utf-8";
	String filePath = application.getRealPath(realFolder);
	
	MultipartRequest multi = new MultipartRequest(request, filePath, maxsize, encType,
	new DefaultFileRenamePolicy());
	String cid			= multi.getParameter("cid");
	String cname		= multi.getParameter("cname");
	String cphone		= multi.getParameter("cphone");
	String cemail		= multi.getParameter("cemail");
	
%>	
	<%@include file = "dbconn.jsp" %>
<%
	
	PreparedStatement pstmt = null;
	int result = 0;
	try{
		String sql = "insert into cust values(?,?,?,?)";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1,Integer.valueOf(cid));
		pstmt.setString(2,cname);
		pstmt.setString(3,cphone);
		pstmt.setString(4,cemail);
		result = pstmt.executeUpdate();
	}
	catch (Exception e){
		out.println(result);
		pstmt.close();
		conn.close();
		PrintWriter o = response.getWriter();
		o.println("<script>alert('회원가입 실패!!'); location.href='./join.jsp';</script> ");
		o.flush();
	}
	if(pstmt != null)
		pstmt.close();
	if(conn != null)
		conn.close();
	if (result >= 1){
		response.sendRedirect("resultMember.jsp?msg=1");
	}
%>
</body>
</html>