# ArrayOfVAppProductInfo

A boxed array of *VAppProductInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppProductInfo]**](VAppProductInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_product_info import ArrayOfVAppProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppProductInfo from a JSON string
array_of_v_app_product_info_instance = ArrayOfVAppProductInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppProductInfo.to_json()

# convert the object into a dict
array_of_v_app_product_info_dict = array_of_v_app_product_info_instance.to_dict()
# create an instance of ArrayOfVAppProductInfo from a dict
array_of_v_app_product_info_form_dict = array_of_v_app_product_info.from_dict(array_of_v_app_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


