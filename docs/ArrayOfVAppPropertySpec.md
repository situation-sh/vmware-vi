# ArrayOfVAppPropertySpec

A boxed array of *VAppPropertySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppPropertySpec]**](VAppPropertySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_property_spec import ArrayOfVAppPropertySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppPropertySpec from a JSON string
array_of_v_app_property_spec_instance = ArrayOfVAppPropertySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppPropertySpec.to_json()

# convert the object into a dict
array_of_v_app_property_spec_dict = array_of_v_app_property_spec_instance.to_dict()
# create an instance of ArrayOfVAppPropertySpec from a dict
array_of_v_app_property_spec_form_dict = array_of_v_app_property_spec.from_dict(array_of_v_app_property_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


