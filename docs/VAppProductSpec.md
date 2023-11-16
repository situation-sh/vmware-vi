# VAppProductSpec

An incremental update to the Product information list.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**VAppProductInfo**](VAppProductInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_app_product_spec import VAppProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VAppProductSpec from a JSON string
v_app_product_spec_instance = VAppProductSpec.from_json(json)
# print the JSON string representation of the object
print VAppProductSpec.to_json()

# convert the object into a dict
v_app_product_spec_dict = v_app_product_spec_instance.to_dict()
# create an instance of VAppProductSpec from a dict
v_app_product_spec_form_dict = v_app_product_spec.from_dict(v_app_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


