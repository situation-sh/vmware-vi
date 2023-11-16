# ExtExtendedProductInfo

This data object encapsulates extended product information for an extension.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_url** | **str** | URL to extension vendor.  ***Since:*** vSphere API 5.0  | [optional] 
**product_url** | **str** | URL to vendor&#39;s description of this extension.  ***Since:*** vSphere API 5.0  | [optional] 
**management_url** | **str** | URL to management UI for this extension.  ***Since:*** vSphere API 5.0  | [optional] 
**var_self** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.ext_extended_product_info import ExtExtendedProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtExtendedProductInfo from a JSON string
ext_extended_product_info_instance = ExtExtendedProductInfo.from_json(json)
# print the JSON string representation of the object
print ExtExtendedProductInfo.to_json()

# convert the object into a dict
ext_extended_product_info_dict = ext_extended_product_info_instance.to_dict()
# create an instance of ExtExtendedProductInfo from a dict
ext_extended_product_info_form_dict = ext_extended_product_info.from_dict(ext_extended_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


