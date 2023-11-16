# StorageVMotionNotSupported

An operation on a powered-on virtual machine requests a change of storage location, but the host does not have that capability.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_v_motion_not_supported import StorageVMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVMotionNotSupported from a JSON string
storage_v_motion_not_supported_instance = StorageVMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print StorageVMotionNotSupported.to_json()

# convert the object into a dict
storage_v_motion_not_supported_dict = storage_v_motion_not_supported_instance.to_dict()
# create an instance of StorageVMotionNotSupported from a dict
storage_v_motion_not_supported_form_dict = storage_v_motion_not_supported.from_dict(storage_v_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


