package com.example.back.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.entity.OlderPerson;
import com.example.back.service.OlderPersonService;
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
public class OlderPersonController {
    @Autowired
    private OlderPersonService olderPersonService;
    /**
     * 添加老人信息
     * @param jsonObject
     * @return
     */
    @RequestMapping("/addoldmaninfo")
    public Return addOldmanInfo(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try{
            String username=jsonObject.getString("username");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String checkin_date=jsonObject.getString("checkin_date");
            String checkout_date=jsonObject.getString("checkout_date");
            String profile_photo="/";
            String room_number=jsonObject.getString("room_number");
            Date date = new Date();
            Timestamp CREATED = new Timestamp(date.getTime());
            int id=olderPersonService.getid().intValue();
            olderPersonService.addOlderInfo(id+1,username,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,room_number,CREATED);
            ret.setStatus(0);
            ret.setMessage(Integer.toString(id+1));
        }catch (Exception e){
            System.out.println(e.getMessage());
            ret.setStatus(1);
            ret.setMessage("添加老人信息失败");
        }
        return ret;
    }

    /**
     * 通过id获取老人信息
     * @param
     * @return
     */
    @RequestMapping("/getoldmaninfo/{id}")
    public Return getOldmanInfo(@PathVariable int id){
        Return ret = new Return();
        try{
            int ID=id;
            OlderPerson ans=olderPersonService.getOlderInfo(ID);
            JSONObject data = new JSONObject();
            data.put("Info",ans);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取老人信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("获取老人信息失败");
        }
        return ret;
    }

    /**
     * 获取所有老人信息
     * @param
     * @return
     */
    @RequestMapping("/getalloldmaninfo")
    public Return getAllOldmanInfo(){
        Return ret=new Return();
        try{
            List<OlderPerson> ans=olderPersonService.getalloldmaninfo();
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
     * 修改老人信息
     * @param jsonObject
     * @return
     */
    @RequestMapping("/updateoldmaninfo/{id}")
    public Return updateOldmanInfo(@PathVariable int id,@RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int ID=id;
            String username=jsonObject.getString("username");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String checkin_date=jsonObject.getString("checkin_date");
            String checkout_date=jsonObject.getString("checkout_date");
            String profile_photo=jsonObject.getString("profile_photo");
            String room_number=jsonObject.getString("room_number");
            Date date = new Date();
            Timestamp UPDATED = new Timestamp(date.getTime());
            olderPersonService.updateOldmanInfo(ID,username,gender,phone,id_card,birthday,checkin_date,checkout_date,profile_photo,room_number,UPDATED);
            ret.setStatus(0);
            ret.setMessage("修改老人信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("修改老人信息失败");
        }
        return ret;
    }

    /**
     * 删除老人信息
     * @param
     * @return
     */
    @RequestMapping(value = "/deleteoldmaninfo/{id}", method = RequestMethod.DELETE)
    public Return deleteoldmaninfo(@PathVariable int id){
        Return ret=new Return();
        try{
            int ID=id;
            olderPersonService.deleteoldmaninfo(ID);
            ret.setStatus(0);
            ret.setMessage("删除老人信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("删除老人信息失败");
        }
        return ret;
    }

    /**
     * 修改老人头像
     * @param jsonObject
     * @return
     */
    @RequestMapping("/setoldertag")
    public Return setTag(@RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int id=Integer.parseInt(jsonObject.getString("id"));
            String profile_photo=jsonObject.getString("profile_photo");
            olderPersonService.setTag(id,profile_photo);
            ret.setStatus(0);
            ret.setMessage("更新头像成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("更新头像失败");
        }
        return ret;
    }

    /**
     * 报表信息：老人年龄分布
     * @param
     * @return
     */
    @RequestMapping("/oldrecord")
    public Return oldrecord(){
        Return ret=new Return();
        try{
            List<String> string=olderPersonService.oldrecord();
            int age[]=new int[string.size()];
            int agenum[]=new int[5];
            int i=0;
            for(String s:string){
                String[] sub=s.split("-");
                age[i]=Integer.parseInt(sub[0]);
                age[i]=2021-age[i];
                i++;
            }
            for(int a:agenum){
                a=0;
            }
            for(int a:age){
                //System.out.println(a);
                if(a<=60){
                    agenum[0]+=1;
                }else if(a>60&&a<=70){
                    agenum[1]+=1;
                }else if(a>70&&a<=80){
                    agenum[2]+=1;
                }else if(a>80&&a<=90){
                    agenum[3]+=1;
                }else if(a>90){
                    agenum[4]+=1;
                }
            }
            JSONObject data = new JSONObject();
            data.put("<60",agenum[0]);
            data.put("60-70",agenum[1]);
            data.put("70-80",agenum[2]);
            data.put("80-90",agenum[3]);
            data.put(">90",agenum[4]);
            ret.setData(data);
            ret.setStatus(0);
            ret.setMessage("获取成功");
        }catch (Exception e){
            System.out.println(e.getMessage());
            ret.setStatus(1);
            ret.setMessage("操作失败！");
        }
        return ret;
    }
}
