# ArrayOfPowerSystemCapability

A boxed array of *PowerSystemCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PowerSystemCapability]**](PowerSystemCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_power_system_capability import ArrayOfPowerSystemCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPowerSystemCapability from a JSON string
array_of_power_system_capability_instance = ArrayOfPowerSystemCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfPowerSystemCapability.to_json()

# convert the object into a dict
array_of_power_system_capability_dict = array_of_power_system_capability_instance.to_dict()
# create an instance of ArrayOfPowerSystemCapability from a dict
array_of_power_system_capability_form_dict = array_of_power_system_capability.from_dict(array_of_power_system_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


