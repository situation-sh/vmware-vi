# DasHeartbeatDatastoreInfo

Class for the selection of heartbeat datastores  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.das_heartbeat_datastore_info import DasHeartbeatDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DasHeartbeatDatastoreInfo from a JSON string
das_heartbeat_datastore_info_instance = DasHeartbeatDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print DasHeartbeatDatastoreInfo.to_json()

# convert the object into a dict
das_heartbeat_datastore_info_dict = das_heartbeat_datastore_info_instance.to_dict()
# create an instance of DasHeartbeatDatastoreInfo from a dict
das_heartbeat_datastore_info_form_dict = das_heartbeat_datastore_info.from_dict(das_heartbeat_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


