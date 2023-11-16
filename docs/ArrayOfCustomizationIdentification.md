# ArrayOfCustomizationIdentification

A boxed array of *CustomizationIdentification*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationIdentification]**](CustomizationIdentification.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_identification import ArrayOfCustomizationIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationIdentification from a JSON string
array_of_customization_identification_instance = ArrayOfCustomizationIdentification.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationIdentification.to_json()

# convert the object into a dict
array_of_customization_identification_dict = array_of_customization_identification_instance.to_dict()
# create an instance of ArrayOfCustomizationIdentification from a dict
array_of_customization_identification_form_dict = array_of_customization_identification.from_dict(array_of_customization_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


