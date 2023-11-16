# VMotionProtocolIncompatible

VMotion protocol version incompatibility prevents VMotion from the virtual machine's current host to the requested destination host.  (VMotion in the other direction may or may not be supported.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_motion_protocol_incompatible import VMotionProtocolIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionProtocolIncompatible from a JSON string
v_motion_protocol_incompatible_instance = VMotionProtocolIncompatible.from_json(json)
# print the JSON string representation of the object
print VMotionProtocolIncompatible.to_json()

# convert the object into a dict
v_motion_protocol_incompatible_dict = v_motion_protocol_incompatible_instance.to_dict()
# create an instance of VMotionProtocolIncompatible from a dict
v_motion_protocol_incompatible_form_dict = v_motion_protocol_incompatible.from_dict(v_motion_protocol_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


