package com.example.back.entity;

public class OlderPerson {
    private int ID;
    private String username;
    private String gender;
    private String phone;
    private String id_card;
    private String birthday;
    private String checkin_date;
    private String checkout_date;
    private String imgset_dir;
    private String profile_photo;
    private String room_number;
    private String CREATED;
    private String UPDATED;

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getUsername() {
        return username;
    }

    public void setUserName(String userName) {
        this.username = userName;
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

    public String getCheckin_date() {
        return checkin_date;
    }

    public void setCheckin_date(String checkin_date) {
        this.checkin_date = checkin_date;
    }

    public String getCheckout_date() {
        return checkout_date;
    }

    public void setCheckout_date(String checkout_date) {
        this.checkout_date = checkout_date;
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

    public String getRoom_number() {
        return room_number;
    }

    public void setRoom_number(String room_number) {
        this.room_number = room_number;
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
