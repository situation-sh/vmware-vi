# HostSystemResourceInfo

The SystemResourceInfo data object describes the configuration of a single system resource group.  System resource groups are analogous to *ResourcePool* objects for virtual machines; however, their structure is fixed and groups may not be created nor destroyed, only configured. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | ID of the system resource group.  | 
**config** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | [optional] 
**child** | [**List[HostSystemResourceInfo]**](HostSystemResourceInfo.md) | List of child resource groups.  | [optional] 

## Example

```python
from vmware_vi.models.host_system_resource_info import HostSystemResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemResourceInfo from a JSON string
host_system_resource_info_instance = HostSystemResourceInfo.from_json(json)
# print the JSON string representation of the object
print HostSystemResourceInfo.to_json()

# convert the object into a dict
host_system_resource_info_dict = host_system_resource_info_instance.to_dict()
# create an instance of HostSystemResourceInfo from a dict
host_system_resource_info_form_dict = host_system_resource_info.from_dict(host_system_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


