# ArrayOfCustomizationSpec

A boxed array of *CustomizationSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationSpec]**](CustomizationSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_spec import ArrayOfCustomizationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationSpec from a JSON string
array_of_customization_spec_instance = ArrayOfCustomizationSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationSpec.to_json()

# convert the object into a dict
array_of_customization_spec_dict = array_of_customization_spec_instance.to_dict()
# create an instance of ArrayOfCustomizationSpec from a dict
array_of_customization_spec_form_dict = array_of_customization_spec.from_dict(array_of_customization_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


