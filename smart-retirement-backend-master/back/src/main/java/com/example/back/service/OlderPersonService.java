package com.example.back.service;

import com.example.back.entity.OlderPerson;
import com.example.back.mapper.OlderPersonMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.List;

@Service
public class OlderPersonService {
    @Autowired
    OlderPersonMapper olderPersonMapper;

    public int addOlderInfo(int ID,String username,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,String room_number,Timestamp CREATED){
        return olderPersonMapper.addOlderInfo(ID,username,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,room_number,CREATED);
    }
    public OlderPerson getOlderInfo(int ID){
        return olderPersonMapper.getOlderInfo(ID);
    }
    public List<OlderPerson> getalloldmaninfo(){
        return olderPersonMapper.getalloldmaninfo();
    }
    public void updateOldmanInfo(int ID,String username,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,String room_number,Timestamp UPDATED){
        olderPersonMapper.updateOldmanInfo(ID,username,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,room_number,UPDATED);
    }
    public void deleteoldmaninfo(int ID){
        olderPersonMapper.deleteoldmaninfo(ID);
    }
    public void insertEvent(int event_type,Timestamp event_date,String event_location,String event_desc,String snapshot){
        olderPersonMapper.insertEvent(event_type,event_date,event_location,event_desc,snapshot);
    }
    public void insertOldEvent(int event_type,Timestamp event_date,String event_location,String event_desc,int oldperson_id,String snapshot){
        olderPersonMapper.insertOldEvent(event_type,event_date,event_location,event_desc,oldperson_id,snapshot);
    }
    public void autoSetTag(int ID,String imgset_dir,String profile_photo){
        olderPersonMapper.autoSetTag(ID,imgset_dir,profile_photo);
    }
    public void setTag(int ID,String profile_photo){
        olderPersonMapper.setTag(ID,profile_photo);
    }
    public List<String> oldrecord(){
        return olderPersonMapper.oldrecord();
    }
    public Integer getid(){
    	if(olderPersonMapper.getid() == null)
    		return 0;
    	return olderPersonMapper.getid();
    }
}
