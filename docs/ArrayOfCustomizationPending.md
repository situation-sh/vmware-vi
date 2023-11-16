# ArrayOfCustomizationPending

A boxed array of *CustomizationPending*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationPending]**](CustomizationPending.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_pending import ArrayOfCustomizationPending

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationPending from a JSON string
array_of_customization_pending_instance = ArrayOfCustomizationPending.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationPending.to_json()

# convert the object into a dict
array_of_customization_pending_dict = array_of_customization_pending_instance.to_dict()
# create an instance of ArrayOfCustomizationPending from a dict
array_of_customization_pending_form_dict = array_of_customization_pending.from_dict(array_of_customization_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


