# HostLowLevelProvisioningManagerFileDeleteResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_file_delete_result import HostLowLevelProvisioningManagerFileDeleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerFileDeleteResult from a JSON string
host_low_level_provisioning_manager_file_delete_result_instance = HostLowLevelProvisioningManagerFileDeleteResult.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerFileDeleteResult.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_file_delete_result_dict = host_low_level_provisioning_manager_file_delete_result_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerFileDeleteResult from a dict
host_low_level_provisioning_manager_file_delete_result_form_dict = host_low_level_provisioning_manager_file_delete_result.from_dict(host_low_level_provisioning_manager_file_delete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


