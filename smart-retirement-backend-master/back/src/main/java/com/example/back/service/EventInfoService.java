package com.example.back.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.back.entity.EventInfo;
import com.example.back.mapper.EventInfoMapper;

@Service
public class EventInfoService {
   @Autowired
   EventInfoMapper eventInfoMapper;
   
   public List<EventInfo> getAllEventInfo(){
       return eventInfoMapper.getAllEventInfo();
   }
   
   public void deleteEventInfo(int no){
       eventInfoMapper.deleteEventInfo(no);
   }
   
   public List<EventInfo> getInteractEventInfo(){
       return eventInfoMapper.getInteractEventInfo();
   }
   
   public List<EventInfo> getStrangerEventInfo(){
       return eventInfoMapper.getStrangerEventInfo();
   }
   
   public List<EventInfo> getPoseEventInfo(){
       return eventInfoMapper.getPoseEventInfo();
   }
   
   public List<EventInfo> getFenceEventInfo(){
       return eventInfoMapper.getFenceEventInfo();
   }
}
