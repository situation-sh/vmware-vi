# ArrayOfCustomizationSpecInfo

A boxed array of *CustomizationSpecInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationSpecInfo]**](CustomizationSpecInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_spec_info import ArrayOfCustomizationSpecInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationSpecInfo from a JSON string
array_of_customization_spec_info_instance = ArrayOfCustomizationSpecInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationSpecInfo.to_json()

# convert the object into a dict
array_of_customization_spec_info_dict = array_of_customization_spec_info_instance.to_dict()
# create an instance of ArrayOfCustomizationSpecInfo from a dict
array_of_customization_spec_info_form_dict = array_of_customization_spec_info.from_dict(array_of_customization_spec_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


