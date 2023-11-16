# NasConnectionLimitReached

This fault is thrown when an operation to configure a CIFS volume fails because the request exceeds the maximum allowed connections on this host for the specified remote path.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the NFS server.  ***Since:*** vSphere API 4.0  | 
**remote_path** | **str** | The remote share.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.nas_connection_limit_reached import NasConnectionLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of NasConnectionLimitReached from a JSON string
nas_connection_limit_reached_instance = NasConnectionLimitReached.from_json(json)
# print the JSON string representation of the object
print NasConnectionLimitReached.to_json()

# convert the object into a dict
nas_connection_limit_reached_dict = nas_connection_limit_reached_instance.to_dict()
# create an instance of NasConnectionLimitReached from a dict
nas_connection_limit_reached_form_dict = nas_connection_limit_reached.from_dict(nas_connection_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


