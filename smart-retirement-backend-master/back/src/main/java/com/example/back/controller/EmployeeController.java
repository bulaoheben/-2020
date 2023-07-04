package com.example.back.controller;

import com.alibaba.fastjson.JSONObject;
import com.example.back.Return;
import com.example.back.entity.Employee;
import com.example.back.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.sql.Timestamp;
import java.util.Date;
import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("/back")
public class EmployeeController {
    @Autowired
    private EmployeeService employeeService;

    /**
     * 添加工作人员信息
     * @param jsonObject
     * @return
     */
    @RequestMapping("/addemployeeinfo")
    public Return addEmployeeInfo(@RequestBody JSONObject jsonObject){
        Return ret = new Return();
        try{
            String name=jsonObject.getString("username");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String hire_date=jsonObject.getString("hire_date");
            String resign_date=jsonObject.getString("resign_date");
            String profile_photo="/";
            Date date = new Date();
            Timestamp CREATED = new Timestamp(date.getTime());
            int id=employeeService.getid().intValue();
            employeeService.addEmployeeInfo(id+1,name,gender,phone,id_card,birthday,hire_date,resign_date,profile_photo,CREATED);
            ret.setStatus(0);
            ret.setMessage(Integer.toString(id+1));
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("添加工作人员信息失败");
        }
        return ret;
    }

    /**
     * 用id获取某工作人员信息
     * @param id
     * @return
     */
    @RequestMapping("/getemployeeinfo/{id}")
    public Return getEmployeeInfo(@PathVariable int id){
        Return ret = new Return();
        try{
            Employee ans=employeeService.getEmployeeInfo(id);
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
     * 获取所有工作人员信息
     * @param
     * @return
     */
    @RequestMapping("/getallemployeeinfo")
    public Return getAllEmployeeInfo(){
        Return ret=new Return();
        try{
            List<Employee> ans=employeeService.getallemployeeinfo();
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

    /**
     * 更新某工作人员信息
     * @param id，jsonObject
     * @return
     */
    @RequestMapping("/updateemployeeinfo/{id}")
    public Return updateEmployeeInfo(@PathVariable int id, @RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int ID=id;
            String name=jsonObject.getString("username");
            String gender=jsonObject.getString("gender");
            String phone=jsonObject.getString("phone");
            String id_card=jsonObject.getString("id_card");
            String birthday=jsonObject.getString("birthday");
            String hire_date=jsonObject.getString("hire_date");
            String resign_date=jsonObject.getString("resign_date");
            String profile_photo=jsonObject.getString("profile_photo");
            Date date = new Date();
            Timestamp UPDATED = new Timestamp(date.getTime());
            employeeService.updateemployeeInfo(ID,name,gender,phone,id_card,birthday,hire_date,resign_date,profile_photo,UPDATED);
            ret.setStatus(0);
            ret.setMessage("更新工作人员信息成功");
        }catch (Exception e){
            System.out.println(e.getMessage());
            ret.setStatus(1);
            ret.setMessage("更新工作人员信息失败");
        }
        return ret;
    }

    /**
     * 用id删除某工作人员信息
     * @param id
     * @return
     */
    @RequestMapping("/deleteemployeeinfo/{id}")
    public Return deleteemployeeinfo(@PathVariable int id){
        Return ret=new Return();
        try{
            int ID=id;
            employeeService.deleteemployeeinfo(ID);
            ret.setStatus(0);
            ret.setMessage("删除工作人员信息成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("删除工作人员信息失败");
        }
        return ret;
    }

    /**
     * 更换工作人员头像
     * @param jsonObject
     * @return
     */
    @RequestMapping("/setemployeetag")
    public Return setTag(@RequestBody JSONObject jsonObject){
        Return ret=new Return();
        try{
            int id=Integer.parseInt(jsonObject.getString("id"));
            String profile_photo=jsonObject.getString("profile_photo");
            employeeService.setTag(id,profile_photo);
            ret.setStatus(0);
            ret.setMessage("更换头像成功");
        }catch (Exception e){
            ret.setStatus(1);
            ret.setMessage("更换头像失败");
        }
        return ret;
    }

    /**
     * 报表信息:工作人员入职离职时间统计
     * @param
     * @return
     */
    @RequestMapping("/employeerecord")
    public Return employeerecord(){
        Return ret=new Return();
        try{
            List<String> employeein=employeeService.employeerecordin();
            List<String> employeeout=employeeService.employeerecordout();
            int in[]=new int[employeein.size()];
            int out[]=new int[employeeout.size()];
            int i=0;
            int j=0;
            for(String s1:employeein){
                String[] sub=s1.split("-");
                in[i]=Integer.parseInt(sub[1]);
                i++;
            }
            for(String s2:employeeout){
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
