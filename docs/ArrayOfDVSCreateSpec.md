# ArrayOfDVSCreateSpec

A boxed array of *DVSCreateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSCreateSpec]**](DVSCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_create_spec import ArrayOfDVSCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSCreateSpec from a JSON string
array_of_dvs_create_spec_instance = ArrayOfDVSCreateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSCreateSpec.to_json()

# convert the object into a dict
array_of_dvs_create_spec_dict = array_of_dvs_create_spec_instance.to_dict()
# create an instance of ArrayOfDVSCreateSpec from a dict
array_of_dvs_create_spec_form_dict = array_of_dvs_create_spec.from_dict(array_of_dvs_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


