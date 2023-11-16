# VMotionAcrossNetworkNotSupported

An operation on a powered-on virtual machine requests a change of networks, but the host does not have that capability.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_motion_across_network_not_supported import VMotionAcrossNetworkNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionAcrossNetworkNotSupported from a JSON string
v_motion_across_network_not_supported_instance = VMotionAcrossNetworkNotSupported.from_json(json)
# print the JSON string representation of the object
print VMotionAcrossNetworkNotSupported.to_json()

# convert the object into a dict
v_motion_across_network_not_supported_dict = v_motion_across_network_not_supported_instance.to_dict()
# create an instance of VMotionAcrossNetworkNotSupported from a dict
v_motion_across_network_not_supported_form_dict = v_motion_across_network_not_supported.from_dict(v_motion_across_network_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


