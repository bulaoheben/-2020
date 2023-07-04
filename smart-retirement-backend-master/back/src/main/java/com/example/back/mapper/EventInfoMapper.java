package com.example.back.mapper;

import java.util.List;

import org.springframework.stereotype.Repository;

import com.example.back.entity.EventInfo;
@Repository
public interface EventInfoMapper {
	 List<EventInfo> getAllEventInfo();
	 void deleteEventInfo(int no);
	 List<EventInfo> getInteractEventInfo();
	 List<EventInfo> getStrangerEventInfo();
	 List<EventInfo> getPoseEventInfo();
	 List<EventInfo> getFenceEventInfo();
}
