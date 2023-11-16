# MoveHostIntoRequestType

The parameters of *ClusterComputeResource.MoveHostInto_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**resource_pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.move_host_into_request_type import MoveHostIntoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveHostIntoRequestType from a JSON string
move_host_into_request_type_instance = MoveHostIntoRequestType.from_json(json)
# print the JSON string representation of the object
print MoveHostIntoRequestType.to_json()

# convert the object into a dict
move_host_into_request_type_dict = move_host_into_request_type_instance.to_dict()
# create an instance of MoveHostIntoRequestType from a dict
move_host_into_request_type_form_dict = move_host_into_request_type.from_dict(move_host_into_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


