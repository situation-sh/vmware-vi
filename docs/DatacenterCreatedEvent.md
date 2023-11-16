# DatacenterCreatedEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**FolderEventArgument**](FolderEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.datacenter_created_event import DatacenterCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterCreatedEvent from a JSON string
datacenter_created_event_instance = DatacenterCreatedEvent.from_json(json)
# print the JSON string representation of the object
print DatacenterCreatedEvent.to_json()

# convert the object into a dict
datacenter_created_event_dict = datacenter_created_event_instance.to_dict()
# create an instance of DatacenterCreatedEvent from a dict
datacenter_created_event_form_dict = datacenter_created_event.from_dict(datacenter_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


