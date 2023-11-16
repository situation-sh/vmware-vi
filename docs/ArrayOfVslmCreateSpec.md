# ArrayOfVslmCreateSpec

A boxed array of *VslmCreateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VslmCreateSpec]**](VslmCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vslm_create_spec import ArrayOfVslmCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVslmCreateSpec from a JSON string
array_of_vslm_create_spec_instance = ArrayOfVslmCreateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVslmCreateSpec.to_json()

# convert the object into a dict
array_of_vslm_create_spec_dict = array_of_vslm_create_spec_instance.to_dict()
# create an instance of ArrayOfVslmCreateSpec from a dict
array_of_vslm_create_spec_form_dict = array_of_vslm_create_spec.from_dict(array_of_vslm_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


