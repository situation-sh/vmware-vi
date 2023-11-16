# VMotionNotConfigured

A VMotion interface is not configured (or is misconfigured) on either the source or destination host.  This is an error only when migrating a powered-on virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_motion_not_configured import VMotionNotConfigured

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionNotConfigured from a JSON string
v_motion_not_configured_instance = VMotionNotConfigured.from_json(json)
# print the JSON string representation of the object
print VMotionNotConfigured.to_json()

# convert the object into a dict
v_motion_not_configured_dict = v_motion_not_configured_instance.to_dict()
# create an instance of VMotionNotConfigured from a dict
v_motion_not_configured_form_dict = v_motion_not_configured.from_dict(v_motion_not_configured_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


