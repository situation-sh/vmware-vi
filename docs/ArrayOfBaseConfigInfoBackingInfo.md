# ArrayOfBaseConfigInfoBackingInfo

A boxed array of *BaseConfigInfoBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BaseConfigInfoBackingInfo]**](BaseConfigInfoBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_base_config_info_backing_info import ArrayOfBaseConfigInfoBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBaseConfigInfoBackingInfo from a JSON string
array_of_base_config_info_backing_info_instance = ArrayOfBaseConfigInfoBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfBaseConfigInfoBackingInfo.to_json()

# convert the object into a dict
array_of_base_config_info_backing_info_dict = array_of_base_config_info_backing_info_instance.to_dict()
# create an instance of ArrayOfBaseConfigInfoBackingInfo from a dict
array_of_base_config_info_backing_info_form_dict = array_of_base_config_info_backing_info.from_dict(array_of_base_config_info_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


