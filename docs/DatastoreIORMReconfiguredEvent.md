# DatastoreIORMReconfiguredEvent

This event records that the configuration of storage I/O resource management for a datastore has changed.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.datastore_iorm_reconfigured_event import DatastoreIORMReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreIORMReconfiguredEvent from a JSON string
datastore_iorm_reconfigured_event_instance = DatastoreIORMReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreIORMReconfiguredEvent.to_json()

# convert the object into a dict
datastore_iorm_reconfigured_event_dict = datastore_iorm_reconfigured_event_instance.to_dict()
# create an instance of DatastoreIORMReconfiguredEvent from a dict
datastore_iorm_reconfigured_event_form_dict = datastore_iorm_reconfigured_event.from_dict(datastore_iorm_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


