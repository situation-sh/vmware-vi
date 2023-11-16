# ArrayOfDVSCapability

A boxed array of *DVSCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSCapability]**](DVSCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_capability import ArrayOfDVSCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSCapability from a JSON string
array_of_dvs_capability_instance = ArrayOfDVSCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSCapability.to_json()

# convert the object into a dict
array_of_dvs_capability_dict = array_of_dvs_capability_instance.to_dict()
# create an instance of ArrayOfDVSCapability from a dict
array_of_dvs_capability_form_dict = array_of_dvs_capability.from_dict(array_of_dvs_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


