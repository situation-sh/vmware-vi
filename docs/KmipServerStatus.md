# KmipServerStatus

Data Object representing a KMIP server status.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**name** | **str** | Name for the KMIP server.  ***Since:*** vSphere API 6.5  | 
**status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**description** | **str** | KMIP server status description.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.kmip_server_status import KmipServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of KmipServerStatus from a JSON string
kmip_server_status_instance = KmipServerStatus.from_json(json)
# print the JSON string representation of the object
print KmipServerStatus.to_json()

# convert the object into a dict
kmip_server_status_dict = kmip_server_status_instance.to_dict()
# create an instance of KmipServerStatus from a dict
kmip_server_status_form_dict = kmip_server_status.from_dict(kmip_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


