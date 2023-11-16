# ArrayOfHostService

A boxed array of *HostService*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostService]**](HostService.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_service import ArrayOfHostService

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostService from a JSON string
array_of_host_service_instance = ArrayOfHostService.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostService.to_json()

# convert the object into a dict
array_of_host_service_dict = array_of_host_service_instance.to_dict()
# create an instance of ArrayOfHostService from a dict
array_of_host_service_form_dict = array_of_host_service.from_dict(array_of_host_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


