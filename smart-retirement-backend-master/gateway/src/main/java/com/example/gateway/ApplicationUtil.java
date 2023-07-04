package com.example.gateway;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.discovery.DiscoveryClient;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Component
public class ApplicationUtil {

    @Autowired
    private DiscoveryClient discoveryClient;

    public Map<String, List<ServiceInstance>> serviceUrl() {
        Map<String, List<ServiceInstance>> msl = new HashMap<String, List<ServiceInstance>>();
        List<String> services = discoveryClient.getServices();
        for (String service : services) {
            List<ServiceInstance> sis = discoveryClient.getInstances(service);
            msl.put(service, sis);
        }
        return msl;

    }

    public boolean isExitservice(String applicationName) {
        List<String> services = discoveryClient.getServices();
        for (String service : services) {
            if(service.toUpperCase().equals(applicationName.toUpperCase())) {
                return true;
            }
        }
        return false;
    }


}