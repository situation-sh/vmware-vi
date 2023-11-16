# HostFaultToleranceManagerComponentHealthInfo

Data structure for component health information of a virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_storage_healthy** | **bool** | Whether the virtual machine can access the datastores configured.  ***Since:*** vSphere API 6.0  | 
**is_network_healthy** | **bool** | Whether the virtual machine can access the VM network configured.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_fault_tolerance_manager_component_health_info import HostFaultToleranceManagerComponentHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFaultToleranceManagerComponentHealthInfo from a JSON string
host_fault_tolerance_manager_component_health_info_instance = HostFaultToleranceManagerComponentHealthInfo.from_json(json)
# print the JSON string representation of the object
print HostFaultToleranceManagerComponentHealthInfo.to_json()

# convert the object into a dict
host_fault_tolerance_manager_component_health_info_dict = host_fault_tolerance_manager_component_health_info_instance.to_dict()
# create an instance of HostFaultToleranceManagerComponentHealthInfo from a dict
host_fault_tolerance_manager_component_health_info_form_dict = host_fault_tolerance_manager_component_health_info.from_dict(host_fault_tolerance_manager_component_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


