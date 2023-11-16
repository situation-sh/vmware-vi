# ArrayOfLatencySensitivity

A boxed array of *LatencySensitivity*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LatencySensitivity]**](LatencySensitivity.md) |  | 

## Example

```python
from vmware_vi.models.array_of_latency_sensitivity import ArrayOfLatencySensitivity

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLatencySensitivity from a JSON string
array_of_latency_sensitivity_instance = ArrayOfLatencySensitivity.from_json(json)
# print the JSON string representation of the object
print ArrayOfLatencySensitivity.to_json()

# convert the object into a dict
array_of_latency_sensitivity_dict = array_of_latency_sensitivity_instance.to_dict()
# create an instance of ArrayOfLatencySensitivity from a dict
array_of_latency_sensitivity_form_dict = array_of_latency_sensitivity.from_dict(array_of_latency_sensitivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


