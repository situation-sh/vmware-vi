# ArrayOfHealthUpdateInfo

A boxed array of *HealthUpdateInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HealthUpdateInfo]**](HealthUpdateInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_health_update_info import ArrayOfHealthUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHealthUpdateInfo from a JSON string
array_of_health_update_info_instance = ArrayOfHealthUpdateInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHealthUpdateInfo.to_json()

# convert the object into a dict
array_of_health_update_info_dict = array_of_health_update_info_instance.to_dict()
# create an instance of ArrayOfHealthUpdateInfo from a dict
array_of_health_update_info_form_dict = array_of_health_update_info.from_dict(array_of_health_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


