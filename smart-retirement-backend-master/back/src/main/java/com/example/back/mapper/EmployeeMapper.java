package com.example.back.mapper;

import com.example.back.entity.Employee;
import com.example.back.entity.Volunteer;
import org.springframework.stereotype.Repository;

import java.sql.Timestamp;
import java.util.List;

@Repository
public interface EmployeeMapper {
    void addEmployeeInfo(int id,String name,String gender,String phone,String id_card,String birthday,String hire_date,String resign_date,String profile_photo,Timestamp CREATED);
    Employee getEmployeeInfo(int id);
    List<Employee> getallemployeeinfo();
    void updateemployeeInfo(int id,String name,String gender,String phone,String id_card,String birthday,String hire_date,String resign_date,String profile_photo,Timestamp UPDATED);
    void deleteemployeeinfo(int id);
    void autoSetTag(int id,String imgset_dir,String profile_photo);
    void setTag(int id,String profile_photo);
    List<String> employeerecordin();
    List<String> employeerecordout();
    Integer getid();
}
