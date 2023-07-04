package com.example.back.mapper;

import com.example.back.entity.SysUser;
import org.springframework.stereotype.Repository;

import java.sql.Timestamp;


@Repository
public interface SysUserMapper {
    SysUser Login(String UserName,String Password);
    void Register(String UserName, String Password, String REAL_NAME, String SEX, String EMAIL, String PHONE, String MOBILE, Timestamp CREATED);
    void updateadmininfo(int ID,String UserName, String REAL_NAME, String SEX, String EMAIL, String PHONE, String MOBILE, String logoimage, Timestamp UPDATED);
    void updateadminpassword(int ID,String Password,Timestamp UPDATED);
    int getid(String UserName,String Password);
    SysUser get(int ID);
}
