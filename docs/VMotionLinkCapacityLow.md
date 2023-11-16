# VMotionLinkCapacityLow

The VMotion interface does not have the recommended capacity to support VMotion.  VMotion is supported on links that have a speed of at least 1000 Mbps and are full duplex. This is a warning for migrating powered-on virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Name of the network being used for the VMotion interface.  | 

## Example

```python
from vmware_vi.models.v_motion_link_capacity_low import VMotionLinkCapacityLow

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionLinkCapacityLow from a JSON string
v_motion_link_capacity_low_instance = VMotionLinkCapacityLow.from_json(json)
# print the JSON string representation of the object
print VMotionLinkCapacityLow.to_json()

# convert the object into a dict
v_motion_link_capacity_low_dict = v_motion_link_capacity_low_instance.to_dict()
# create an instance of VMotionLinkCapacityLow from a dict
v_motion_link_capacity_low_form_dict = v_motion_link_capacity_low.from_dict(v_motion_link_capacity_low_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


