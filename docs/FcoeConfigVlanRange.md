# FcoeConfigVlanRange

Used to represent inclusive intervals of VLAN IDs.  Valid VLAN IDs fall within the range \\[0,4094\\], and the low value of a VlanRange must be less than or equal to the high value.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_low** | **int** |  | 
**vlan_high** | **int** |  | 

## Example

```python
from vmware_vi.models.fcoe_config_vlan_range import FcoeConfigVlanRange

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeConfigVlanRange from a JSON string
fcoe_config_vlan_range_instance = FcoeConfigVlanRange.from_json(json)
# print the JSON string representation of the object
print FcoeConfigVlanRange.to_json()

# convert the object into a dict
fcoe_config_vlan_range_dict = fcoe_config_vlan_range_instance.to_dict()
# create an instance of FcoeConfigVlanRange from a dict
fcoe_config_vlan_range_form_dict = fcoe_config_vlan_range.from_dict(fcoe_config_vlan_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


