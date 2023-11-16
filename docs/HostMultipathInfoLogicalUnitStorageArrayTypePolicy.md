# HostMultipathInfoLogicalUnitStorageArrayTypePolicy

The *HostMultipathInfoLogicalUnitStorageArrayTypePolicy* data object describes a storage array type policy for for a device.  This policy determines how device I/O and management is performed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | String indicating the storage array type policy.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_multipath_info_logical_unit_storage_array_type_policy import HostMultipathInfoLogicalUnitStorageArrayTypePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoLogicalUnitStorageArrayTypePolicy from a JSON string
host_multipath_info_logical_unit_storage_array_type_policy_instance = HostMultipathInfoLogicalUnitStorageArrayTypePolicy.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoLogicalUnitStorageArrayTypePolicy.to_json()

# convert the object into a dict
host_multipath_info_logical_unit_storage_array_type_policy_dict = host_multipath_info_logical_unit_storage_array_type_policy_instance.to_dict()
# create an instance of HostMultipathInfoLogicalUnitStorageArrayTypePolicy from a dict
host_multipath_info_logical_unit_storage_array_type_policy_form_dict = host_multipath_info_logical_unit_storage_array_type_policy.from_dict(host_multipath_info_logical_unit_storage_array_type_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


