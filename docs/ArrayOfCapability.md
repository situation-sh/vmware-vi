# ArrayOfCapability

A boxed array of *Capability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Capability]**](Capability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_capability import ArrayOfCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCapability from a JSON string
array_of_capability_instance = ArrayOfCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfCapability.to_json()

# convert the object into a dict
array_of_capability_dict = array_of_capability_instance.to_dict()
# create an instance of ArrayOfCapability from a dict
array_of_capability_form_dict = array_of_capability.from_dict(array_of_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


