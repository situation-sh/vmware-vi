# ArrayOfMissingPowerOffConfiguration

A boxed array of *MissingPowerOffConfiguration*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MissingPowerOffConfiguration]**](MissingPowerOffConfiguration.md) |  | 

## Example

```python
from vmware_vi.models.array_of_missing_power_off_configuration import ArrayOfMissingPowerOffConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMissingPowerOffConfiguration from a JSON string
array_of_missing_power_off_configuration_instance = ArrayOfMissingPowerOffConfiguration.from_json(json)
# print the JSON string representation of the object
print ArrayOfMissingPowerOffConfiguration.to_json()

# convert the object into a dict
array_of_missing_power_off_configuration_dict = array_of_missing_power_off_configuration_instance.to_dict()
# create an instance of ArrayOfMissingPowerOffConfiguration from a dict
array_of_missing_power_off_configuration_form_dict = array_of_missing_power_off_configuration.from_dict(array_of_missing_power_off_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


