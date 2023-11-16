# HostLowLevelProvisioningManagerFileReserveSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_name** | **str** |  | 
**parent_dir** | **str** |  | 
**file_type** | **str** |  | 
**storage_profile** | **str** |  | 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_file_reserve_spec import HostLowLevelProvisioningManagerFileReserveSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerFileReserveSpec from a JSON string
host_low_level_provisioning_manager_file_reserve_spec_instance = HostLowLevelProvisioningManagerFileReserveSpec.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerFileReserveSpec.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_file_reserve_spec_dict = host_low_level_provisioning_manager_file_reserve_spec_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerFileReserveSpec from a dict
host_low_level_provisioning_manager_file_reserve_spec_form_dict = host_low_level_provisioning_manager_file_reserve_spec.from_dict(host_low_level_provisioning_manager_file_reserve_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


