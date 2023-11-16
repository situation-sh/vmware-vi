# ArrayOfCustomizationName

A boxed array of *CustomizationName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationName]**](CustomizationName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_name import ArrayOfCustomizationName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationName from a JSON string
array_of_customization_name_instance = ArrayOfCustomizationName.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationName.to_json()

# convert the object into a dict
array_of_customization_name_dict = array_of_customization_name_instance.to_dict()
# create an instance of ArrayOfCustomizationName from a dict
array_of_customization_name_form_dict = array_of_customization_name.from_dict(array_of_customization_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


