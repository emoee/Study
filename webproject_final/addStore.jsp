<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet"
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<meta charset="UTF-8">
<link rel="stylesheet" href = "cssstyle.css" >
<title>레스토랑 등록</title>
</head>
<body>
	<jsp:include page="./menu.jsp"/>
	<div class="jumbotron">
		<div class ="container">
			<h1 class = "display-4">레스토랑 등록</h1>
		</div>
	</div>
	<div class = "container">
		<form name ="newStore" action="./processAddStore.jsp" class ="form-horizontal" method="post"
		enctype = "multipart/form-data">
		
			<div class="form-group row">
				<label class="col-sm-2">상점 코드</label>
				<div class ="col-sm-3">
					<input type="text" name="sid" class ="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">상점명</label>
				<div class = "col-sm-3">
					<input type="text" name = "sname" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">주소</label>
				<div class = "col-sm-3">
					<input type="text" name = "saddress" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">이미지</label>
				<div class = "col-sm-5">
					<input type="file" name = "simg1_fname" class="form-control">
				</div>
			</div>
			<div class = "form-group row">
				<label class="col-sm-2">상세 정보</label>
				<div class = "col-sm-5">
					<textarea name="sdescription" cols="50" rows="2" class="form-control"></textarea>
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