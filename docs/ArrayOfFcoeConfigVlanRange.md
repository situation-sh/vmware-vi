# ArrayOfFcoeConfigVlanRange

A boxed array of *FcoeConfigVlanRange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FcoeConfigVlanRange]**](FcoeConfigVlanRange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fcoe_config_vlan_range import ArrayOfFcoeConfigVlanRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFcoeConfigVlanRange from a JSON string
array_of_fcoe_config_vlan_range_instance = ArrayOfFcoeConfigVlanRange.from_json(json)
# print the JSON string representation of the object
print ArrayOfFcoeConfigVlanRange.to_json()

# convert the object into a dict
array_of_fcoe_config_vlan_range_dict = array_of_fcoe_config_vlan_range_instance.to_dict()
# create an instance of ArrayOfFcoeConfigVlanRange from a dict
array_of_fcoe_config_vlan_range_form_dict = array_of_fcoe_config_vlan_range.from_dict(array_of_fcoe_config_vlan_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


