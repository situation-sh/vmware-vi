# HostSubSpecificationUpdateEvent

This event suggests that update the host sub specification with the encapsulated copy.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_sub_spec** | [**HostSubSpecification**](HostSubSpecification.md) |  | 

## Example

```python
from vmware_vi.models.host_sub_specification_update_event import HostSubSpecificationUpdateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostSubSpecificationUpdateEvent from a JSON string
host_sub_specification_update_event_instance = HostSubSpecificationUpdateEvent.from_json(json)
# print the JSON string representation of the object
print HostSubSpecificationUpdateEvent.to_json()

# convert the object into a dict
host_sub_specification_update_event_dict = host_sub_specification_update_event_instance.to_dict()
# create an instance of HostSubSpecificationUpdateEvent from a dict
host_sub_specification_update_event_form_dict = host_sub_specification_update_event.from_dict(host_sub_specification_update_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


