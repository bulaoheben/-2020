package com.example.back.controller;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.OSSObjectSummary;
import com.aliyun.oss.model.ObjectListing;
import com.example.back.Return;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class PicController {
	
	private List<String> pic_url;
	private List<String> Screenshoot;
	

    /**
     * 向前端返回所有头像url
     * @param jsonObject
     * @return
     */
    @RequestMapping("/getPic")
    public Return getPic(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try{
            JSONObject data = new JSONObject();
            pic_url = new ArrayList<String>();
        	HttpUtil.doPost("http://localhost:5000/get_pics",jsonObject);	
//        	List<String> ans = getPic_fromflask(jsonObject);
        	while(pic_url.isEmpty()) {
//        		System.out.println("111");
        	}
//        	for(int i = 0;i < pic_url.size();i++) {
//        		System.out.println(pic_url.get(i));
//			}
            data.put("pic",pic_url);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取成功");
        }catch (Exception e){
        	e.printStackTrace();
            ret.setStatus(1);
            ret.setMessage("获取失败");
        }
        return ret;
    }
	
	@RequestMapping("/getPic_fromflask")
	public void getPic_fromflask(@RequestBody JSONObject jsonObject){
		try {
			if(!pic_url.isEmpty()) {
				pic_url.clear();
			}
			JSONArray jsonArray = jsonObject.getJSONArray("allfile");
			for(int i = 0;i < jsonArray.size();i++) {
				pic_url.add(jsonArray.get(i).toString());
			}
            
            
        }catch (Exception e){
            e.printStackTrace();
        }
	}
	
	@RequestMapping("/getScreenshoot_fromflask")
	public void getScreenshoot_fromflask(@RequestBody JSONObject jsonObject){
		try {
			if(!Screenshoot.isEmpty()) {
				Screenshoot.clear();
			}
			JSONArray jsonArray = jsonObject.getJSONArray("allfile");
			for(int i = 0;i < jsonArray.size();i++) {
				Screenshoot.add(jsonArray.get(i).toString());
			}
            
            
        }catch (Exception e){
            e.printStackTrace();
        }
	}

    /**
     * 截图url
     * @param jsonObject
     * @return
     */
    @RequestMapping("/getScreenshoot")
    public Return getScreenshoot(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try{
            String name=jsonObject.getString("name");
            JSONObject data = new JSONObject();
            Screenshoot = new ArrayList<String>();
        	HttpUtil.doPost("http://localhost:5000/getScreenshoot",jsonObject);	
        	while(Screenshoot.isEmpty()) {
//        		System.out.println("111");
        	}
         
            data.put("pic",Screenshoot);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("获取失败");
        }
        return ret;
    }
}
