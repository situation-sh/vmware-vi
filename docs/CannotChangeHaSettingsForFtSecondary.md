# CannotChangeHaSettingsForFtSecondary

This fault is used to report that the HA settings cannot be modified for a FT secondary virtual machine  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | Name of the FT secondary virtual machine  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.cannot_change_ha_settings_for_ft_secondary import CannotChangeHaSettingsForFtSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of CannotChangeHaSettingsForFtSecondary from a JSON string
cannot_change_ha_settings_for_ft_secondary_instance = CannotChangeHaSettingsForFtSecondary.from_json(json)
# print the JSON string representation of the object
print CannotChangeHaSettingsForFtSecondary.to_json()

# convert the object into a dict
cannot_change_ha_settings_for_ft_secondary_dict = cannot_change_ha_settings_for_ft_secondary_instance.to_dict()
# create an instance of CannotChangeHaSettingsForFtSecondary from a dict
cannot_change_ha_settings_for_ft_secondary_form_dict = cannot_change_ha_settings_for_ft_secondary.from_dict(cannot_change_ha_settings_for_ft_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


