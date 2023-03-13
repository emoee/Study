package dto;
import java.io.Serializable;

public class Cust {
	private static final long serialVersionUID = 1L;
	private String cid;
	private String cname;
	private String cphone;
	private String cemail;
	
	public Cust(String cid, String cname, String cphone, String cemail) {
		this.cid = cid;
		this.cname = cname;
		this.cphone = cphone;
		this.cemail = cemail;
	}
	public String getCid() {
		return cid;
	}
	public void setCid(String cid) {
		this.cid = cid;
	}
	public String getCname() {
		return cname;
	}
	public void setCname(String cname) {
		this.cname = cname;
	}
	public String getCphone() {
		return cphone;
	}
	public void setCphone(String cphone) {
		this.cphone = cphone;
	}
	public String getCemail() {
		return cemail;
	}
	public void setCemail(String cemail) {
		this.cemail = cemail;
	}
	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
}
