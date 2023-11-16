# VMotionNotSupported

The source or the destination host does not support VMotion.  This is an error only when migrating a powered-on virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_motion_not_supported import VMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionNotSupported from a JSON string
v_motion_not_supported_instance = VMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print VMotionNotSupported.to_json()

# convert the object into a dict
v_motion_not_supported_dict = v_motion_not_supported_instance.to_dict()
# create an instance of VMotionNotSupported from a dict
v_motion_not_supported_form_dict = v_motion_not_supported.from_dict(v_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


