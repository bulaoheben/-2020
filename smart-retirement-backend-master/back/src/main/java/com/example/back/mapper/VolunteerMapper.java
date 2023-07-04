package com.example.back.mapper;

import com.example.back.entity.Volunteer;
import org.springframework.stereotype.Repository;

import java.sql.Timestamp;
import java.util.List;

@Repository
public interface VolunteerMapper {
    void addVolunteerInfo(int id,String name,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,Timestamp CREATED);
    Volunteer getVolunteerInfo(int id);
    List<Volunteer> getallvolunteerinfo();
    void updatevolunteerInfo(int id,String name,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,Timestamp UPDATED);
    void deletevolunteerinfo(int id);
    void autoSetTag(int id,String imgset_dir,String profile_photo);
    void setTag(int id,String profile_photo);
    List<String> volunteerrecordin();
    List<String> volunteerrecordout();
    Integer getid();
}
