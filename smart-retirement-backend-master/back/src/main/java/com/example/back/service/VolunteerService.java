package com.example.back.service;

import com.example.back.entity.Volunteer;
import com.example.back.mapper.VolunteerMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.List;

@Service
public class VolunteerService {
    @Autowired
    VolunteerMapper volunteerMapper;
    public void addVolunteerInfo(int id,String name,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,Timestamp CREATED){
        volunteerMapper.addVolunteerInfo(id,name,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,CREATED);
    }
    public Volunteer getVolunteerInfo(int id){
        return volunteerMapper.getVolunteerInfo(id);
    }
    public List<Volunteer> getallvolunteerinfo(){
        return volunteerMapper.getallvolunteerinfo();
    }
    public void updatevolunteerInfo(int id,String name,String gender,String phone,String id_card,String birthday,String checkin_date,String checkout_date,String profile_photo,Timestamp UPDATED){
        volunteerMapper.updatevolunteerInfo(id,name,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,UPDATED);
    }
    public void deletevolunteerinfo(int ID){
        volunteerMapper.deletevolunteerinfo(ID);
    }
    public void autoSetTag(int id,String imgset_dir,String profile_photo){
        volunteerMapper.autoSetTag(id,imgset_dir,profile_photo);
    }
    public void setTag(int id,String profile_photo){
        volunteerMapper.setTag(id,profile_photo);
    }
    public List<String> volunteerrecordin(){
        return volunteerMapper.volunteerrecordin();
    }
    public List<String> volunteerrecordout(){
        return volunteerMapper.volunteerrecordout();
    }
    public Integer getid(){
    	if(volunteerMapper.getid() == null)
    		return 0;
    	return volunteerMapper.getid();
    }
}
