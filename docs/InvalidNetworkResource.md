# InvalidNetworkResource

This fault is thrown when an operation to configure a NAS volume fails because the network resource specified is invalid.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the CIFS or NFS server.  ***Since:*** vSphere API 4.0  | 
**remote_path** | **str** | The remote share.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.invalid_network_resource import InvalidNetworkResource

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidNetworkResource from a JSON string
invalid_network_resource_instance = InvalidNetworkResource.from_json(json)
# print the JSON string representation of the object
print InvalidNetworkResource.to_json()

# convert the object into a dict
invalid_network_resource_dict = invalid_network_resource_instance.to_dict()
# create an instance of InvalidNetworkResource from a dict
invalid_network_resource_form_dict = invalid_network_resource.from_dict(invalid_network_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


