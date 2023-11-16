# HostSpecificationUpdateEvent

This event suggests that update the host specification with the encapsulated copy.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_spec** | [**HostSpecification**](HostSpecification.md) |  | 

## Example

```python
from vmware_vi.models.host_specification_update_event import HostSpecificationUpdateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostSpecificationUpdateEvent from a JSON string
host_specification_update_event_instance = HostSpecificationUpdateEvent.from_json(json)
# print the JSON string representation of the object
print HostSpecificationUpdateEvent.to_json()

# convert the object into a dict
host_specification_update_event_dict = host_specification_update_event_instance.to_dict()
# create an instance of HostSpecificationUpdateEvent from a dict
host_specification_update_event_form_dict = host_specification_update_event.from_dict(host_specification_update_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


