# ArrayOfCustomizationSucceeded

A boxed array of *CustomizationSucceeded*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationSucceeded]**](CustomizationSucceeded.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_succeeded import ArrayOfCustomizationSucceeded

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationSucceeded from a JSON string
array_of_customization_succeeded_instance = ArrayOfCustomizationSucceeded.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationSucceeded.to_json()

# convert the object into a dict
array_of_customization_succeeded_dict = array_of_customization_succeeded_instance.to_dict()
# create an instance of ArrayOfCustomizationSucceeded from a dict
array_of_customization_succeeded_form_dict = array_of_customization_succeeded.from_dict(array_of_customization_succeeded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


