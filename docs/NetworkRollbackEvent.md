# NetworkRollbackEvent

This event records when networking configuration on the host is rolled back as it disconnects the host from vCenter server.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_name** | **str** | Method name which caused the disconnect  ***Since:*** vSphere API 5.1  | 
**transaction_id** | **str** | Transaction ID for the method call that caused the disconnect  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.network_rollback_event import NetworkRollbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRollbackEvent from a JSON string
network_rollback_event_instance = NetworkRollbackEvent.from_json(json)
# print the JSON string representation of the object
print NetworkRollbackEvent.to_json()

# convert the object into a dict
network_rollback_event_dict = network_rollback_event_instance.to_dict()
# create an instance of NetworkRollbackEvent from a dict
network_rollback_event_form_dict = network_rollback_event.from_dict(network_rollback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


