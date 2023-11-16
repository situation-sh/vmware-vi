# MoveIntoResourcePoolRequestType

The parameters of *ResourcePool.MoveIntoResourcePool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | A list of ResourcePool and VirtualMachine objects.  Refers instances of *ManagedEntity*.  | 

## Example

```python
from vmware_vi.models.move_into_resource_pool_request_type import MoveIntoResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveIntoResourcePoolRequestType from a JSON string
move_into_resource_pool_request_type_instance = MoveIntoResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print MoveIntoResourcePoolRequestType.to_json()

# convert the object into a dict
move_into_resource_pool_request_type_dict = move_into_resource_pool_request_type_instance.to_dict()
# create an instance of MoveIntoResourcePoolRequestType from a dict
move_into_resource_pool_request_type_form_dict = move_into_resource_pool_request_type.from_dict(move_into_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


