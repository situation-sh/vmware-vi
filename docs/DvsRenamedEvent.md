# DvsRenamedEvent

A distributed virtual switch was renamed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old DistributedVirtualSwitch name.  ***Since:*** vSphere API 4.0  | 
**new_name** | **str** | The new DistributedVirtualSwitch name.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_renamed_event import DvsRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsRenamedEvent from a JSON string
dvs_renamed_event_instance = DvsRenamedEvent.from_json(json)
# print the JSON string representation of the object
print DvsRenamedEvent.to_json()

# convert the object into a dict
dvs_renamed_event_dict = dvs_renamed_event_instance.to_dict()
# create an instance of DvsRenamedEvent from a dict
dvs_renamed_event_form_dict = dvs_renamed_event.from_dict(dvs_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


