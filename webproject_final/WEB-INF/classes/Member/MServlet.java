package Member;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.*;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/MServlet")
public class MServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
   
    public MServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		processRequest(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		processRequest(request, response);
	}
	private void processRequest(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String cname = request.getParameter("name");
		String cemail = request.getParameter("email");
		if ( cname != null && cemail != null) {
			Connection conn = null;
			try { 
				Class.forName("com.mysql.cj.jdbc.Driver"); 
			} catch (ClassNotFoundException e) {
				System.out.println("ClassNotFoundException: " + e.getMessage());
			}
			try {
			String jdbcURL = "jdbc:mysql://localhost:3306/RestaurantsDB";
			String dbUser = "root";
			String dbPass = "test";
			conn = DriverManager.getConnection(jdbcURL,dbUser,dbPass);
			
			PreparedStatement pstat = null;
			ResultSet rs = null;
			Object result = null; 
			List<Map<String, Object>> cs = new ArrayList<>();
			String sql1 = "select * from cust where c_name = ? and c_email = ?";
			pstat = conn.prepareStatement(sql1);
			pstat.setString(1, cname);
			pstat.setString(2, cemail);
			rs = pstat.executeQuery();
			if(rs.next()){
				Map<String, Object> c = new HashMap<>();
				c.put("id", rs.getInt("c_id"));
				c.put("name", rs.getString("c_name"));
				cs.add(c);
				request.setAttribute("name", c.get("name"));
				request.setAttribute("id", c.get("id"));
				RequestDispatcher rd = request.getRequestDispatcher("view.jsp");
				rd.forward(request, response);		
			} else {
				result = "데이터를 찾을 수 없습니다. ";
				request.setAttribute("name", result);
				RequestDispatcher rd = request.getRequestDispatcher("view.jsp");
				rd.forward(request, response);
			}
			} catch(SQLException e) {
				System.out.println("SQLException: " + e.getMessage());
				System.out.println("SQLState: " + e.getSQLState());
				System.out.println("VendorError: " + e.getErrorCode());
			}
			
		}
	
	}

}
