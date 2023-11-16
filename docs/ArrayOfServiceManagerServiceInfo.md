# ArrayOfServiceManagerServiceInfo

A boxed array of *ServiceManagerServiceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceManagerServiceInfo]**](ServiceManagerServiceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_manager_service_info import ArrayOfServiceManagerServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceManagerServiceInfo from a JSON string
array_of_service_manager_service_info_instance = ArrayOfServiceManagerServiceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceManagerServiceInfo.to_json()

# convert the object into a dict
array_of_service_manager_service_info_dict = array_of_service_manager_service_info_instance.to_dict()
# create an instance of ArrayOfServiceManagerServiceInfo from a dict
array_of_service_manager_service_info_form_dict = array_of_service_manager_service_info.from_dict(array_of_service_manager_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


