<%@page import="java.util.Enumeration"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<%@ page import="java.sql.*"%>

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
	String sid				= multi.getParameter("sid");
	String sname			= multi.getParameter("sname");
	String saddress		= multi.getParameter("saddress");
	String sdescription	= multi.getParameter("sdescription");
	
	Enumeration files = multi.getFileNames();
	String fname = (String)files.nextElement();
	filename = multi.getFilesystemName(fname);
%>	
	<%@include file = "dbconn.jsp" %>
<%
	PreparedStatement pstmt = null;
	int result = 0;
	
		String sql = "insert into store values(?,?,?,?,?)";
		pstmt = conn.prepareStatement(sql);
		pstmt.setInt(1,Integer.valueOf(sid));
		pstmt.setString(2,sname);
		pstmt.setString(3,saddress);
		pstmt.setString(4,filename);
		pstmt.setString(5,sdescription);
		result = pstmt.executeUpdate();
	out.println(result);
	if(pstmt != null)
		pstmt.close();
	if(conn != null)
		conn.close();
	
	response.sendRedirect("stores.jsp");
%>
</body>
</html>