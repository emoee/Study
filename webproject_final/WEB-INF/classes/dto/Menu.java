package dto;
import java.io.Serializable;

public class Menu {
	private static final long serialVersionUID = 1L;
	private String msid;
	private String mid;
	private String mname;
	private String mprice;
	private String mimg1_fname;
	private String mcontent;
	
	public String getMsid() {
		return msid;
	}
	public void setMsid(String msid) {
		this.msid = msid;
	}
	public String getMid() {
		return mid;
	}
	public void setMid(String mid) {
		this.mid = mid;
	}
	public String getMname() {
		return mname;
	}
	public void setMname(String mname) {
		this.mname = mname;
	}
	public String getMprice() {
		return mprice;
	}
	public void setMprice(String mprice) {
		this.mprice = mprice;
	}
	public String getMimg1_fname() {
		return mimg1_fname;
	}
	public void setMimg1_fname(String mimg1_fname) {
		this.mimg1_fname = mimg1_fname;
	}
	public String getMcontent() {
		return mcontent;
	}
	public void setMcontent(String mcontent) {
		this.mcontent = mcontent;
	}
	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
}
