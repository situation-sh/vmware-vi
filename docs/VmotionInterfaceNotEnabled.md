# VmotionInterfaceNotEnabled

This fault is thrown when the Vmotion Interface on this host is not enabled.  The Vmotion Interface is needed for waking up the host from standby mode.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmotion_interface_not_enabled import VmotionInterfaceNotEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of VmotionInterfaceNotEnabled from a JSON string
vmotion_interface_not_enabled_instance = VmotionInterfaceNotEnabled.from_json(json)
# print the JSON string representation of the object
print VmotionInterfaceNotEnabled.to_json()

# convert the object into a dict
vmotion_interface_not_enabled_dict = vmotion_interface_not_enabled_instance.to_dict()
# create an instance of VmotionInterfaceNotEnabled from a dict
vmotion_interface_not_enabled_form_dict = vmotion_interface_not_enabled.from_dict(vmotion_interface_not_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


