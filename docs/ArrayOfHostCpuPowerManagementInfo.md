# ArrayOfHostCpuPowerManagementInfo

A boxed array of *HostCpuPowerManagementInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCpuPowerManagementInfo]**](HostCpuPowerManagementInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cpu_power_management_info import ArrayOfHostCpuPowerManagementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCpuPowerManagementInfo from a JSON string
array_of_host_cpu_power_management_info_instance = ArrayOfHostCpuPowerManagementInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCpuPowerManagementInfo.to_json()

# convert the object into a dict
array_of_host_cpu_power_management_info_dict = array_of_host_cpu_power_management_info_instance.to_dict()
# create an instance of ArrayOfHostCpuPowerManagementInfo from a dict
array_of_host_cpu_power_management_info_form_dict = array_of_host_cpu_power_management_info.from_dict(array_of_host_cpu_power_management_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


