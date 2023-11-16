# HostCpuPowerManagementInfo

The CpuPowerManagementInfo data object type describes supported power management and current policy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_policy** | **str** | Information about current CPU power management policy.  ***Since:*** vSphere API 4.0  | [optional] 
**hardware_support** | **str** | Information about supported CPU power management.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_cpu_power_management_info import HostCpuPowerManagementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostCpuPowerManagementInfo from a JSON string
host_cpu_power_management_info_instance = HostCpuPowerManagementInfo.from_json(json)
# print the JSON string representation of the object
print HostCpuPowerManagementInfo.to_json()

# convert the object into a dict
host_cpu_power_management_info_dict = host_cpu_power_management_info_instance.to_dict()
# create an instance of HostCpuPowerManagementInfo from a dict
host_cpu_power_management_info_form_dict = host_cpu_power_management_info.from_dict(host_cpu_power_management_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


