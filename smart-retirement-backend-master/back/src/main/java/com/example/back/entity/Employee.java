package com.example.back.entity;

public class Employee {
    private int id;
    private String name;
    private String gender;
    private String phone;
    private String id_card;
    private String birthday;
    private String hire_date;
    private String resign_date;
    private String imgset_dir;
    private String profile_photo;
    private String CREATED;
    private String UPDATED;

    public int getID() {
        return id;
    }

    public void setID(int ID) {
        this.id = ID;
    }

    public String getUsername() {
        return name;
    }

    public void setUserName(String userName) {
        this.name = userName;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getId_card() {
        return id_card;
    }

    public void setId_card(String id_card) {
        this.id_card = id_card;
    }

    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public String getHire_date() {
        return hire_date;
    }

    public void setHire_date(String hire_date) {
        this.hire_date = hire_date;
    }

    public String getResign_date() {
        return resign_date;
    }

    public void setResign_date(String resign_date) {
        this.resign_date = resign_date;
    }

    public String getImgset_dir() {
        return imgset_dir;
    }

    public void setImgset_dir(String imgset_dir) {
        this.imgset_dir = imgset_dir;
    }

    public String getProfile_photo() {
        return profile_photo;
    }

    public void setProfile_photo(String profile_photo) {
        this.profile_photo = profile_photo;
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
}
