package com.example.back.entity;

public class SysUser {
    private int ID;
    private String UserName;
    private String Password;
    private String REAL_NAME;
    private String SEX;
    private String EMAIL;
    private String PHONE;
    private String MOBILE;
    private String CREATED;
    private String UPDATED;
    private String logoimage;



    public int getUser_id() {
        return ID;
    }

    public void setUser_id(int ID) {
        this.ID = ID;
    }

    public String getUserName() {
        return UserName;
    }

    public void setUserName(String UserName) {
        this.UserName = UserName;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public String getReal_name() {
        return REAL_NAME;
    }

    public void setReal_name(String REALNAME) {
        this.REAL_NAME = REALNAME;
    }

    public String getSex() {
        return SEX;
    }

    public void setSex(String SEX) {
        this.SEX = SEX;
    }

    public String getEmail() {
        return EMAIL;
    }

    public void setEmail(String EMAIL) {
        this.EMAIL = EMAIL;
    }

    public String getPhone() {
        return PHONE;
    }

    public void setPhone(String PHONE) {
        this.PHONE = PHONE;
    }

    public String getMobile() {
        return MOBILE;
    }

    public void setMobile(String MOBILE) {
        this.MOBILE = MOBILE;
    }

    public String getCreate_time() {
        return CREATED;
    }

    public void setCreate_time(String CREATED) {
        this.CREATED = CREATED;
    }

    public String getUpdate_time() {
        return UPDATED;
    }

    public void setUpdate_time(String UPDATED) {
        this.UPDATED = UPDATED;
    }

    public String getLogoimage() {
        return logoimage;
    }

    public void setLogoimage(String logoimage) {
        this.logoimage = logoimage;
    }

}
