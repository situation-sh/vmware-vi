# ArrayOfVAppProductSpec

A boxed array of *VAppProductSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppProductSpec]**](VAppProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_product_spec import ArrayOfVAppProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppProductSpec from a JSON string
array_of_v_app_product_spec_instance = ArrayOfVAppProductSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppProductSpec.to_json()

# convert the object into a dict
array_of_v_app_product_spec_dict = array_of_v_app_product_spec_instance.to_dict()
# create an instance of ArrayOfVAppProductSpec from a dict
array_of_v_app_product_spec_form_dict = array_of_v_app_product_spec.from_dict(array_of_v_app_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


