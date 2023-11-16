# ArrayOfCustomizationUserData

A boxed array of *CustomizationUserData*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationUserData]**](CustomizationUserData.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_user_data import ArrayOfCustomizationUserData

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationUserData from a JSON string
array_of_customization_user_data_instance = ArrayOfCustomizationUserData.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationUserData.to_json()

# convert the object into a dict
array_of_customization_user_data_dict = array_of_customization_user_data_instance.to_dict()
# create an instance of ArrayOfCustomizationUserData from a dict
array_of_customization_user_data_form_dict = array_of_customization_user_data.from_dict(array_of_customization_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


