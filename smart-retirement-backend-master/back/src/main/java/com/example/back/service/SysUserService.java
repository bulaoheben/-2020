package com.example.back.service;

import com.example.back.entity.SysUser;
import com.example.back.mapper.SysUserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;

@Service
public class SysUserService {
    @Autowired
    SysUserMapper sysUserMapper;

    public SysUser Login(String UserName,String Password){return sysUserMapper.Login(UserName,Password);}
    public void Register(String UserName, String Password, String REAL_NAME, String SEX, String EMAIL, String PHONE, String MOBILE, Timestamp CREATED){sysUserMapper.Register(UserName,Password,REAL_NAME,SEX,EMAIL,PHONE,MOBILE,CREATED);}
    public void updateadmininfo(int ID,String UserName, String REAL_NAME, String SEX, String EMAIL, String PHONE, String MOBILE, String logoimage, Timestamp UPDATED){
        sysUserMapper.updateadmininfo(ID,UserName,REAL_NAME,SEX,EMAIL,PHONE,MOBILE,logoimage,UPDATED);
    }
    public void updateadminpassword(int ID,String Password,Timestamp UPDATED){
        sysUserMapper.updateadminpassword(ID,Password,UPDATED);
    }
    public int getid(String UserName,String Password){
        return sysUserMapper.getid(UserName,Password);
    }
    public SysUser get(int ID){
        return sysUserMapper.get(ID);
    }
}
