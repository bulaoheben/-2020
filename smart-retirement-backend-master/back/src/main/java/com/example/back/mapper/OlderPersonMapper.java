package com.example.back.mapper;

import com.example.back.entity.OlderPerson;
import org.springframework.stereotype.Repository;

import java.sql.Timestamp;
import java.util.List;


@Repository
public interface OlderPersonMapper {
    int addOlderInfo(int ID,String username,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,String room_number,Timestamp CREATED);
    OlderPerson getOlderInfo(int ID);
    List<OlderPerson> getalloldmaninfo();
    void updateOldmanInfo(int ID,String username,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,String room_number,Timestamp UPDATED);
    void deleteoldmaninfo(int ID);
    void insertEvent(int event_type,Timestamp event_date,String event_location,String event_desc,String snapshot);
    void insertOldEvent(int event_type,Timestamp event_date,String event_location,String event_desc,int oldperson_id,String snapshot);
    void autoSetTag(int ID,String imgset_dir,String profile_photo);
    void setTag(int id,String profile_photo);
    List<String> oldrecord();
    Integer getid();
}