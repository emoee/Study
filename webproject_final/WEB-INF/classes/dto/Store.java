package dto;
import java.io.Serializable;

public class Store {
	private static final long serialVersionUID = 1L;
	private String sid;
	private String sname;
	private String saddress;
	private String simg1_fname;
	private String sdescription;
	
	public String getSid() {
		return sid;
	}

	public void setSid(String sid) {
		this.sid = sid;
	}

	public String getSname() {
		return sname;
	}

	public void setSname(String sname) {
		this.sname = sname;
	}

	public String getSaddress() {
		return saddress;
	}

	public void setSaddress(String saddress) {
		this.saddress = saddress;
	}

	public String getSimg1_fname() {
		return simg1_fname;
	}

	public void setSimg1_fname(String simg1_fname) {
		this.simg1_fname = simg1_fname;
	}

	public String getSdescription() {
		return sdescription;
	}

	public void setSdescription(String sdescription) {
		this.sdescription = sdescription;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	
}
