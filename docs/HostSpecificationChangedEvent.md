# HostSpecificationChangedEvent

This event records that the host specification was changed.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_specification_changed_event import HostSpecificationChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostSpecificationChangedEvent from a JSON string
host_specification_changed_event_instance = HostSpecificationChangedEvent.from_json(json)
# print the JSON string representation of the object
print HostSpecificationChangedEvent.to_json()

# convert the object into a dict
host_specification_changed_event_dict = host_specification_changed_event_instance.to_dict()
# create an instance of HostSpecificationChangedEvent from a dict
host_specification_changed_event_form_dict = host_specification_changed_event.from_dict(host_specification_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


