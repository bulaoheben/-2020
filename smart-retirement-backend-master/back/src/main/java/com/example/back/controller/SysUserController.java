package com.example.back.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.entity.SysUser;
import com.example.back.service.SysUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.sql.Timestamp;
import java.util.Date;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class SysUserController {

    @Autowired
    private SysUserService sysUserService;

    /**
     * 管理员登录系统
     * @param jsonObject
     * @return
     */
    @RequestMapping("/login")
    public Return Login(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try {
            String UserName=jsonObject.getString("UserName");
            String Password=jsonObject.getString("Password");
            SysUser user=sysUserService.Login(UserName,Password);
            if(user==null){
                ret.setStatus(1);
                ret.setMessage("账号或密码错误");
            }else{
                JSONObject data = new JSONObject();
                data.put("user",user);
                ret.setData(data);
                ret.setStatus(0);
                ret.setMessage("登录成功");
            }
        }catch (Exception e){
            System.out.println(e.toString());
            e.printStackTrace();
            ret.setStatus(1);
            ret.setMessage("登录失败");
        }
        return ret;
    }

    /**
     * 注册
     * @param jsonObject
     * @return
     */
    @RequestMapping("//er")
    public Return register(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try {
            String UserName=jsonObject.getString("UserName");
            String Password=jsonObject.getString("Password");
            String REAL_NAME=jsonObject.getString("REAL_NAME");
            String SEX=jsonObject.getString("SEX");
            String EMAIL=jsonObject.getString("EMAIL");
            String PHONE=jsonObject.getString("PHONE");
            String MOBILE=jsonObject.getString("MOBILE");
            Date date = new Date();
            Timestamp CREATED = new Timestamp(date.getTime());
            sysUserService.Register(UserName,Password,REAL_NAME,SEX,EMAIL,PHONE,MOBILE,CREATED);
            ret.setStatus(0);
            ret.setMessage("注册成功");
        }catch (Exception e){
        	e.printStackTrace();
            ret.setStatus(1);
            ret.setMessage("注册失败");
        }
        return ret;
    }

    /**
     * 管理员信息修改
     * @param jsonObject
     * @return
     */
    @RequestMapping("/updateadmininfo")
    public Return updateadmininfo(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try {
            int ID=Integer.parseInt(jsonObject.getString("ID"));
            String UserName=jsonObject.getString("UserName");
            String REAL_NAME=jsonObject.getString("REAL_NAME");
            String SEX=jsonObject.getString("SEX");
            String EMAIL=jsonObject.getString("EMAIL");
            String PHONE=jsonObject.getString("PHONE");
            String MOBILE=jsonObject.getString("MOBILE");
            String logoimage=jsonObject.getString("logoimage");
            Date date = new Date();
            Timestamp UPDATED = new Timestamp(date.getTime());
            sysUserService.updateadmininfo(ID,UserName,REAL_NAME,SEX,EMAIL,PHONE,MOBILE,logoimage,UPDATED);
            ret.setStatus(0);
            ret.setMessage("修改成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("修改失败");
        }
        return ret;
    }

    /**
     * 管理员密码修改
     * @param jsonObject
     * @return
     */
    @RequestMapping("/updateadminpassword")
    public Return updateadminpassword(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try {
            int ID=Integer.parseInt(jsonObject.getString("ID"));
            String Password=jsonObject.getString("Password");
            Date date = new Date();
            Timestamp UPDATED = new Timestamp(date.getTime());
            sysUserService.updateadminpassword(ID,Password,UPDATED);
            ret.setStatus(0);
            ret.setMessage("修改成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("修改失败");
        }
        return ret;
    }

    //flask demo
    //后面改成和前端录入信息的接口，传入信息是OSS存放的文件夹
    @RequestMapping("/test")
    public void sendPostRequest(){
        String url = "http://192.168.0.149:5000/FLASK-SERVER/collecting_faces";
        JSONObject jsonObject1=new JSONObject();
        jsonObject1.put("id", "czm");
        HttpUtil.doPost(url,jsonObject1);
    }
}