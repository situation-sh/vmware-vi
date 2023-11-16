# RetrieveKmipServersStatusRequestType

The parameters of *CryptoManagerKmip.RetrieveKmipServersStatus_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[KmipClusterInfo]**](KmipClusterInfo.md) | \\[in\\] KMIP clusters and their servers.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_kmip_servers_status_request_type import RetrieveKmipServersStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveKmipServersStatusRequestType from a JSON string
retrieve_kmip_servers_status_request_type_instance = RetrieveKmipServersStatusRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveKmipServersStatusRequestType.to_json()

# convert the object into a dict
retrieve_kmip_servers_status_request_type_dict = retrieve_kmip_servers_status_request_type_instance.to_dict()
# create an instance of RetrieveKmipServersStatusRequestType from a dict
retrieve_kmip_servers_status_request_type_form_dict = retrieve_kmip_servers_status_request_type.from_dict(retrieve_kmip_servers_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


