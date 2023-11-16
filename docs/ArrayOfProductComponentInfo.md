# ArrayOfProductComponentInfo

A boxed array of *ProductComponentInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProductComponentInfo]**](ProductComponentInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_product_component_info import ArrayOfProductComponentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProductComponentInfo from a JSON string
array_of_product_component_info_instance = ArrayOfProductComponentInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfProductComponentInfo.to_json()

# convert the object into a dict
array_of_product_component_info_dict = array_of_product_component_info_instance.to_dict()
# create an instance of ArrayOfProductComponentInfo from a dict
array_of_product_component_info_form_dict = array_of_product_component_info.from_dict(array_of_product_component_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


