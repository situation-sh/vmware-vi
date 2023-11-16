# ArrayOfCustomizationFailed

A boxed array of *CustomizationFailed*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationFailed]**](CustomizationFailed.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_failed import ArrayOfCustomizationFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationFailed from a JSON string
array_of_customization_failed_instance = ArrayOfCustomizationFailed.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationFailed.to_json()

# convert the object into a dict
array_of_customization_failed_dict = array_of_customization_failed_instance.to_dict()
# create an instance of ArrayOfCustomizationFailed from a dict
array_of_customization_failed_form_dict = array_of_customization_failed.from_dict(array_of_customization_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


