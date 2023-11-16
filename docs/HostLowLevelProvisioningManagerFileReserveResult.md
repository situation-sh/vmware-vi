# HostLowLevelProvisioningManagerFileReserveResult

A FileReserveResult object describles the information of a file reserved by the ReserveFiles method.  This includes the original input ReserveFiles method so that the caller can map the input with the reserved file. All paths will be the complete local path in the url format.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_name** | **str** |  | 
**parent_dir** | **str** |  | 
**reserved_name** | **str** |  | 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_file_reserve_result import HostLowLevelProvisioningManagerFileReserveResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerFileReserveResult from a JSON string
host_low_level_provisioning_manager_file_reserve_result_instance = HostLowLevelProvisioningManagerFileReserveResult.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerFileReserveResult.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_file_reserve_result_dict = host_low_level_provisioning_manager_file_reserve_result_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerFileReserveResult from a dict
host_low_level_provisioning_manager_file_reserve_result_form_dict = host_low_level_provisioning_manager_file_reserve_result.from_dict(host_low_level_provisioning_manager_file_reserve_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


