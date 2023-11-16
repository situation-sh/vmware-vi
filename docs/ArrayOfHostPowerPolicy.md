# ArrayOfHostPowerPolicy

A boxed array of *HostPowerPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPowerPolicy]**](HostPowerPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_power_policy import ArrayOfHostPowerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPowerPolicy from a JSON string
array_of_host_power_policy_instance = ArrayOfHostPowerPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPowerPolicy.to_json()

# convert the object into a dict
array_of_host_power_policy_dict = array_of_host_power_policy_instance.to_dict()
# create an instance of ArrayOfHostPowerPolicy from a dict
array_of_host_power_policy_form_dict = array_of_host_power_policy.from_dict(array_of_host_power_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


