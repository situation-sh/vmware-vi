# SwitchNotInUpgradeMode

Thrown if an operation is not supported while the DistributedVirtualSwitch is not in upgrade mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.switch_not_in_upgrade_mode import SwitchNotInUpgradeMode

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchNotInUpgradeMode from a JSON string
switch_not_in_upgrade_mode_instance = SwitchNotInUpgradeMode.from_json(json)
# print the JSON string representation of the object
print SwitchNotInUpgradeMode.to_json()

# convert the object into a dict
switch_not_in_upgrade_mode_dict = switch_not_in_upgrade_mode_instance.to_dict()
# create an instance of SwitchNotInUpgradeMode from a dict
switch_not_in_upgrade_mode_form_dict = switch_not_in_upgrade_mode.from_dict(switch_not_in_upgrade_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


