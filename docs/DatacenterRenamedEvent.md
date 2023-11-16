# DatacenterRenamedEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old datacenter name.  ***Since:*** VI API 2.5  | 
**new_name** | **str** | The new datacenter name.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.datacenter_renamed_event import DatacenterRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterRenamedEvent from a JSON string
datacenter_renamed_event_instance = DatacenterRenamedEvent.from_json(json)
# print the JSON string representation of the object
print DatacenterRenamedEvent.to_json()

# convert the object into a dict
datacenter_renamed_event_dict = datacenter_renamed_event_instance.to_dict()
# create an instance of DatacenterRenamedEvent from a dict
datacenter_renamed_event_form_dict = datacenter_renamed_event.from_dict(datacenter_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


