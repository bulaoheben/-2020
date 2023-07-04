package com.example.back.service;

import com.example.back.entity.Employee;
import com.example.back.entity.Volunteer;
import com.example.back.mapper.EmployeeMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.List;

@Service
public class EmployeeService {
    @Autowired
    EmployeeMapper employeeMapper;

    public void addEmployeeInfo(int id,String name,String gender,String phone,String id_card,String birthday,String hire_date,String resign_date,String profile_photo,Timestamp CREATED){
        employeeMapper.addEmployeeInfo(id,name,gender,phone,id_card,birthday,hire_date,resign_date,profile_photo,CREATED);
    }
    public Employee getEmployeeInfo(int id){
        return employeeMapper.getEmployeeInfo(id);
    }
    public List<Employee> getallemployeeinfo(){
        return employeeMapper.getallemployeeinfo();
    }
    public void updateemployeeInfo(int id,String name,String gender,String phone,String id_card,String birthday,String hire_date,String resign_date,String profile_photo,Timestamp UPDATED){
        employeeMapper.updateemployeeInfo(id,name,gender,phone,id_card,birthday,hire_date,resign_date,profile_photo,UPDATED);
    }
    public void deleteemployeeinfo(int id){
        employeeMapper.deleteemployeeinfo(id);
    }
    public void autoSetTag(int id,String imgset_dir,String profile_photo){
        employeeMapper.autoSetTag(id,imgset_dir,profile_photo);
    }
    public void setTag(int id,String profile_photo){
        employeeMapper.setTag(id,profile_photo);
    }
    public List<String> employeerecordin(){
        return employeeMapper.employeerecordin();
    }
    public List<String> employeerecordout(){
        return employeeMapper.employeerecordout();
    }
    public Integer getid(){
    	if(employeeMapper.getid() == null)
    		return 0;
    	return employeeMapper.getid();
    }
}
