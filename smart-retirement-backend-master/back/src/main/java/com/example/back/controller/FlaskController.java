package com.example.back.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.service.EmployeeService;
import com.example.back.service.OlderPersonService;
import com.example.back.service.VolunteerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.sql.Timestamp;
import java.util.Date;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class FlaskController {
    @Autowired
    private OlderPersonService olderPersonService;
    @Autowired
    private VolunteerService volunteerService;
    @Autowired
    private EmployeeService employeeService;

    /**
     * 事件信息插入数据库
     * @param jsonObject
     * @return
     */
    @RequestMapping("/eventLoad")
    public Return eventLoad(@RequestBody JSONObject jsonObject) {
        Return ret = new Return();

        try {
            System.out.println(jsonObject);
            int event_type=Integer.parseInt(jsonObject.getString("event_type"));
            Date date = new Date();
            Timestamp event_date = new Timestamp(date.getTime());
            String event_location=jsonObject.getString("event_location");
            String event_desc=jsonObject.getString("event_desc");
            String snapshot=jsonObject.getString("snapshot_url");
            int oldperson_id=Integer.parseInt(jsonObject.getString("oldperson_id"));
            if(oldperson_id==-1){
                olderPersonService.insertEvent(event_type,event_date,event_location,event_desc,snapshot);
            }else{
                olderPersonService.insertOldEvent(event_type,event_date,event_location,event_desc,oldperson_id,snapshot);
            }
            ret.setStatus(0);
            ret.setMessage("添加事件信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("操作失败");
        }
        return ret;
    }

    /**
     * 调用采集人脸摄像头并通知前端录入人脸的id
     * @param jsonObject
     * @return
     */
    @RequestMapping("/startCollectingFaces")
    public Return startCollectingFaces(@RequestBody JSONObject jsonObject) {
        Return ret = new Return();
        try {
            int ID=Integer.parseInt(jsonObject.getString("id"));//用户
            int type=Integer.parseInt(jsonObject.getString("type"));//摄像头类型
            String base_url = jsonObject.getString("url");//摄像头选择
            System.out.println(base_url);
            String type1="";
            String url = base_url + "/collecting_faces";
            JSONObject jsonObject1=new JSONObject();
            jsonObject1.put("id", String.valueOf(ID));
            System.out.println(type);
            if (type == 1) {
                type1="oldpeople";
                String imgset_dir="http://localhost:5000/static/images/"+type1+"/"+ID;
                String profile_photo="http://localhost:5000/static/images/"+type1+"/"+ID+"/smile_10.jpg";//默认头像，选一张笑的
                olderPersonService.autoSetTag(ID,imgset_dir,profile_photo);
            }else if (type == 2){
                type1="volunteer";
                String imgset_dir="http://localhost:5000/static/images/"+type1+"/"+ID;
                String profile_photo="http://localhost:5000/static/images/"+type1+"/"+ID+"/smile_10.jpg";//默认头像，选一张笑的
                volunteerService.autoSetTag(ID,imgset_dir,profile_photo);
            }else if (type == 3){
                type1="employee";
                String imgset_dir="http://localhost:5000/static/images/"+type1+"/"+ID;
                String profile_photo="http://localhost:5000/static/images/"+type1+"/"+ID+"/smile_10.jpg";//默认头像，选一张笑的
                employeeService.autoSetTag(ID,imgset_dir,profile_photo);
            }
            jsonObject1.put("type", type1);
            HttpUtil.doPost(url,jsonObject1);
            ret.setStatus(0);
            ret.setMessage("成功");
        }catch (Exception e){
            System.out.println(e.getMessage());
            ret.setStatus(1);
            ret.setMessage("操作失败");
        }
        return ret;
    }

}
