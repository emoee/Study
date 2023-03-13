<%@page import="org.apache.el.parser.BooleanNode"%>
<%@page import="java.util.Random"%>
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
	Random random = new Random(); 
	
	MultipartRequest multi = new MultipartRequest(request, filePath, maxsize, encType,
	new DefaultFileRenamePolicy());
	String osid		= multi.getParameter("osid");
	String odate	= multi.getParameter("odate");
	String ocid		= multi.getParameter("ocid");
	String omid		= multi.getParameter("omid");
	int oid			= (int)(Math.random() * 100)*(int)(Math.random() * 100)*7/23;
	Boolean b 		= true;
%>	
<%@include file = "dbconn.jsp" %>
<%
	if( odate != null){
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	int result = 0;
	
	String sql = "select * from r_order where o_id = ?";
	pstmt = conn.prepareStatement(sql);
	
	while(b){
		pstmt.setInt(1,oid);
		rs = pstmt.executeQuery();
		if(rs.next()){
			oid = oid + 1;
		} else {
			b = false;
		}
	}
	
	try{
		pstmt = null;
		String sql2 = "insert into r_order values(?,?,?,?)";
		pstmt = conn.prepareStatement(sql2);
		pstmt.setInt(1,oid);
		pstmt.setInt(2,Integer.valueOf(osid));
		pstmt.setString(3,odate);
		pstmt.setInt(4,Integer.valueOf(ocid));
		result = pstmt.executeUpdate();
	} catch (Exception e){
		out.println(result);
		pstmt.close();
		conn.close();
		PrintWriter o = response.getWriter();
		o.println("<script>alert('예약 실패!! 다시시도해주세요.'); location.href='./stores.jsp';</script> ");
		o.flush();
	} finally{
		pstmt = null;
		String sql3 = "insert into order_menu values(?,?)";
		pstmt = conn.prepareStatement(sql3);
		pstmt.setInt(1,Integer.valueOf(omid));
		pstmt.setInt(2,oid);
		result = pstmt.executeUpdate();
		out.println(result);
		if(pstmt != null)
			pstmt.close();
		if(conn != null)
			conn.close();
		if (result >= 1){
			response.sendRedirect("./check.jsp");
	}
	}
	}
%>
</body>
</html>