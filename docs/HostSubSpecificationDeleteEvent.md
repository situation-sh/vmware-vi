# HostSubSpecificationDeleteEvent

This event suggests that delete the host sub specification specified by name.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_spec_name** | **str** |  | 

## Example

```python
from vmware_vi.models.host_sub_specification_delete_event import HostSubSpecificationDeleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostSubSpecificationDeleteEvent from a JSON string
host_sub_specification_delete_event_instance = HostSubSpecificationDeleteEvent.from_json(json)
# print the JSON string representation of the object
print HostSubSpecificationDeleteEvent.to_json()

# convert the object into a dict
host_sub_specification_delete_event_dict = host_sub_specification_delete_event_instance.to_dict()
# create an instance of HostSubSpecificationDeleteEvent from a dict
host_sub_specification_delete_event_form_dict = host_sub_specification_delete_event.from_dict(host_sub_specification_delete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


