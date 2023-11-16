# InvalidCAMServer

Fault indicating that the CAM server for camServer cannot be reached, or is not a valid IP address.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cam_server** | **str** | The address of the CAM server.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.invalid_cam_server import InvalidCAMServer

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidCAMServer from a JSON string
invalid_cam_server_instance = InvalidCAMServer.from_json(json)
# print the JSON string representation of the object
print InvalidCAMServer.to_json()

# convert the object into a dict
invalid_cam_server_dict = invalid_cam_server_instance.to_dict()
# create an instance of InvalidCAMServer from a dict
invalid_cam_server_form_dict = invalid_cam_server.from_dict(invalid_cam_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


