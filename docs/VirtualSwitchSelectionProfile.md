# VirtualSwitchSelectionProfile

The *VirtualSwitchSelectionProfile* data object represents the virtual switch that is connected to a port group.  The *ApplyProfile.policy* property contains the configuration data values for the virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_switch_selection_profile import VirtualSwitchSelectionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSwitchSelectionProfile from a JSON string
virtual_switch_selection_profile_instance = VirtualSwitchSelectionProfile.from_json(json)
# print the JSON string representation of the object
print VirtualSwitchSelectionProfile.to_json()

# convert the object into a dict
virtual_switch_selection_profile_dict = virtual_switch_selection_profile_instance.to_dict()
# create an instance of VirtualSwitchSelectionProfile from a dict
virtual_switch_selection_profile_form_dict = virtual_switch_selection_profile.from_dict(virtual_switch_selection_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


