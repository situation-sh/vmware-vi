# DropConnectionsRequestType

The parameters of *VirtualMachine.DropConnections*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_of_connections** | [**List[VirtualMachineConnection]**](VirtualMachineConnection.md) |  | [optional] 

## Example

```python
from vmware_vi.models.drop_connections_request_type import DropConnectionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DropConnectionsRequestType from a JSON string
drop_connections_request_type_instance = DropConnectionsRequestType.from_json(json)
# print the JSON string representation of the object
print DropConnectionsRequestType.to_json()

# convert the object into a dict
drop_connections_request_type_dict = drop_connections_request_type_instance.to_dict()
# create an instance of DropConnectionsRequestType from a dict
drop_connections_request_type_form_dict = drop_connections_request_type.from_dict(drop_connections_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


