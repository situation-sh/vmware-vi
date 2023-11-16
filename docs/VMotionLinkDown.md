# VMotionLinkDown

The VMotion interface does not have any operational physical links associated with it.  This is an error for migrating powered-on virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Name of the network being used for the VMotion interface.  | 

## Example

```python
from vmware_vi.models.v_motion_link_down import VMotionLinkDown

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionLinkDown from a JSON string
v_motion_link_down_instance = VMotionLinkDown.from_json(json)
# print the JSON string representation of the object
print VMotionLinkDown.to_json()

# convert the object into a dict
v_motion_link_down_dict = v_motion_link_down_instance.to_dict()
# create an instance of VMotionLinkDown from a dict
v_motion_link_down_form_dict = v_motion_link_down.from_dict(v_motion_link_down_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


