# ArrayOfCAMServerRefusedConnection

A boxed array of *CAMServerRefusedConnection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CAMServerRefusedConnection]**](CAMServerRefusedConnection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cam_server_refused_connection import ArrayOfCAMServerRefusedConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCAMServerRefusedConnection from a JSON string
array_of_cam_server_refused_connection_instance = ArrayOfCAMServerRefusedConnection.from_json(json)
# print the JSON string representation of the object
print ArrayOfCAMServerRefusedConnection.to_json()

# convert the object into a dict
array_of_cam_server_refused_connection_dict = array_of_cam_server_refused_connection_instance.to_dict()
# create an instance of ArrayOfCAMServerRefusedConnection from a dict
array_of_cam_server_refused_connection_form_dict = array_of_cam_server_refused_connection.from_dict(array_of_cam_server_refused_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


