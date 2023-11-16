# ArrayOfVirtualSwitchProfile

A boxed array of *VirtualSwitchProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSwitchProfile]**](VirtualSwitchProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_switch_profile import ArrayOfVirtualSwitchProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSwitchProfile from a JSON string
array_of_virtual_switch_profile_instance = ArrayOfVirtualSwitchProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSwitchProfile.to_json()

# convert the object into a dict
array_of_virtual_switch_profile_dict = array_of_virtual_switch_profile_instance.to_dict()
# create an instance of ArrayOfVirtualSwitchProfile from a dict
array_of_virtual_switch_profile_form_dict = array_of_virtual_switch_profile.from_dict(array_of_virtual_switch_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


