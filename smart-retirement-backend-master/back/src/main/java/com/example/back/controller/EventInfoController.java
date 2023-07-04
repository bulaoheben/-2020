package com.example.back.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.entity.EventInfo;
import com.example.back.service.EventInfoService;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class EventInfoController {

	@Autowired
    private EventInfoService eventInfoService;
	
	 @RequestMapping("/getalleventinfo")
	    public Return getAllEmployeeInfo(){
	        Return ret=new Return();
	        try{
	            List<EventInfo> ans=eventInfoService.getAllEventInfo();
	            JSONObject data = new JSONObject();
	            data.put("Info",ans);
	            ret.setData(data);
	            ret.setStatus(0);
	            ret.setMessage("获取成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            e.printStackTrace();
	            ret.setMessage("获取失败");
	        }
	        return ret;
	    }
	 
	 @RequestMapping("/getinteracteventinfo")
	    public Return getInteractEventInfo(){
	        Return ret=new Return();
	        try{
	            List<EventInfo> ans=eventInfoService.getInteractEventInfo();
	            JSONObject data = new JSONObject();
	            data.put("Info",ans);
	            ret.setData(data);
	            ret.setStatus(0);
	            ret.setMessage("获取成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            e.printStackTrace();
	            ret.setMessage("获取失败");
	        }
	        return ret;
	    }
	 
	 @RequestMapping("/getstrangereventinfo")
	    public Return getStrangerEventInfo(){
	        Return ret=new Return();
	        try{
	            List<EventInfo> ans=eventInfoService.getStrangerEventInfo();
	            JSONObject data = new JSONObject();
	            data.put("Info",ans);
	            ret.setData(data);
	            ret.setStatus(0);
	            ret.setMessage("获取成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            e.printStackTrace();
	            ret.setMessage("获取失败");
	        }
	        return ret;
	    }
	 
	 @RequestMapping("/getposeeventinfo")
	    public Return getPoseEventInfo(){
	        Return ret=new Return();
	        try{
	            List<EventInfo> ans=eventInfoService.getPoseEventInfo();
	            JSONObject data = new JSONObject();
	            data.put("Info",ans);
	            ret.setData(data);
	            ret.setStatus(0);
	            ret.setMessage("获取成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            e.printStackTrace();
	            ret.setMessage("获取失败");
	        }
	        return ret;
	    }
	 
	 @RequestMapping("/getFenceeventinfo")
	    public Return getFenceEventInfo(){
	        Return ret=new Return();
	        try{
	            List<EventInfo> ans=eventInfoService.getFenceEventInfo();
	            JSONObject data = new JSONObject();
	            data.put("Info",ans);
	            ret.setData(data);
	            ret.setStatus(0);
	            ret.setMessage("获取成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            e.printStackTrace();
	            ret.setMessage("获取失败");
	        }
	        return ret;
	    }
	 
	  @RequestMapping("/deleteeventinfo/{no}")
	    public Return deleteemployeeinfo(@PathVariable int no){
	        Return ret=new Return();
	        try{
	            int No=no;
	            eventInfoService.deleteEventInfo(No);
	            ret.setStatus(0);
	            ret.setMessage("删除事件信息成功");
	        }catch (Exception e){
	            ret.setStatus(1);
	            ret.setMessage("删除事件信息失败");
	        }
	        return ret;
	    }
}
