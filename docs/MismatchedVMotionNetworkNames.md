# MismatchedVMotionNetworkNames

The source and destination hosts do not use the same network name for their VMotion interfaces.  This is a warning for migrating powered-on virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_network** | **str** | The name of the network used by the source host VMotion interface.  | 
**dest_network** | **str** | The name of the network used by the destination host VMotion interface.  | 

## Example

```python
from vmware_vi.models.mismatched_v_motion_network_names import MismatchedVMotionNetworkNames

# TODO update the JSON string below
json = "{}"
# create an instance of MismatchedVMotionNetworkNames from a JSON string
mismatched_v_motion_network_names_instance = MismatchedVMotionNetworkNames.from_json(json)
# print the JSON string representation of the object
print MismatchedVMotionNetworkNames.to_json()

# convert the object into a dict
mismatched_v_motion_network_names_dict = mismatched_v_motion_network_names_instance.to_dict()
# create an instance of MismatchedVMotionNetworkNames from a dict
mismatched_v_motion_network_names_form_dict = mismatched_v_motion_network_names.from_dict(mismatched_v_motion_network_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


