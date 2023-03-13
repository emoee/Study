<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<title>회원가입 화면</title>
<link rel="Stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script type="text/javascript">
        const autoHyphen = (target) => { //전화번호 하이픈 자동 완성 
        	 target.value = target.value
        	   .replace(/[^0-9]/g, '')
        	   .replace(/^(\d{2,3})(\d{3,4})(\d{4})$/, `$1-$2-$3`);
        	}
    </script>
<meta charset="UTF-8">
</head>
<body>
	<jsp:include page="./menu.jsp"/>
	<div class="jumbotron">
		<div class ="container">
			<h1 class = "display-4">회원 가입 </h1>
		</div>
	</div>
	<div class = "container">
		<form name ="newCust" action="./processjoin.jsp" class ="form-horizontal" method="post"
		enctype = "multipart/form-data" class = "form-signin">
		
			<div class="form-group">
				<label class="col-sm-2">아이디</label>
				<div class ="col-sm-3">
					<input type="text" name="cid" class ="form-control" placeholder= "6자리 숫자만 입력 가능합니다." 
					oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" minlength = "6" maxlength="6">
				</div>
			</div>
			<div class = "form-group">
				<label class="col-sm-2">이름 </label>
				<div class = "col-sm-3">
					<input type="text" name = "cname" class="form-control">
				</div>
			</div>
			<div class = "form-group">
				<label class="col-sm-2">전화 번호 </label>
				<div class = "col-sm-3">
					<input type="text" name = "cphone" class="form-control" oninput="autoHyphen(this)" minlength = "9" maxlength="13"
					placeholder= "전화번호를 입력하세요.">
				</div>
			</div>
			<div class = "form-group">
				<label class="col-sm-2">이메일 </label>
				<div class = "col-sm-3">
					<input type="email" name = "cemail" class="form-control">
				</div>
			</div>
			<div class = "form-group">
				<div class = "col-sm-offset-2 col-sm-10">
					<input type="submit" class="btn btn-primary" value="가입"
					style = "background-color:#59a1d0; border-color:#59a1d0;">
				</div>
			</div>
		</form>
	</div>
</body>
</html>