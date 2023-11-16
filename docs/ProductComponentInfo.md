# ProductComponentInfo

ProductComponentInfo data object type describes installed components.  Product component is defined as a software module that is released and versioned independently but has dependency relationship with other products. If one product, for usability or any other reason, bundles other products, ProductComponentInfo type may be used to describe installed components. For example, ESX product may bundle VI Client in its releases.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Opaque identifier that is unique for this product component  ***Since:*** VI API 2.5  | 
**name** | **str** | Canonical name of product component  ***Since:*** VI API 2.5  | 
**version** | **str** | Version of product component  ***Since:*** VI API 2.5  | 
**release** | **int** | Release property is a number which increments with each new release of product.  Product release may not rev version but release number is always incremented.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.product_component_info import ProductComponentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductComponentInfo from a JSON string
product_component_info_instance = ProductComponentInfo.from_json(json)
# print the JSON string representation of the object
print ProductComponentInfo.to_json()

# convert the object into a dict
product_component_info_dict = product_component_info_instance.to_dict()
# create an instance of ProductComponentInfo from a dict
product_component_info_form_dict = product_component_info.from_dict(product_component_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


