# ArrayOfCustomizationPrefixName

A boxed array of *CustomizationPrefixName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationPrefixName]**](CustomizationPrefixName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_prefix_name import ArrayOfCustomizationPrefixName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationPrefixName from a JSON string
array_of_customization_prefix_name_instance = ArrayOfCustomizationPrefixName.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationPrefixName.to_json()

# convert the object into a dict
array_of_customization_prefix_name_dict = array_of_customization_prefix_name_instance.to_dict()
# create an instance of ArrayOfCustomizationPrefixName from a dict
array_of_customization_prefix_name_form_dict = array_of_customization_prefix_name.from_dict(array_of_customization_prefix_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


