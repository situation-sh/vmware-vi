# MissingPowerOffConfiguration

Attempting to power-off a vApp for which no virtual machines has been configured to power off.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.missing_power_off_configuration import MissingPowerOffConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MissingPowerOffConfiguration from a JSON string
missing_power_off_configuration_instance = MissingPowerOffConfiguration.from_json(json)
# print the JSON string representation of the object
print MissingPowerOffConfiguration.to_json()

# convert the object into a dict
missing_power_off_configuration_dict = missing_power_off_configuration_instance.to_dict()
# create an instance of MissingPowerOffConfiguration from a dict
missing_power_off_configuration_form_dict = missing_power_off_configuration.from_dict(missing_power_off_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


