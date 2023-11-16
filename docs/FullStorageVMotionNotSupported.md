# FullStorageVMotionNotSupported

An operation on a powered-on virtual machine requests a simultaneous change of storage location and execution host, but the host does not have that capability.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.full_storage_v_motion_not_supported import FullStorageVMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of FullStorageVMotionNotSupported from a JSON string
full_storage_v_motion_not_supported_instance = FullStorageVMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print FullStorageVMotionNotSupported.to_json()

# convert the object into a dict
full_storage_v_motion_not_supported_dict = full_storage_v_motion_not_supported_instance.to_dict()
# create an instance of FullStorageVMotionNotSupported from a dict
full_storage_v_motion_not_supported_form_dict = full_storage_v_motion_not_supported.from_dict(full_storage_v_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


