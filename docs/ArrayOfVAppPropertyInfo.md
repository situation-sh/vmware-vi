# ArrayOfVAppPropertyInfo

A boxed array of *VAppPropertyInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppPropertyInfo]**](VAppPropertyInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_property_info import ArrayOfVAppPropertyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppPropertyInfo from a JSON string
array_of_v_app_property_info_instance = ArrayOfVAppPropertyInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppPropertyInfo.to_json()

# convert the object into a dict
array_of_v_app_property_info_dict = array_of_v_app_property_info_instance.to_dict()
# create an instance of ArrayOfVAppPropertyInfo from a dict
array_of_v_app_property_info_form_dict = array_of_v_app_property_info.from_dict(array_of_v_app_property_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


