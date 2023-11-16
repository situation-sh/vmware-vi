# ArrayOfCustomizationSpecItem

A boxed array of *CustomizationSpecItem*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationSpecItem]**](CustomizationSpecItem.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_spec_item import ArrayOfCustomizationSpecItem

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationSpecItem from a JSON string
array_of_customization_spec_item_instance = ArrayOfCustomizationSpecItem.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationSpecItem.to_json()

# convert the object into a dict
array_of_customization_spec_item_dict = array_of_customization_spec_item_instance.to_dict()
# create an instance of ArrayOfCustomizationSpecItem from a dict
array_of_customization_spec_item_form_dict = array_of_customization_spec_item.from_dict(array_of_customization_spec_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


