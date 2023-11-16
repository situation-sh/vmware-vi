# ArrayOfExtExtendedProductInfo

A boxed array of *ExtExtendedProductInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtExtendedProductInfo]**](ExtExtendedProductInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ext_extended_product_info import ArrayOfExtExtendedProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtExtendedProductInfo from a JSON string
array_of_ext_extended_product_info_instance = ArrayOfExtExtendedProductInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtExtendedProductInfo.to_json()

# convert the object into a dict
array_of_ext_extended_product_info_dict = array_of_ext_extended_product_info_instance.to_dict()
# create an instance of ArrayOfExtExtendedProductInfo from a dict
array_of_ext_extended_product_info_form_dict = array_of_ext_extended_product_info.from_dict(array_of_ext_extended_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


