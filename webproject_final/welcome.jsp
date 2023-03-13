<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<%@page import = "dto.Store" %>
<%@page import = "dao.StoreRepository" %>
<!DOCTYPE html>
<html>
<head>
<link rel="Stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<script
    src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script
    src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script
    src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
 
<title>welcome</title>
<link rel="stylesheet" href = "cssstyle.css" >
</head>
<body>
<%@ include file="menu.jsp"%>

	<%!
		String tagline = "Welcome to Web Restaurant!";
	%>
	<%@include file = "dbconn.jsp" %>
			<%
				Statement stat = null;
				ResultSet rs = null;
				int i = 1;
				String item = "";
				String sql = "select * from store";
				stat = conn.createStatement();
				rs = stat.executeQuery(sql);
			%>
	<div class="jumbotron">
		<div class="container">
			<h1 class="display-4"> <%=tagline%> </h1>
		</div>
	</div>
	<div  class = "container" style = "width: 700px; height: 500px; ">
	<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
	    <ol class="carousel-indicators">
	        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
	        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
	        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
	    </ol>
	    <div class="carousel-inner">
	    <%  while(rs.next()){
			if (i == 1) {item = "carousel-item active"; }
    			else item = "carousel-item"; 
    	%>
	        <div class="<%=item%>">
	        	<a href = "./store.jsp?id=<%=rs.getString("s_id")%>">
	            <img class="d-block w-100" src = "./images/<%= rs.getString("s_img1_fname")%>" style = "width: 700px; height: 500px;"/>
	        	</a>
	        	<div class="carousel-caption d-none d-md-block">
	        		<h5 style = "font-size: 30px; text-shadow: 3px 4px 5px black"><%=rs.getString("s_name")%></h5>
       		 	</div>
	        </div>
	        <%  i = i + 1;}
				rs.close();
				stat.close();
				conn.close();
			%>
	    </div>
	    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
	        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
	        <span class="sr-only">Previous</span>
	    </a>
	    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
	        <span class="carousel-control-next-icon" aria-hidden="true"></span>
	        <span class="sr-only">Next</span>
	    </a>
	</div>
	</div>
<hr>
<%@ include file="footer.jsp"%>
</body>
</html>