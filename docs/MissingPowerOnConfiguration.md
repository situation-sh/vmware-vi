# MissingPowerOnConfiguration

Attempting to power-on a vApp service for which no virtual machines has been configured to power on.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.missing_power_on_configuration import MissingPowerOnConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MissingPowerOnConfiguration from a JSON string
missing_power_on_configuration_instance = MissingPowerOnConfiguration.from_json(json)
# print the JSON string representation of the object
print MissingPowerOnConfiguration.to_json()

# convert the object into a dict
missing_power_on_configuration_dict = missing_power_on_configuration_instance.to_dict()
# create an instance of MissingPowerOnConfiguration from a dict
missing_power_on_configuration_form_dict = missing_power_on_configuration.from_dict(missing_power_on_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


