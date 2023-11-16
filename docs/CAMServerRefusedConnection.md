# CAMServerRefusedConnection

Fault indicating that the CAM server cannot be connected.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cam_server_refused_connection import CAMServerRefusedConnection

# TODO update the JSON string below
json = "{}"
# create an instance of CAMServerRefusedConnection from a JSON string
cam_server_refused_connection_instance = CAMServerRefusedConnection.from_json(json)
# print the JSON string representation of the object
print CAMServerRefusedConnection.to_json()

# convert the object into a dict
cam_server_refused_connection_dict = cam_server_refused_connection_instance.to_dict()
# create an instance of CAMServerRefusedConnection from a dict
cam_server_refused_connection_form_dict = cam_server_refused_connection.from_dict(cam_server_refused_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


