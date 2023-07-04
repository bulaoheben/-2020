package com.example.back.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.entity.Volunteer;
import com.example.back.service.VolunteerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.sql.Timestamp;
import java.util.Date;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class VolunteerController {
    @Autowired
    private VolunteerService volunteerService;

    /**
     * 添加义工信息
     * @param jsonObject
     * @return
     */
    @RequestMapping("/addvolunteerinfo")
    public Return addVolunteerInfo(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try{
            String name=jsonObject.getString("name");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String checkin_date=jsonObject.getString("checkin_date");
            String checkout_date=jsonObject.getString("checkout_date");
            String profile_photo="/";
            Date date = new Date();
            Timestamp CREATED = new Timestamp(date.getTime());
            int id=volunteerService.getid().intValue();
            volunteerService.addVolunteerInfo(id+1,name,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,CREATED);
            ret.setStatus(0);
            ret.setMessage(Integer.toString(id+1));
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("添加义工信息失败");
        }
           return ret;
    }

    /**
     * 通过id获取义工信息
     * @param id
     * @return
     */
    @RequestMapping("/getvolunteerinfo/{id}")
    public Return getVolunteerInfo(@PathVariable int id){
        Return ret = new Return();
        try{
            Volunteer ans=volunteerService.getVolunteerInfo(id);
            JSONObject data = new JSONObject();
            data.put("Info",ans);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取义工信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("获取义工信息失败");
        }
        return ret;
    }

    /**
     * 获取所有义工信息
     * @param
     * @return
     */
    @RequestMapping("/getallvolunteerinfo")
    public Return getAllVolunteerInfo(){
        Return ret=new Return();
        try{
            List<Volunteer> ans=volunteerService.getallvolunteerinfo();
            JSONObject data = new JSONObject();
            data.put("Info",ans);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("获取信息失败");
        }
        return ret;
    }

    /**
     * 修改义工信息
     * @param jsonObject
     * @return
     */
    @RequestMapping("/updatevolunteerinfo/{id}")
    public Return updateVolunteerInfo(@PathVariable int id, @RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int ID=id;
            String name=jsonObject.getString("name");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String checkin_date=jsonObject.getString("checkin_date");
            String checkout_date=jsonObject.getString("checkout_date");
            String profile_photo=jsonObject.getString("profile_photo");
            Date date = new Date();
            Timestamp UPDATED = new Timestamp(date.getTime());
            volunteerService.updatevolunteerInfo(ID,name,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,UPDATED);
            ret.setStatus(0);
            ret.setMessage("修改义工信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("修改义工信息失败");
        }
        return ret;
    }

    /**
     * 删除义工信息
     * @param
     * @return
     */
    @RequestMapping("/deletevolunteerinfo/{id}")
    public Return deletevolunteerinfo(@PathVariable int id){
        Return ret=new Return();
        try{
            int ID=id;
            volunteerService.deletevolunteerinfo(ID);
            ret.setStatus(0);
            ret.setMessage("删除义工信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("删除义工信息失败");
        }
        return ret;
    }

    /**
     * 修改义工头像
     * @param jsonObject
     * @return
     */
    @RequestMapping("/setvolunteertag")
    public Return setTag(@RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int id=Integer.parseInt(jsonObject.getString("id"));
            String profile_photo=jsonObject.getString("profile_photo");
            volunteerService.setTag(id,profile_photo);
            ret.setStatus(0);
            ret.setMessage("更新头像成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("更新头像失败");
        }
        return ret;
    }

    /**
     * 报表信息:义工入职离职时间统计
     * @param
     * @return
     */
    @RequestMapping("/volunteerrecord")
    public Return volunteerrecord(){
        Return ret=new Return();
        try{
            List<String> volunteerin=volunteerService.volunteerrecordin();
            List<String> volunteerout=volunteerService.volunteerrecordout();
            int in[]=new int[volunteerin.size()];
            int out[]=new int[volunteerout.size()];
            int i=0;
            int j=0;
            for(String s1:volunteerin){
                String[] sub=s1.split("-");
                in[i]=Integer.parseInt(sub[1]);
                i++;
            }
            for(String s2:volunteerout){
                String[] sub=s2.split("-");
                out[j]=Integer.parseInt(sub[1]);
                j++;
            }
            int innum[]=new int[5];
            int outnum[]=new int[5];
            for(int a:in){
                if(a==3){
                    innum[0]++;
                }else if(a==4){
                    innum[1]++;
                }else if(a==5){
                    innum[2]++;
                }else if(a==6){
                    innum[3]++;
                }else if(a==7){
                    innum[4]++;
                }
            }
            for(int a:out){
                if(a==3){
                    outnum[0]++;
                }else if(a==4){
                    outnum[1]++;
                }else if(a==5){
                    outnum[2]++;
                }else if(a==6){
                    outnum[3]++;
                }else if(a==7){
                    outnum[4]++;
                }
            }
            String num[]=new String[5];
            int k=0;
            for(int a:innum){
                num[k]=innum[k]+","+outnum[k];
                k++;
            }
            JSONObject data = new JSONObject();
            data.put("3",num[0]);
            data.put("4",num[1]);
            data.put("5",num[2]);
            data.put("6",num[3]);
            data.put("7",num[4]);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取记录成功");
        }catch (Exception e){
            System.out.println(e.getMessage());
            ret.setStatus(1);
            ret.setMessage("获取记录失败");
        }
        return ret;
    }
}
