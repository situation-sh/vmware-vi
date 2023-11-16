# CustomizationSpecItem

Specification information and the Specification object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**CustomizationSpecInfo**](CustomizationSpecInfo.md) |  | 
**spec** | [**CustomizationSpec**](CustomizationSpec.md) |  | 

## Example

```python
from vmware_vi.models.customization_spec_item import CustomizationSpecItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSpecItem from a JSON string
customization_spec_item_instance = CustomizationSpecItem.from_json(json)
# print the JSON string representation of the object
print CustomizationSpecItem.to_json()

# convert the object into a dict
customization_spec_item_dict = customization_spec_item_instance.to_dict()
# create an instance of CustomizationSpecItem from a dict
customization_spec_item_form_dict = customization_spec_item.from_dict(customization_spec_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


