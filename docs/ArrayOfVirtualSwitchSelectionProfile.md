# ArrayOfVirtualSwitchSelectionProfile

A boxed array of *VirtualSwitchSelectionProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSwitchSelectionProfile]**](VirtualSwitchSelectionProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_switch_selection_profile import ArrayOfVirtualSwitchSelectionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSwitchSelectionProfile from a JSON string
array_of_virtual_switch_selection_profile_instance = ArrayOfVirtualSwitchSelectionProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSwitchSelectionProfile.to_json()

# convert the object into a dict
array_of_virtual_switch_selection_profile_dict = array_of_virtual_switch_selection_profile_instance.to_dict()
# create an instance of ArrayOfVirtualSwitchSelectionProfile from a dict
array_of_virtual_switch_selection_profile_form_dict = array_of_virtual_switch_selection_profile.from_dict(array_of_virtual_switch_selection_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


