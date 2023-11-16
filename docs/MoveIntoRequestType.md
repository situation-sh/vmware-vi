# MoveIntoRequestType

The parameters of *ClusterComputeResource.MoveInto_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of hosts to move into the cluster.  ***Required privileges:*** Host.Inventory.MoveHost  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.move_into_request_type import MoveIntoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveIntoRequestType from a JSON string
move_into_request_type_instance = MoveIntoRequestType.from_json(json)
# print the JSON string representation of the object
print MoveIntoRequestType.to_json()

# convert the object into a dict
move_into_request_type_dict = move_into_request_type_instance.to_dict()
# create an instance of MoveIntoRequestType from a dict
move_into_request_type_form_dict = move_into_request_type.from_dict(move_into_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


