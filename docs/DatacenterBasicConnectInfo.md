# DatacenterBasicConnectInfo

BasicConnectInfo consists of essential information about the host.  This is a subset of *HostConnectInfo* and contains the information which is relevant when it comes to dealing with a set of hosts.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target host.  ***Since:*** vSphere API 6.7.1  | [optional] 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 
**server_ip** | **str** | IP address of the VirtualCenter already managing this host, if any.  ***Since:*** vSphere API 6.7.1  | [optional] 
**num_vm** | **int** | Specifies the number of VMs on the host.  ***Since:*** vSphere API 6.7.1  | [optional] 
**num_powered_on_vm** | **int** | Specifies the number of powered-on VMs on the host.  ***Since:*** vSphere API 6.7.1  | [optional] 
**host_product_info** | [**AboutInfo**](AboutInfo.md) |  | [optional] 
**hardware_vendor** | **str** | Hardware vendor identification.  ***Since:*** vSphere API 6.7.1  | [optional] 
**hardware_model** | **str** | System model identification.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.datacenter_basic_connect_info import DatacenterBasicConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterBasicConnectInfo from a JSON string
datacenter_basic_connect_info_instance = DatacenterBasicConnectInfo.from_json(json)
# print the JSON string representation of the object
print DatacenterBasicConnectInfo.to_json()

# convert the object into a dict
datacenter_basic_connect_info_dict = datacenter_basic_connect_info_instance.to_dict()
# create an instance of DatacenterBasicConnectInfo from a dict
datacenter_basic_connect_info_form_dict = datacenter_basic_connect_info.from_dict(datacenter_basic_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


