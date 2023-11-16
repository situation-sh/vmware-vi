# VAppPropertySpec

An incremental update to the Property list.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**VAppPropertyInfo**](VAppPropertyInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_app_property_spec import VAppPropertySpec

# TODO update the JSON string below
json = "{}"
# create an instance of VAppPropertySpec from a JSON string
v_app_property_spec_instance = VAppPropertySpec.from_json(json)
# print the JSON string representation of the object
print VAppPropertySpec.to_json()

# convert the object into a dict
v_app_property_spec_dict = v_app_property_spec_instance.to_dict()
# create an instance of VAppPropertySpec from a dict
v_app_property_spec_form_dict = v_app_property_spec.from_dict(v_app_property_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


